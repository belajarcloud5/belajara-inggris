#!/usr/bin/env python3
"""Bangun site/data/*.json dari content/*.py (hanya stdlib). Pakai: python3 build.py"""
import importlib.util, json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "content"))
OUT = os.path.join(ROOT, "site", "data")
os.makedirs(OUT, exist_ok=True)
from helpers import fill  # noqa: E402


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def qkey(q):
    t = q["type"]
    if t == "fill":
        return ("fill", q["id"], q["q"])
    if t == "order":
        return ("order", q["answer"].lower())
    if t == "match":
        return ("match", tuple(sorted(p[0] for p in q["pairs"])))
    if t == "dictate":
        return ("dictate", q["answer"].lower())
    if t == "reply":
        return ("reply", q["turns"][-1][1].lower(), q["id"].lower())
    return (t, q["q"], tuple(sorted(q["options"])))


def qid(q):
    """Kunci pendek yang stabil untuk melacak soal (dipakai fitur 'Ulangi yang salah')."""
    import hashlib
    t = q["type"]
    if t == "fill":
        raw = ["fill", q["id"], q["q"], sorted(q["answers"])]
    elif t == "order":
        raw = ["order", q["q"], q["answer"]]
    elif t == "dictate":
        raw = ["dictate", q["say"], q["answer"]]
    elif t == "reply":
        raw = ["reply", q["turns"], q["id"], sorted(q["answers"])]
    elif t == "match":
        raw = ["match", q["q"], sorted(map(list, q["pairs"]))]
    else:
        raw = [t, q["q"], q.get("say", ""), sorted(q["options"]), q["options"][q["answer"]]]
    return hashlib.md5(json.dumps(raw, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:8]


def dedupe(uid, kind, qs):
    seen, out = set(), []
    for q in qs:
        k = qkey(q)
        if k in seen:
            print(f"  duplikat dibuang: {uid}.{kind}: {str(k[1])[:50]}")
            continue
        seen.add(k); out.append(q)
    return out



GENERIC = {"word.", "complete.", "tr.", "ant.", "fix.", "odd.", "syn.", "dialog.", "situation.", "Sopan.", "form.", "past."}
TYPE_RULE = {
    "Type 1.": "Conditional type 1: if + present simple, ... will + kata kerja dasar.",
    "Type 2.": "Conditional type 2: if + past simple, ... would + kata kerja dasar.",
    "Type 3.": "Conditional type 3: if + past perfect, ... would have + V3.",
    "past.": "Kejadian sudah selesai, jadi memakai past simple.",
}


def answer_text(q):
    t = q["type"]
    if t in ("mcq", "listen"):
        return q["options"][q["answer"]]
    if t == "fill":
        return q["answers"][0]
    if t == "order":
        return q["answer"]
    return None


def enrich_exp(q):
    """Penjelasan yang terlalu pendek ('word.', 'fix.', ...) diganti penjelasan yang memuat jawaban/kalimat lengkapnya."""
    e = q["exp"].strip()
    if len(e) > 12:
        return
    a = answer_text(q)
    if not a:
        return
    qs = q.get("q", "")
    m = re.search(r'"([^"]+)"', qs)
    w = m.group(1) if m else ""
    lengkap = None
    dot = "" if a[-1] in ".?!" else "."
    if "___" in qs and q["type"] in ("mcq", "listen", "fill"):
        mm = re.search(r'"([^"]*___[^"]*)"', qs)
        if mm and " – " not in qs:
            lengkap = mm.group(1).replace("___", a)
    if e == "word." and w:
        out = f'"{w}" dalam bahasa Inggris: **{a}**{dot}'
    elif e == "tr.":
        out = f"Terjemahan yang tepat: **{a}**{dot}"
    elif e == "ant." and w:
        out = f'Antonim (lawan kata) "{w}" adalah **{a}**{dot}'
    elif e == "syn." and w:
        out = f'Sinonim (kata yang artinya hampir sama) "{w}" adalah **{a}**{dot}'
    elif e == "form." and w:
        out = f'Bentuk yang benar dari "{w}": **{a}**{dot}'
    elif e == "fix." and w and w != a:
        out = f"Salah: ~~{w}~~ → Benar: **{a}**{dot}"
    elif e == "dialog.":
        out = f"Balasan yang wajar untuk pertanyaan itu: **{a}**{dot}"
    elif e == "odd." and re.search(r"bukan|tidak sama|kecuali|ganjil|SALAH", qs) and q["type"] == "mcq":
        lain = " / ".join(o for i, o in enumerate(q["options"]) if i != q["answer"])
        out = f"Yang berbeda: **{a}**{dot} Pilihan lain ({lain}) satu kelompok."
    elif lengkap:
        out = (TYPE_RULE.get(e, e) + " " if e in TYPE_RULE else (e + " " if e not in GENERIC else "")) + f"Kalimat lengkap: **{lengkap}**"
    else:
        out = (TYPE_RULE[e] + " " if e in TYPE_RULE else (e + " " if e not in GENERIC else "")) + f"Jawaban yang tepat: **{a}**{dot}"
    q["exp"] = out



BE_DO_HAVE = {"am", "is", "are", "was", "were", "be", "been", "being", "do", "does", "did", "have", "has", "had", "don't", "doesn't", "didn't", "isn't", "aren't", "wasn't", "weren't"}
PREP = {"to", "for", "by", "on", "in", "at", "of", "with", "from", "into", "about", "since"}


def to_fill(q):
    """Ubah pilihan ganda 'Lengkapi ___' yang jawabannya tunggal menjadi soal isian ketik. None bila rawan ambigu."""
    if q["type"] != "mcq" or q["q"].count("___") != 1 or " – " in q["q"]:
        return None
    m = re.search(r'"([^"]*___[^"]*)"', q["q"])
    if not m:
        return None
    a = q["options"][q["answer"]]
    others = [o for i, o in enumerate(q["options"]) if i != q["answer"]]
    words = [x.lower() for x in q["options"]]
    if len(a.split()) > 3 or not re.fullmatch(r"[A-Za-z' ]+", a):
        return None
    closed = all(x in BE_DO_HAVE for x in words) or all(x in PREP for x in words)
    stem = a.split()[-1].lower()[:3]
    par = re.search(r"\(([^)]+)\)\s*$", q["q"])
    # bentuk kata kerja hanya bila kata dasarnya disebut di kurung, mis. "(easy)" -> easier; kalau tidak, ada sinonim lain
    inflect = bool(par) and len(stem) == 3 and par.group(1).strip().lower()[:3] == stem and sum(o.split()[-1].lower().startswith(stem) for o in others) >= 2
    if not (closed or inflect):
        return None
    sent = m.group(1) + (f" ({par.group(1)})" if par else "")
    hint = " / ".join(w[0] + (" " + " ".join("_" * (len(w) - 1)) if len(w) > 1 else "") for w in a.split())
    answers = [a]
    if a.lower().endswith("n't") and len(a.split()) == 1:  # aren't = are not
        answers.append(a[:-3] + " not" if a.lower() != "can't" else "cannot")
    f = fill("", sent, answers, hint, q["exp"])
    f["g"] = q["k"]
    return f


def check_q(uid, kind, i, q):
    where = f"{uid}.{kind}[{i}]"
    t = q.get("type")
    assert t in ("mcq", "listen", "fill", "order", "match", "dictate", "reply"), f"{where}: tipe tidak dikenal {t}"
    assert q.get("exp"), f"{where}: penjelasan (exp) kosong"
    if t in ("mcq", "listen"):
        assert len(q["options"]) >= 3 and 0 <= q["answer"] < len(q["options"]), f"{where}: opsi/answer salah"
        assert len(set(q["options"])) == len(q["options"]), f"{where}: opsi duplikat"
        if t == "listen":
            assert q.get("say"), f"{where}: listen butuh 'say'"
    elif t == "fill":
        assert "___" in q["q"] and q["answers"], f"{where}: fill butuh ___ dan answers"
    elif t == "order":
        assert len(q["answer"].split()) >= 3, f"{where}: kalimat terlalu pendek"
    elif t == "reply":
        assert q.get("turns") and q["turns"][-1][0] != "You" and q.get("id") and q.get("scene"), f"{where}: reply butuh scene, turns (terakhir lawan bicara), id"
        assert len(q["answers"]) >= 3 or q.get("keys"), f"{where}: reply butuh >=3 jawaban contoh atau kata kunci"
        assert all(len(a.split()) >= 2 for a in q["answers"]), f"{where}: jawaban contoh min. 2 kata"
    elif t == "dictate":
        assert q.get("say") and len(q["answer"].split()) >= 3, f"{where}: dikte butuh 'say' dan kalimat min. 3 kata"
        assert not any(ch.isdigit() for ch in q["answer"]), f"{where}: dikte tanpa angka (tulis dengan huruf)"
    elif t == "match":
        assert len(q["pairs"]) >= 3, f"{where}: pasangan kurang dari 3"
        assert len({a for a, _ in q["pairs"]}) == len(q["pairs"]) == len({b for _, b in q["pairs"]}), f"{where}: pasangan duplikat"


def main():
    units = load(os.path.join(ROOT, "content", "units.py")).UNITS
    index = []
    kamus = []
    n_conv = 0
    for u in units:
        entry = {k: u[k] for k in ("id", "kelas", "no", "judul", "title", "emoji", "ringkas")}
        p = os.path.join(ROOT, "content", f"{u['id']}.py")
        entry["ready"] = os.path.isfile(p)
        if entry["ready"]:
            d = load(p).UNIT
            assert d["id"] == u["id"], f"{p}: id tidak cocok"
            for suffix, var in (("extra", "EXTRA"), ("more", "MORE"), ("plus", "PLUS"), ("ext", "EXT"), ("quiz", "QUIZ"), ("bank", "BANK"), ("q2", "Q2"), ("p2", "P2"), ("r3", "R3"), ("r4", "R4"), ("f5", "F5"), ("dict", "D"), ("ord", "ORD"), ("rep", "REP")):  # bank soal tambahan
                xp = os.path.join(ROOT, "content", f"{u['id']}_{suffix}.py")
                if os.path.isfile(xp):
                    x = getattr(load(xp), var)
                    d["practice"] = dedupe(u["id"], "practice", d["practice"] + x.get("practice", []))
                    d["quiz"] = dedupe(u["id"], "quiz", d["quiz"] + x.get("quiz", []))
            for kind in ("practice", "quiz"):
                for i, q in enumerate(d[kind]):
                    check_q(u["id"], kind, i, q)
            rp = os.path.join(ROOT, "content", f"{u['id']}_read.py")
            d["read"] = load(rp).READ if os.path.isfile(rp) else []
            rp2 = os.path.join(ROOT, "content", f"{u['id']}_read2.py")
            if os.path.isfile(rp2):  # cerita tambahan dengan soal beragam (fokus tenses)
                d["read"] = d["read"] + load(rp2).READ2
            rp3 = os.path.join(ROOT, "content", f"{u['id']}_read3.py")
            if os.path.isfile(rp3):  # cerita fokus tenses ke-2
                d["read"] = d["read"] + load(rp3).READ3
            for pi, ps in enumerate(d["read"]):
                assert ps.get("title") and ps.get("text") and ps.get("id"), f"{u['id']}.read[{pi}]: judul/teks/terjemahan kosong"
                assert 3 <= len(ps["qs"]) <= 8, f"{u['id']}.read[{pi}]: butuh 3 sampai 8 pertanyaan"
                for qi, q in enumerate(ps["qs"]):
                    assert q["type"] in ("mcq", "fill", "order", "match"), f"{u['id']}.read[{pi}][{qi}]: tipe {q['type']} tidak didukung di bacaan"
                    check_q(u["id"], f"read{pi}", qi, q)
            assert len(d["quiz"]) >= 8, f"{u['id']}: kuis minimal 8 soal"
            for kind in ("practice", "quiz"):
                for q in d[kind]:
                    q["k"] = qid(q)
                    enrich_exp(q)
                nf = [x for x in (to_fill(q) for q in d[kind] if q["type"] == "mcq") if x]
                for x in nf:
                    x["k"] = qid(x)
                for q in d[kind]:
                    if any(x["g"] == q["k"] for x in nf):
                        q["g"] = q["k"]
                d[kind] = dedupe(u["id"], kind, d[kind] + nf)
                n_conv += len(nf)
            for blk in d["lesson"]:
                if blk.get("t") == "vocab":
                    for it in blk["items"]:
                        if it.get("id"):
                            kamus.append({"en": it["en"], "id": it["id"], "ex": it.get("ex", ""), "u": u["id"], "no": u["no"], "kelas": u["kelas"]})
            d = {**entry, **{k: d[k] for k in ("goals", "lesson", "practice", "quiz", "read")}}
            json.dump(d, open(os.path.join(OUT, f"{u['id']}.json"), "w"), ensure_ascii=False, separators=(",", ":"))
            entry["practice_n"], entry["quiz_n"] = len(d["practice"]), len(d["quiz"])
            entry["read_n"] = len(d["read"])
        index.append(entry)
    json.dump(index, open(os.path.join(OUT, "index.json"), "w"), ensure_ascii=False, indent=1)
    seen, out = set(), []
    for it in kamus:  # buang kata kembar, simpan kemunculan pertama
        key = it["en"].lower()
        if key not in seen:
            seen.add(key); out.append(it)
    out.sort(key=lambda x: x["en"].lower())
    json.dump(out, open(os.path.join(OUT, "kamus.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    print(f"kamus: {len(out)} kata; soal isian hasil konversi: {n_conv}")
    print(f"{sum(e['ready'] for e in index)}/{len(index)} unit siap")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("GAGAL:", e); sys.exit(1)
