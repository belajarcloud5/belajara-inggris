from helpers import mcq, fill, order

def hint_of(a):
    return " ".join(w[0] + (" " + " ".join("_" * (len(w) - 1)) if len(w) > 1 else "") for w in a.split())

def story(title, focus, text, idt, comp, mistake, pick, fills, order_row):
    """comp=(q,benar,s1,s2,s3,exp); mistake=(kalimat_salah,b1,b2,b3,exp); pick=(q,benar,s1,s2,s3,exp);
    fills=[(terjemahan, kalimat ___, jawaban, exp)]; order_row=(terjemahan, kalimat, kata_pengecoh, exp)."""
    qs = [mcq(comp[0], list(comp[1:5]), 0, comp[5]),
          mcq("Which sentence has a mistake?", list(mistake[:4]), 0, mistake[4]),
          mcq(pick[0], list(pick[1:5]), 0, pick[5])]
    for idf, q, a, exp in fills:
        qs.append(fill(idf, q, a.split("/"), hint_of(a.split("/")[0]), exp))
    idt_, en, extra, exp = order_row
    qs.append(order(f'Susun kalimat dari cerita: "{idt_}"', en, exp, extra.split() or None))
    return dict(title=title, focus=focus, text=text, id=idt, qs=qs)
