from qk import mk
R4 = dict(practice=mk([
 ("Mana yang bukan bagian rapat?","dessert","agenda","minutes","chairperson","odd."),
 ("Mana ungkapan membuka rapat?","Let's get started.","Let's go home.","That's all.","Goodbye.","odd."),
 ("Mana ungkapan menutup rapat?","Thank you all for coming.","Let's begin.","First item.","Any objections to start?","odd."),
 ("Mana ungkapan menyela sopan?","Sorry to interrupt, but...","Shut up.","Stop talking.","Wait you.","odd."),
 ("Situasi: ingin menambahkan:","May I add something?","Add I may?","I adding something.","Something add may.","situation."),
 ("Situasi: setuju dengan pembicara:","I agree with you.","I am agree you.","I agreeing with.","I agrees you.","situation."),
 ("Lengkapi: \"Who will take the ___?\" (notulen)","minutes","minute","minuting","minuted","complete."),
 ("Lengkapi: \"Let's move ___ to the next item.\"","on","in","at","by","complete."),
 ("Lengkapi: \"I'd like to ___ a point.\" (mengemukakan)","raise","rise","raising","rose","complete."),
 ("Lengkapi: \"We need to ___ a decision.\" (membuat)","make","do","take place","build","complete."),
 ("Lengkapi: \"All ___ favor, say yes.\"","in","at","on","for to","complete."),
 ("Lengkapi: \"Let's wrap ___ the meeting.\"","up","in","at","by","complete."),
]), quiz=mk([
 ("Sinonim \"propose\":","suggest","refuse","ignore","delay","syn."),
 ("Antonim \"agree\":","disagree","accept","approve","allow","ant."),
 ("Sinonim \"conclude\":","end","start","open","begin","syn."),
 ("Antonim \"approve\":","reject","accept","allow","support","ant."),
 ("Sinonim \"attendee\":","participant","speaker","boss","outsider","syn."),
 ("Antonim \"absent\":","present","away","missing","gone","ant."),
 ("Sinonim \"discuss\":","talk about","ignore","forget","skip","syn."),
 ("Antonim \"start\" (rapat):","adjourn","open","begin","launch","ant."),
]))
