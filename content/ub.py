"""Pembangun unit baru (modul pelafalan, kosakata, TOEIC)."""
import random
from helpers import mcq, fill, order, match, listen
from qk import mk, mkf, mko, mkd, mkr

def mkunit(id, goals, lesson, practice, quiz):
    return dict(id=id, goals=goals, lesson=lesson, practice=practice, quiz=quiz)

def intro(text): return dict(t="intro", text=text)
def tip(title, text): return dict(t="tip", title=title, text=text)
def warn(title, text): return dict(t="warn", title=title, text=text)
def summary(items): return dict(t="summary", items=items)
def gram(title, text=None, table=None, examples=None):
    d = dict(t="grammar", title=title)
    if text: d["text"] = text
    if table: d["table"] = table
    if examples: d["examples"] = [dict(en=e, id=i) for e, i in examples]
    return d
def vocab(title, rows):
    """rows: (en, id, contoh atau '')."""
    return dict(t="vocab", title=title, items=[dict(en=e, id=i, ex=x) if x else dict(en=e, id=i) for e, i, x in rows])
def dialog(title, lines):
    """lines: (nama, en, id)."""
    return dict(t="dialog", title=title, lines=[dict(who=w, en=e, id=i) for w, e, i in lines])

def listen_words(triples, say_fmt="{w}", q="Dengarkan. Kata mana yang kamu dengar?", per=1, seed=1, exp_fmt="Kata yang diucapkan: {w}.", subset=None):
    """triples: tuple kata yang mirip bunyinya. Tiap kata dibuat satu soal listen (opsi = semua kata dalam tuple)."""
    rng = random.Random(seed)
    items = []
    for tr in triples:
        for w in tr:
            opts = [w] + [x for x in tr if x != w]
            items.append(listen(q, say_fmt.format(w=w), opts, 0, exp_fmt.format(w=w)))
    rng.shuffle(items)
    return items[:subset] if subset else items

def dictate(sents):
    return mkd(sents)


import re as _re

def vocab_unit(id, goals, intro_text, groups, dlg_title, dlg_lines, tip_text, seed=1):
    """Unit kosakata bertema. groups = [(judul, [(en, arti, contoh)])]; soal dibangkitkan otomatis dari daftar kata."""
    rng = random.Random(seed)
    words = [r for _, rows in groups for r in rows]
    lesson = [intro(intro_text)]
    for i, (t, rows) in enumerate(groups, 1):
        lesson.append(vocab(f"{i}. {t}", rows))
    lesson.append(dialog(dlg_title, dlg_lines))
    lesson.append(tip("Cara menghafal", tip_text))
    lesson.append(summary([f"{t}: " + ", ".join(f"[[{r[0]}]]" for r in rows[:6]) + "." for t, rows in groups]))
    def other(idx, key, n=3):
        pool = [w for j, w in enumerate(words) if j != idx and w[key] != words[idx][key]]
        return [w[key] for w in rng.sample(pool, n)]
    P, Q = [], []
    for i, (en, ar, ex) in enumerate(words):
        P.append(mcq(f'Apa arti "{en}"?', [ar] + other(i, 1), 0, f"{en} = {ar}."))
        P.append(mcq(f'Kata Inggris untuk "{ar}" adalah...', [en] + other(i, 0), 0, f"{ar} = {en}."))
        if ex:
            pat = _re.compile(r"\b" + _re.escape(en) + r"\b", _re.I)
            if pat.search(ex) and not any(ch.isdigit() for ch in ex):
                P.append(fill(f'Isi dengan kata Inggris untuk "{ar}":', pat.sub("___", ex, count=1), [en.lower() if en.islower() else en, en.lower()], " ".join(w[0] + (" " + " ".join("_" * (len(w) - 1)) if len(w) > 1 else "") for w in en.split()), f"{ar} = {en}."))
    ls = rng.sample(range(len(words)), min(14, len(words)))
    for i in ls:
        en = words[i][0]
        P.append(listen("Dengarkan. Kata mana yang kamu dengar?", en, [en] + other(i, 0), 0, f"Kata yang diucapkan: {en}."))
    dsent = [(w[2], f'mengandung kata "{w[1]}"') for w in words if w[2] and not any(ch.isdigit() for ch in w[2]) and len(w[2].split()) >= 3]
    P += dictate(rng.sample(dsent, 6))
    qs = rng.sample(range(len(words)), min(14, len(words)))
    for k, i in enumerate(qs):
        en, ar, ex = words[i]
        if k % 3 == 0:
            Q.append(mcq(f'Kata mana yang artinya "{ar}"?', [en] + other(i, 0), 0, f"{ar} = {en}."))
        elif k % 3 == 1:
            Q.append(mcq(f'Arti kata "{en}" adalah...', [ar] + other(i, 1), 0, f"{en} = {ar}."))
        else:
            Q.append(listen("Dengarkan. Apa artinya?", en, [ar] + other(i, 1), 0, f"{en} = {ar}."))
    return mkunit(id, goals, lesson, P, Q)


def seq(items, exp, q="Susun kalimat-kalimat berikut menjadi paragraf yang runtut."):
    return dict(type="seq", q=q, items=items, exp=exp)

def spot(items, idx, exp, q="Ketuk kalimat yang mengandung kesalahan."):
    return dict(type="spot", q=q, items=items, answer=idx, exp=exp)

def cloze(marked, exp, q="Dengarkan, lalu isi kata yang hilang."):
    """marked: kalimat dengan kata hilang ditulis {kata} atau {kata|alternatif}."""
    answers = [m.split("|") for m in _re.findall(r"\{([^}]*)\}", marked)]
    text = _re.sub(r"\{[^}]*\}", "___", marked)
    say = _re.sub(r"\{([^|}]*)(?:\|[^}]*)?\}", r"\1", marked)
    return dict(type="cloze", q=q, say=say, text=text, answers=answers, exp=exp)
