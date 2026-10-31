from qk import mk
R3 = dict(practice=mk([
 ("Terjemahan \"Kami mengundang Anda ke acara kami\":","We invite you to our event.","We inviting you at event our.","We invite you in our event.","Us invite you our event.","tr."),
 ("Terjemahan \"Rapat dimulai pukul sembilan\":","The meeting starts at nine.","The meeting start on nine.","Meeting starts in nine.","The meeting is start at nine.","tr."),
 ("Terjemahan \"Mohon datang tepat waktu\":","Please come on time.","Please coming in time.","Please comes on time.","Please come at time on.","tr."),
 ("Terjemahan \"Acara akan diadakan di aula\":","The event will be held in the hall.","The event will hold in hall.","The event will be hold at hall.","Event will held hall.","tr."),
 ("Terjemahan \"Pesta ulang tahun saya hari Sabtu\":","My birthday party is on Saturday.","My birthday party is at Saturday.","Birthday my party in Saturday.","My party birthday are Saturday.","tr."),
 ("Terjemahan \"Semua siswa harus hadir\":","All students must attend.","All students must to attend.","All student must attending.","All students musts attend.","tr."),
 ("Perbaiki: \"The party will be hold on Sunday.\"","The party will be held on Sunday.","The party will held Sunday.","The party will hold Sunday.","The party be hold Sunday.","fix."),
 ("Perbaiki: \"Please be come at 8.\"","Please come at 8.","Please be coming at 8.","Please comes at 8.","Please to come at 8.","fix."),
 ("Perbaiki: \"We are invite you.\"","We invite you.","We are inviting you's.","We invites you.","We inviting you.","fix."),
 ("Perbaiki: \"The meeting cancel.\"","The meeting is cancelled.","The meeting cancel is.","The meeting has cancel.","The meeting cancelling.","fix."),
 ("Dialog: \"Can you come to my party?\" – \"___\"","I'd love to, thank you.","I love to you.","Thank to you love.","I come you party.","dialog."),
 ("Dialog: \"When is the meeting?\" – \"___\"","It's at ten.","It's on ten.","It's in ten o'clock at.","It's ten at.","dialog."),
]), quiz=mk([
 ("\"Rapat\":","meeting","party","class","trip","word."),
 ("\"Lomba\":","competition","party","class","trip","word."),
 ("\"Pesta\":","party","meeting","class","exam","word."),
 ("\"Acara\":","event","exam","class","trip","word."),
 ("\"Hadir\":","attend","absent","leave","skip","word."),
 ("\"Tidak hadir\":","absent","present","attend","join","word."),
 ("\"Panitia\":","committee","audience","winner","judge","word."),
 ("\"Peserta\":","participant","committee","judge","winner","word."),
]))
