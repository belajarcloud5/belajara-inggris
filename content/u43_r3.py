from qk import mk
R3 = dict(practice=mk([
 ("Terjemahan \"Pencuri itu ditangkap oleh polisi\":","The thief was arrested by the police.","The thief arrested by police.","The thief is arrest by police.","The thief was arrest police.","tr."),
 ("Terjemahan \"Jembatan itu akan diperbaiki bulan depan\":","The bridge will be repaired next month.","The bridge will repaired next month.","The bridge will be repair next month.","The bridge is will repaired.","tr."),
 ("Terjemahan \"Dia berkata bahwa dia sedang sibuk\":","She said that she was busy.","She said she is busy then.","She says that she was busy.","She said that she busy.","tr."),
 ("Terjemahan \"Guru menyuruh kami membuka buku\":","The teacher told us to open our books.","The teacher told us open books.","The teacher told to us opening books.","The teacher says us to open.","tr."),
 ("Terjemahan \"Ibu bertanya apakah saya sudah makan\":","Mother asked if I had eaten.","Mother asked if I have eaten.","Mother asked did I eat.","Mother asked that I eaten.","tr."),
 ("Terjemahan \"Pekerjaan itu sudah diselesaikan\":","The work has been finished.","The work has finished.","The work was been finish.","The work have been finished.","tr."),
 ("Perbaiki: \"The cake is eating by children.\"","The cake is being eaten by children.","The cake is eating by children.","The cake eaten by children is.","The cake is eat by children.","fix."),
 ("Perbaiki: \"He said that he will come.\" (laporan lampau)","He said that he would come.","He said that he will come.","He says that he would came.","He said that he come.","fix."),
 ("Perbaiki: \"She asked where did I live.\"","She asked where I lived.","She asked where did I lived.","She asked where I live did.","She asked where do I live.","fix."),
 ("Perbaiki: \"The letters has been sent.\"","The letters have been sent.","The letters has been send.","The letters have been sending.","The letters was been sent.","fix."),
 ("Dialog: \"Who built this temple?\" – \"___\"","It was built by King Sanjaya.","It built by King Sanjaya.","It is build by King.","King Sanjaya was build.","dialog."),
 ("Dialog: \"What did he say?\" – \"___\"","He said he was tired.","He said he is tired now.","He says he tired.","He said tired he was.","dialog."),
]), quiz=mk([
 ("\"Dilaporkan\":","reported","reporter","reporting","reports","word."),
 ("\"Diperbaiki\":","repaired","repeated","replaced","replied","word."),
 ("\"Ditemukan\":","found","fund","fond","fount","word."),
 ("\"Dibangun\":","built","build","builder","building","word."),
 ("\"Ditulis\":","written","wrote","writer","writing","word."),
 ("\"Dikirim\":","sent","send","sand","scent","word."),
 ("\"Dicuri\":","stolen","stole","steal","steel","word."),
 ("\"Diumumkan\":","announced","announcer","announce","annual","word."),
]))
