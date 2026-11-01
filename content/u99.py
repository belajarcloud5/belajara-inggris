import random
from ub import *
import u92, u93, u94, u95, u96, u97, u98
UNIT = mkunit("u99",
 ["mengulang semua materi pelafalan: **vokal, konsonan, akhiran, tekanan, ejaan, irama, dan intonasi**",
  "menjawab soal campuran **mendengar** dan **memilih bunyi**",
  "menulis kalimat dari **dikte** dengan bunyi yang mirip",
  "mengetahui **langkah berlatih** pelafalan sehari-hari"],
 [intro("Unit ini mengulang seluruh modul pelafalan. Kerjakan latihan dan kuis, lalu ulangi unit sebelumnya untuk bagian yang masih sulit."),
  gram("Peta ringkas modul pelafalan",
   table=[["Unit", "Isi utama", "Contoh"],
          ["92 Vokal", "pendek dan panjang, diftong", "[[ship]] – [[sheep]], [[bad]] – [[bed]]"],
          ["93 Konsonan", "th, v/f, r/l, sh/ch, ng", "[[think]], [[very]], [[right]], [[ship]]"],
          ["94 Akhiran", "-s: /s/ /z/ /ɪz/; -ed: /t/ /d/ /ɪd/", "[[cats]], [[dogs]], [[watches]]; [[worked]], [[played]], [[wanted]]"],
          ["95 Tekanan kata", "suku kata yang ditekan", "[[TEAcher]], [[beGIN]], [[eduCAtion]]"],
          ["96 Ejaan", "huruf diam, -ough, c/g lunak", "[[knife]], [[through]], [[city]]"],
          ["97 Irama", "kata isi, kata fungsi, schwa", "[[I WANT to GO to the MARket]]"],
          ["98 Intonasi", "nada naik/turun, linking", "[[Do you live here?]] ↗, [[pick it up]]"]]),
  tip("Rutinitas 10 menit sehari", text="1) Dengarkan 5 kata dengan 🔊 lalu tirukan. 2) Baca satu paragraf keras-keras sambil menekan kata isi. 3) Rekam dirimu 30 detik dan dengarkan kembali. Konsistensi mengalahkan durasi."),
  summary(["Bunyi: vokal pendek/panjang dan konsonan sulit.", "Akhiran: /s/ /z/ /ɪz/ dan /t/ /d/ /ɪd/.", "Tekanan kata, irama kalimat, dan nada.", "Berlatih sedikit tetapi rutin."])],
 [], [])
rng = random.Random(99)
def pool(u, kinds=("mcq", "listen")):
    return [q for q in u.UNIT["practice"] if q["type"] in kinds]
P = []
for u in (u92, u93, u94, u95, u96, u97, u98):
    P += rng.sample(pool(u), 6)
P += dictate([("The boy thinks the ship is very big.", "Anak itu mengira kapalnya sangat besar."), ("She watched the sheep and washed the chair.", "Dia menonton domba dan mencuci kursi."),
              ("I know the teacher wanted to begin.", "Aku tahu gurunya ingin memulai."), ("Please pick it up and turn it off.", "Tolong ambil itu dan matikan."),
              ("My brother bought enough bread yesterday.", "Kakakku membeli cukup roti kemarin."), ("Did you listen to the radio tonight?", "Apakah kamu mendengarkan radio malam ini?")])
Q = []
for u in (u92, u93, u94, u95, u96, u97, u98):
    Q += rng.sample(u.UNIT["quiz"], 2)
UNIT["practice"] = P
UNIT["quiz"] = Q
