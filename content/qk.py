from helpers import mcq

def mk(rows):
    """rows: (pertanyaan, benar, salah1, salah2, salah3, penjelasan). Jawaban benar di indeks 0 (diacak di frontend)."""
    return [mcq(q, [r, a, b, c], 0, e) for q, r, a, b, c, e in rows]


def mkf(rows):
    """Soal isian ketik. rows: (terjemahan, kalimat dengan ___, jawaban atau 'a/b' bila ada beberapa, penjelasan).
    Petunjuk dibuat otomatis: huruf pertama dan jumlah huruf."""
    from helpers import fill
    out = []
    for idt, q, ans, exp in rows:
        answers = ans.split("/")
        hint = " / ".join(w[0] + (" " + " ".join("_" * (len(w) - 1)) if len(w) > 1 else "") for w in answers[0].split())
        out.append(fill(idt, q, answers, hint, exp))
    return out
