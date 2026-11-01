"""Pembangun unit baru (modul pelafalan, kosakata, TOEIC)."""
import random
from helpers import mcq, fill, order, match, listen
from qk import mk, mkf, mko, mkd

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
