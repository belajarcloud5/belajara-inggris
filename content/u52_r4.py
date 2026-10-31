from qk import mk
R4 = dict(practice=mk([
 ("Mana kalimat membuka telepon kantor?","Good morning, how may I help you?","Who?","What?","Yes?","odd."),
 ("Mana kalimat meminta menunggu?","Please hold the line.","Hang up.","Call later.","Stop.","odd."),
 ("Mana yang bukan istilah telepon?","spoon","voicemail","dial","ring","odd."),
 ("Mana kalimat salah sambung?","I think you have the wrong number.","I think you have wrong pen.","Wrong spoon.","No number.","odd."),
 ("Situasi: meninggalkan pesan:","Could you tell him I called?","Tell he call I.","You tell called?","Telling him I call.","situation."),
 ("Situasi: sinyal buruk:","Sorry, you're breaking up.","Sorry, you're breaking cup.","Sorry, you break.","You break up is.","situation."),
 ("Lengkapi: \"May I ask who is ___?\" (menelepon)","calling","call","called","calls","complete."),
 ("Lengkapi: \"I'll put you ___ to Ms. Rina.\"","through","in","at","by","complete."),
 ("Lengkapi: \"Could you speak ___ ?\" (lebih keras)","up","off","out","in","complete."),
 ("Lengkapi: \"He is not ___ his desk.\"","at","on","in to","by","complete."),
 ("Lengkapi: \"I'll call you ___ later.\" (kembali)","back","away","off","out","complete."),
 ("Lengkapi: \"Thank you for ___ PT Maju.\" (menelepon)","calling","call","called","calls","complete."),
]), quiz=mk([
 ("Sinonim \"dial\":","call","answer","hang","drop","syn."),
 ("Antonim \"answer\" (telepon):","hang up","pick up","respond","reply","ant."),
 ("Sinonim \"message\":","note","joke","gift","game","syn."),
 ("Antonim \"incoming\":","outgoing","coming","entering","arriving","ant."),
 ("Sinonim \"available\":","free","busy","absent","away","syn."),
 ("Antonim \"available\":","unavailable","free","ready","open","ant."),
 ("Antonim \"clear\" (suara):","muffled","loud","quiet","soft","ant."),
 ("Sinonim \"inquire\":","ask","answer","refuse","forget","syn."),
]))
