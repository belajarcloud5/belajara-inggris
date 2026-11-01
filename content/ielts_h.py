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

from helpers import fill as _fill
def rstory(title, focus, text, idt, comp, tfn_rows, fills):
    """Bacaan IELTS: comp=[(q,benar,s1,s2,s3,exp)], tfn_rows=[(pernyataan,'T/F/N',exp)], fills=[(terjemahan,kalimat ___,jawaban,exp)]."""
    qs = [mcq(q, [r, a, b, c], 0, e) for q, r, a, b, c, e in comp]
    for st, a, exp in tfn_rows:
        right = {'T': 'True', 'F': 'False', 'N': 'Not Given'}[a]
        qs.append(mcq(f'Pernyataan: "{st}"  ·  True, False, atau Not Given?', [right] + [x for x in TFN if x != right], 0, exp))
    for idf, q, a, exp in fills:
        ans = a.split("/")
        hint = " ".join(w[0] + (" " + " ".join("_" * (len(w) - 1)) if len(w) > 1 else "") for w in ans[0].split())
        qs.append(_fill(idf, q, ans, hint, exp))
    return dict(title=title, focus=focus, text=text, id=idt, qs=qs)
