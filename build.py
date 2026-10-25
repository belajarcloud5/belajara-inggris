#!/usr/bin/env python3
"""Bangun site/data/*.json dari content/*.py (hanya stdlib). Pakai: python3 build.py"""
import importlib.util, json, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "content"))
OUT = os.path.join(ROOT, "site", "data")
os.makedirs(OUT, exist_ok=True)


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


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
    for u in units:
        entry = {k: u[k] for k in ("id", "kelas", "no", "judul", "title", "emoji", "ringkas")}
        p = os.path.join(ROOT, "content", f"{u['id']}.py")
        entry["ready"] = os.path.isfile(p)
        if entry["ready"]:
            d = load(p).UNIT
            assert d["id"] == u["id"], f"{p}: id tidak cocok"
            for kind in ("practice", "quiz"):
                for i, q in enumerate(d[kind]):
                    check_q(u["id"], kind, i, q)
            assert len(d["quiz"]) >= 8, f"{u['id']}: kuis minimal 8 soal"
            d = {**entry, **{k: d[k] for k in ("goals", "lesson", "practice", "quiz")}}
            json.dump(d, open(os.path.join(OUT, f"{u['id']}.json"), "w"), ensure_ascii=False, separators=(",", ":"))
            entry["practice_n"], entry["quiz_n"] = len(d["practice"]), len(d["quiz"])
        index.append(entry)
    json.dump(index, open(os.path.join(OUT, "index.json"), "w"), ensure_ascii=False, indent=1)
    print(f"{sum(e['ready'] for e in index)}/{len(index)} unit siap")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("GAGAL:", e); sys.exit(1)
