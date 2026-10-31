from helpers import mcq

def mk(rows):
    """rows: (pertanyaan, benar, salah1, salah2, salah3, penjelasan). Jawaban benar di indeks 0 (diacak di frontend)."""
    return [mcq(q, [r, a, b, c], 0, e) for q, r, a, b, c, e in rows]
