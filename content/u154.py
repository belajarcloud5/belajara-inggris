from ub import *
UNIT = mkunit("u154",
 ["memahami kata lewat **definisi sederhana** dalam bahasa Inggris",
  "memasangkan **kata dan definisinya**",
  "menebak kata dari **petunjuk dalam bahasa Inggris**",
  "mulai **berpikir dalam bahasa Inggris**, bukan lewat terjemahan"],
 [intro("Kamus bahasa Inggris menjelaskan kata dengan kata-kata sederhana. Membaca definisi seperti ini melatihmu **berpikir dalam bahasa Inggris** dan membantu bila terjemahan tidak tersedia. Pasangkan kata dengan definisinya, lalu jawab pertanyaan *Which word means ...?*"),
  gram("1. Pola definisi sederhana",
   table=[["Pola", "Contoh"],
          ["a/an + kata benda umum + yang ...", "[[A teacher is a person who teaches students.]]"],
          ["to + kata kerja = melakukan ...", "[[To borrow means to take something and give it back later.]]"],
          ["kata sifat = sifat ...", "[[Hungry means you want to eat.]]"],
          ["tempat = tempat untuk ...", "[[A library is a place where you can read and borrow books.]]"],
          ["kebalikan", "[[Cheap is the opposite of expensive.]]"]]),
  tip("Cari kata kunci dalam definisi", text="Dalam definisi, kata benda umum (person, place, thing) dan kata kerja kunci memberi petunjuk. *A place where you sleep at night* → bedroom."),
  summary(["Definisi: a ... is a person/place/thing that ...", "To ... means to ...", "Opposite of ... = kebalikan.", "Pakai kata kunci untuk menebak."])],
 [], [])
sets = [
 [("teacher", "a person who teaches students"), ("doctor", "a person who helps sick people"), ("farmer", "a person who grows food"), ("driver", "a person who drives a car or bus")],
 [("library", "a place where you can read and borrow books"), ("kitchen", "a room where you cook food"), ("hospital", "a place where sick people get help"), ("bank", "a place where people keep money")],
 [("hungry", "wanting to eat"), ("tired", "needing to sleep or rest"), ("angry", "feeling very upset with someone"), ("happy", "feeling good and glad")],
 [("borrow", "to take something and give it back later"), ("lend", "to give something to someone for a short time"), ("buy", "to get something by paying money"), ("sell", "to give something to someone for money")],
 [("early", "before the usual time"), ("late", "after the usual time"), ("always", "every time"), ("never", "not at any time")],
 [("umbrella", "something you carry to stay dry in the rain"), ("map", "a drawing that shows where places are"), ("key", "something you use to open a door"), ("wallet", "a small case for money and cards")],
 [("breakfast", "the first meal of the day"), ("lunch", "the meal in the middle of the day"), ("dinner", "the main meal in the evening"), ("snack", "a small amount of food between meals")],
 [("cheap", "not costing much money"), ("expensive", "costing a lot of money"), ("free", "costing no money"), ("rich", "having a lot of money")],
 [("quiet", "making very little noise"), ("noisy", "making a lot of noise"), ("crowded", "full of people"), ("empty", "with nothing or no one inside")],
 [("ancient", "very old, from long ago"), ("modern", "new and up to date"), ("popular", "liked by many people"), ("famous", "known by many people")],
 [("passport", "a document you need to travel to another country"), ("ticket", "a piece of paper that lets you travel or enter a place"), ("luggage", "the bags you take on a trip"), ("souvenir", "something you buy to remember a place")],
 [("whisper", "to speak very quietly"), ("shout", "to speak very loudly"), ("laugh", "to make sounds because something is funny"), ("cry", "to have tears because you are sad")],
 [("improve", "to become better"), ("decrease", "to become smaller in amount"), ("increase", "to become bigger in amount"), ("avoid", "to stay away from something")],
 [("honest", "always telling the truth"), ("polite", "having good manners"), ("generous", "happy to give things to others"), ("shy", "nervous with people you do not know")],
 [("schedule", "a plan that shows when things will happen"), ("deadline", "the last time you can finish something"), ("meeting", "an event where people talk about work"), ("agenda", "a list of things to talk about in a meeting")],
 [("environment", "the natural world around us"), ("pollution", "dirty or harmful things in air, water, or land"), ("recycle", "to use materials again"), ("waste", "things we throw away")],
]
P = [dict(type="match", q="Pasangkan kata dengan definisinya.", pairs=[list(p) for p in s], exp="Definisi: " + "; ".join(f"{a} = {b}" for a, b in s) + ".") for s in sets]
# soal pilihan ganda "Which word means ..."
import random
rng = random.Random(154)
allp = [p for s in sets for p in s]
M = []
for s in sets:
    for w, d in s:
        others = [x[0] for x in s if x[0] != w]
        M.append(mcq(f'Which word means: "{d}"?', [w] + others[:3], 0, f"{w}: {d}."))
rng.shuffle(M)
UNIT["practice"] = P + M[:40]
UNIT["quiz"] = M[40:48] + P[-4:]
