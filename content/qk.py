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


def mkd(rows):
    """Soal dikte. rows: (kalimat, terjemahan). Pemain mendengar kalimat lalu mengetiknya."""
    return [dict(type="dictate", q="Dengarkan, lalu ketik kalimat yang kamu dengar.", say=en, answer=en, exp=f"Kalimatnya: {en} Artinya: {idn}") for en, idn in rows]


def mko(rows):
    """Susun kalimat. rows: (terjemahan, kalimat Inggris, kata pengecoh dipisah spasi atau '', kalimat alternatif dipisah ' // ' atau '')."""
    from helpers import order
    out = []
    for idt, en, extra, alts in rows:
        q = order(f'Susun kalimat: "{idt}"', en, f"Urutan yang benar: {en}", extra.split() or None)
        if alts:
            q["alts"] = alts.split(" // ")
        out.append(q)
    return out


def mkr(rows):
    """Percakapan, pemain mengetik balasan. rows: (situasi, giliran 'Nama: teks >> Nama: teks' (terakhir = lawan bicara),
    maksud balasan, jawaban contoh dipisah ' // ', kata kunci 'a,b;c,d' atau '-')."""
    out = []
    for scene, turns, intent, answers, keys in rows:
        tl = [[x.split(": ", 1)[0], x.split(": ", 1)[1]] for x in turns.split(" >> ")]
        ans = answers.split(" // ")
        q = dict(type="reply", q=tl[-1][1], scene=scene, turns=tl, id=intent, answers=ans,
                 exp="Contoh balasan: " + "  atau  ".join(ans[:3]))
        if keys != "-":
            q["keys"] = [g.split(",") for g in keys.split(";")]
        out.append(q)
    return out
