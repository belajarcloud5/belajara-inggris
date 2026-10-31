#!/usr/bin/env python3
"""Bangun site/data/*.json dari content/*.py (hanya stdlib). Pakai: python3 build.py"""
import importlib.util, json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "content"))
OUT = os.path.join(ROOT, "site", "data")
os.makedirs(OUT, exist_ok=True)


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
    return (t, q["q"], tuple(sorted(q["options"])))


def qid(q):
    """Kunci pendek yang stabil untuk melacak soal (dipakai fitur 'Ulangi yang salah')."""
    import hashlib
    t = q["type"]
    if t == "fill":
        raw = ["fill", q["id"], q["q"], sorted(q["answers"])]
    elif t == "order":
        raw = ["order", q["q"], q["answer"]]
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


def check_q(uid, kind, i, q):
    where = f"{uid}.{kind}[{i}]"
    t = q.get("type")
    assert t in ("mcq", "listen", "fill", "order", "match"), f"{where}: tipe tidak dikenal {t}"
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
    elif t == "match":
        assert len(q["pairs"]) >= 3, f"{where}: pasangan kurang dari 3"
        assert len({a for a, _ in q["pairs"]}) == len(q["pairs"]) == len({b for _, b in q["pairs"]}), f"{where}: pasangan duplikat"


def main():
    units = load(os.path.join(ROOT, "content", "units.py")).UNITS
    index = []
    kamus = []
    for u in units:
        entry = {k: u[k] for k in ("id", "kelas", "no", "judul", "title", "emoji", "ringkas")}
        p = os.path.join(ROOT, "content", f"{u['id']}.py")
        entry["ready"] = os.path.isfile(p)
        if entry["ready"]:
            d = load(p).UNIT
            assert d["id"] == u["id"], f"{p}: id tidak cocok"
            for suffix, var in (("extra", "EXTRA"), ("more", "MORE"), ("plus", "PLUS"), ("ext", "EXT"), ("quiz", "QUIZ"), ("bank", "BANK"), ("q2", "Q2"), ("p2", "P2"), ("r3", "R3"), ("r4", "R4")):  # bank soal tambahan
                xp = os.path.join(ROOT, "content", f"{u['id']}_{suffix}.py")
                if os.path.isfile(xp):
                    x = getattr(load(xp), var)
                    d["practice"] = dedupe(u["id"], "practice", d["practice"] + x.get("practice", []))
                    d["quiz"] = dedupe(u["id"], "quiz", d["quiz"] + x.get("quiz", []))
            for kind in ("practice", "quiz"):
                for i, q in enumerate(d[kind]):
                    check_q(u["id"], kind, i, q)
            assert len(d["quiz"]) >= 8, f"{u['id']}: kuis minimal 8 soal"
            for kind in ("practice", "quiz"):
                for q in d[kind]:
                    q["k"] = qid(q)
                    enrich_exp(q)
            for blk in d["lesson"]:
                if blk.get("t") == "vocab":
                    for it in blk["items"]:
                        if it.get("id"):
                            kamus.append({"en": it["en"], "id": it["id"], "ex": it.get("ex", ""), "u": u["id"], "no": u["no"], "kelas": u["kelas"]})
            d = {**entry, **{k: d[k] for k in ("goals", "lesson", "practice", "quiz")}}
            json.dump(d, open(os.path.join(OUT, f"{u['id']}.json"), "w"), ensure_ascii=False, separators=(",", ":"))
            entry["practice_n"], entry["quiz_n"] = len(d["practice"]), len(d["quiz"])
        index.append(entry)
    json.dump(index, open(os.path.join(OUT, "index.json"), "w"), ensure_ascii=False, indent=1)
    seen, out = set(), []
    for it in kamus:  # buang kata kembar, simpan kemunculan pertama
        key = it["en"].lower()
        if key not in seen:
            seen.add(key); out.append(it)
    out.sort(key=lambda x: x["en"].lower())
    json.dump(out, open(os.path.join(OUT, "kamus.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    print(f"kamus: {len(out)} kata")
    print(f"{sum(e['ready'] for e in index)}/{len(index)} unit siap")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("GAGAL:", e); sys.exit(1)
