from qk import mk
R4 = dict(practice=mk([
 ("Mana yang bukan tempat umum?","pocket","hospital","station","market","odd."),
 ("Mana yang bukan arah?","market","left","right","straight","odd."),
 ("Mana yang bukan transportasi?","bridge","bus","train","taxi","odd."),
 ("Mana yang bukan penunjuk letak?","notebook","behind","next to","opposite","odd."),
 ("Situasi: tersesat, kamu bertanya:","Excuse me, where is the station?","Station where you?","Where station excuse?","I lost station.","situation."),
 ("Situasi: menjelaskan arah ke bank:","Go straight and turn right.","Straight go right and turn.","Going straight, turned right.","Go straight turning right.","situation."),
 ("Lengkapi: \"The hospital is ___ the bank.\" (di seberang)","opposite","behind","between","next","complete."),
 ("Lengkapi: \"Walk ___ the street.\" (menyusuri)","along","at","to","by","complete."),
 ("Lengkapi: \"Turn left ___ the traffic light.\"","at","in","to","by","complete."),
 ("Lengkapi: \"Is it far ___ here?\"","from","at","in","on","complete."),
 ("Lengkapi: \"It's ___ the corner.\"","on","in","at the","by","complete."),
 ("Lengkapi: \"There ___ a post office near here.\"","is","are","am","be","complete."),
]), quiz=mk([
 ("Antonim \"near\":","far","close","next","beside","ant."),
 ("Antonim \"left\":","right","straight","back","front","ant."),
 ("Antonim \"in front of\":","behind","beside","opposite","near","ant."),
 ("Antonim \"enter\":","exit","arrive","stay","cross","ant."),
 ("Antonim \"arrive\":","leave","come","stay","return","ant."),
 ("Sinonim \"street\":","road","bridge","alley","river","syn."),
 ("Antonim \"north\":","south","east","west","center","ant."),
 ("Antonim \"east\":","west","north","south","center","ant."),
]))
