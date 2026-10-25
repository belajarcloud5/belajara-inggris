# Pembuat soal ringkas. Semua soal wajib punya penjelasan (exp).
def mcq(q, options, answer, exp):
    return dict(type="mcq", q=q, options=options, answer=answer, exp=exp)

def listen(q, say, options, answer, exp):
    return dict(type="listen", q=q, say=say, options=options, answer=answer, exp=exp)

def fill(id_text, q, answers, hint, exp):
    """id_text = terjemahan/perintah (bahasa Indonesia); q memuat ___ ; answers = jawaban yang diterima."""
    return dict(type="fill", id=id_text, q=q, answers=answers, hint=hint, exp=exp)

def order(q, answer, exp, extra=None):
    d = dict(type="order", q=q, answer=answer, exp=exp)
    if extra:
        d["extra"] = extra
    return d

def match(q, pairs, exp):
    return dict(type="match", q=q, pairs=pairs, exp=exp)
