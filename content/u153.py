from ub import *
UNIT = mkunit("u153",
 ["menemukan kesalahan **preposisi, kata hubung, kata ganti, dan tanda baca**",
  "memeriksa **perbandingan, pasif, dan present perfect**",
  "mengenali kesalahan **kata benda tak terhitung** dan **kata sifat/keterangan**",
  "mengedit paragraf pendek secara mandiri"],
 [intro("Latihan ini lebih sulit: kesalahannya ada pada **preposisi, kata hubung, kata ganti, perbandingan, pasif, present perfect**, dan tanda baca. Ketuk satu kalimat yang salah di setiap paragraf."),
  gram("1. Kesalahan yang sering muncul",
   table=[["Jenis", "Salah → Benar"],
          ["Preposisi", "[[depend of]] → [[depend on]]; [[good in]] → [[good at]]"],
          ["Kata hubung", "[[Although he was tired, but he worked.]] → buang but"],
          ["Kata ganti", "[[Me and her went.]] → [[She and I went.]]"],
          ["Perbandingan", "[[more taller]] → [[taller]]; [[the most best]] → [[the best]]"],
          ["Pasif", "[[The cake was ate.]] → [[was eaten]]"],
          ["Present perfect", "[[I have went]] → [[I have gone]]"],
          ["Tak terhitung", "[[many informations]] → [[a lot of information]]"],
          ["Sifat/keterangan", "[[He runs quick.]] → [[quickly]]"]]),
  warn("Satu kalimat saja yang salah", text="Hanya satu kalimat yang mengandung kesalahan. Jika kamu menemukan dua yang tampak janggal, periksa lagi mana yang benar-benar melanggar aturan."),
  summary(["Preposisi tetap: depend on, good at.", "Although tanpa but.", "Perbandingan tanpa more + -er.", "Pasif memakai V3.", "Informasi tak terhitung."])],
 [], [])
sets = [
 (["The result depends of the weather.", "We will check it tomorrow.", "If it rains, we stay home.", "The weather report says it will be sunny."], 0, "depend on."),
 (["Although it was raining, we played outside.", "We got wet.", "But we had a lot of fun.", "Our mother was angry, though."], 2, "Kalimat ini sebenarnya wajar; kesalahan lain? — lihat catatan."),
]
sets = [
 (["The result depends of the weather.", "We will check it tomorrow.", "If it rains, we will stay home.", "The report says it will be sunny."], 0, "depends on."),
 (["Rani is good in maths.", "She always gets high marks.", "Her teacher praises her.", "She helps her friends."], 0, "good at."),
 (["Although he was tired, but he finished the work.", "His boss was happy.", "He went home at six.", "He slept early."], 0, "Although tanpa but."),
 (["Me and Tom went to the cinema.", "We watched a funny film.", "We laughed a lot.", "Then we had dinner."], 0, "Tom and I."),
 (["This bag is more cheaper than that one.", "I like its colour.", "It is also lighter.", "I will buy it."], 0, "cheaper."),
 (["She is the most best student in the class.", "She studies every day.", "Her friends admire her.", "She wins many prizes."], 0, "the best."),
 (["The cake was ate by the children.", "It was delicious.", "Nothing was left.", "Their mother baked another one."], 0, "was eaten."),
 (["I have went to Bali twice.", "I love the beaches.", "I want to go again.", "My friends want to come with me."], 0, "have been/gone."),
 (["He gave me many informations.", "They were very useful.", "I wrote them down.", "I thanked him."], 0, "a lot of information."),
 (["The boy runs quick.", "He wins every race.", "His coach is proud of him.", "He trains hard."], 0, "quickly."),
 (["If I will see him, I will tell him.", "He is my classmate.", "We sit in the same row.", "We often talk."], 0, "If I see him."),
 (["She has lived here since five years.", "She likes the town.", "Her neighbours are kind.", "She wants to stay."], 0, "for five years."),
 (["The books on the table is mine.", "The pens are Dina's.", "The bag belongs to Tom.", "Please do not move them."], 0, "are mine."),
 (["I am looking forward to meet you.", "Your email was very kind.", "I hope we can talk soon.", "Thank you again."], 0, "to meeting."),
 (["My teacher suggested me to read more.", "I read a story every night.", "My English is improving.", "I feel more confident."], 0, "suggested that I read / suggested reading."),
 (["He is interested on music.", "He plays the guitar.", "He sings at school events.", "Everyone enjoys his songs."], 0, "interested in."),
 (["Everyone have finished their work.", "Please check again.", "Take your time.", "Ask me if you need help."], 0, "Everyone has finished."),
 (["We discussed about the plan.", "Everyone agreed.", "The meeting ended at five.", "We left the room."], 0, "discussed the plan."),
 (["Its a nice day today.", "The sun is shining.", "Let's go to the park.", "We can have a picnic."], 0, "It's."),
 (["He asked me where did I live.", "I told him my address.", "He wrote it down.", "He thanked me."], 0, "where I lived."),
]
import random
rng = random.Random(153)
out = []
for items, a, e in sets:
    idx = list(range(len(items)))
    rng.shuffle(idx)
    out.append(spot([items[k] for k in idx], idx.index(a), e))
UNIT["practice"] = out
UNIT["quiz"] = out[-8:]
