from qk import mk
R4 = dict(practice=mk([
 ("Mana yang bukan sapaan?","Banana","Hello","Hi","Good morning","odd."),
 ("Mana yang bukan perkenalan diri?","See you later.","My name is Ali.","I'm Dina.","Let me introduce myself.","odd."),
 ("Mana yang dipakai saat berpisah?","Goodbye.","Welcome.","Nice to meet you.","Good morning.","parting."),
 ("Situasi: kamu bertemu teman baru. Kamu bilang...","Nice to meet you.","See you later.","Goodbye.","Good night.","situation."),
 ("Situasi: kamu menginjak kaki orang. Kamu bilang...","I'm sorry.","You're welcome.","Good morning.","Nice to meet you.","situation."),
 ("Situasi: seseorang membantumu. Kamu bilang...","Thank you.","Excuse me.","Good night.","How old are you?","situation."),
 ("Situasi: ingin lewat di tengah kerumunan. Kamu bilang...","Excuse me.","Thank you.","Goodbye.","Welcome.","situation."),
 ("Lengkapi: \"Nice to ___ you.\"","meet","see you","met","meets","complete."),
 ("Lengkapi: \"What ___ your name?\"","is","are","am","do","complete."),
 ("Lengkapi: \"How ___ you?\"","are","is","am","do","complete."),
 ("Lengkapi: \"I ___ from Indonesia.\"","am","is","are","be","complete."),
 ("Lengkapi: \"She ___ my friend.\"","is","am","are","be","complete."),
]), quiz=mk([
 ("Sinonim \"hello\":","hi","bye","sorry","please","syn."),
 ("Antonim \"hello\" (berpisah):","goodbye","welcome","thanks","please","ant."),
 ("Antonim \"morning\":","evening","noon","sunrise","breakfast","ant."),
 ("Antonim \"student\" (peran di kelas):","teacher","friend","brother","child","ant."),
 ("Antonim \"yes\":","no","maybe","sure","okay","ant."),
 ("Antonim \"old\" (benda):","new","big","long","slow","ant."),
 ("Antonim \"big\":","small","tall","long","wide","ant."),
 ("Antonim \"happy\":","sad","angry","tired","hungry","ant."),
]))
