from helpers import mcq
TFN = ['True', 'False', 'Not Given']
def tfn(text, rows):
    """rows: (pernyataan, jawaban 'T'/'F'/'N', penjelasan). Opsi jawaban benar di indeks 0 (diacak di frontend)."""
    out = []
    for st, a, exp in rows:
        right = {'T': 'True', 'F': 'False', 'N': 'Not Given'}[a]
        opts = [right] + [x for x in TFN if x != right]
        out.append(mcq(f'Teks: "{text}"  ·  Pernyataan: "{st}"  ·  Jawabannya True, False, atau Not Given?', opts, 0, exp))
    return out
def ask(text, rows):
    """rows: (pertanyaan, benar, s1, s2, s3, exp)."""
    return [mcq(f'Teks: "{text}"  ·  {q}', [r, a, b, c], 0, e) for q, r, a, b, c, e in rows]
