from qk import mk
R3 = dict(practice=mk([
 ("Terjemahan \"Menurut saya, ini ide bagus\":","In my opinion, this is a good idea.","In my opinion, this good idea.","On my opinion this is idea good.","I opinion this is good idea.","tr."),
 ("Terjemahan \"Saya setuju dengan kamu\":","I agree with you.","I am agree with you.","I agree to you.","I agreeing you.","tr."),
 ("Terjemahan \"Saya tidak setuju karena mahal\":","I disagree because it is expensive.","I not agree because expensive.","I don't disagree because mahal.","I disagree because expensively.","tr."),
 ("Terjemahan \"Bagaimana pendapatmu?\":","What do you think?","How is your think?","What you thinking?","How do you opinion?","tr."),
 ("Terjemahan \"Itu poin yang bagus\":","That's a good point.","That good point is.","That's good a point.","That a good points.","tr."),
 ("Terjemahan \"Saya pikir sekolah harus lebih lama\":","I think school should be longer.","I think school must longer.","I thinking school should longer.","I think that school is should long.","tr."),
 ("Perbaiki: \"I am agree with you.\"","I agree with you.","I agree to you.","I am agreeing with you.","I agrees with you.","fix."),
 ("Perbaiki: \"In my opinion, I think it is good.\"","In my opinion, it is good.","In my opinion, I think it good.","My opinion I think good.","In opinion mine, it good.","fix."),
 ("Perbaiki: \"I think so because it is useful for.\"","I think so because it is useful.","I think so because useful for.","I think because is useful for it.","I thinks so because it useful.","fix."),
 ("Perbaiki: \"I don't agree to him.\"","I don't agree with him.","I don't agree at him.","I not agree with him.","I doesn't agree him.","fix."),
 ("Dialog: \"Do you agree?\" – \"___\"","Yes, I totally agree.","Yes, I agrees.","Yes, I am agree.","Yes, agreeing.","dialog."),
 ("Dialog: \"Why do you think so?\" – \"___\"","Because it is helpful.","Because helpfully.","Because of help is.","Because helping.","dialog."),
]), quiz=mk([
 ("\"Pendapat\":","opinion","opening","option","opposite","word."),
 ("\"Alasan\":","reason","season","reasoned","raising","word."),
 ("\"Setuju\":","agree","argue","angry","arrive","word."),
 ("\"Menentang\":","oppose","open","order","offer","word."),
 ("\"Berdebat\":","debate","decide","delay","depend","word."),
 ("\"Keputusan\":","decision","division","decoration","description","word."),
 ("\"Solusi\":","solution","situation","station","section","word."),
 ("\"Masalah\":","problem","project","program","promise","word."),
]))
