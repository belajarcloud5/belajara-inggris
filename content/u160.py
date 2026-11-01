from ub import *
from ielts_h import ask, rstory
UNIT = mkunit("u160",
 ["menemukan **gagasan utama** teks akademik",
  "menjawab soal **detail, inferensi, dan referensi kata ganti**",
  "memahami **kosakata dalam konteks**",
  "membaca teks akademik dalam **waktu sekitar 11 menit per teks**"],
 [intro("Bagian **Reading** terdiri dari lima teks akademik, masing-masing dengan sekitar sepuluh soal. Waktu sangat terbatas, jadi kamu harus **membaca selektif**. Kenali jenis soal dan tahu di mana mencari jawabannya."),
  gram("1. Jenis soal Reading",
   table=[["Jenis", "Contoh soal", "Cara menjawab"],
          ["Gagasan utama", "[[What is the main topic of the passage?]]", "baca kalimat pertama dan terakhir paragraf"],
          ["Detail", "[[According to the passage, ...]]", "scan kata kunci, baca kalimat sekitarnya"],
          ["Referensi", "[[The word 'it' in line 5 refers to ...]]", "baca kalimat sebelumnya"],
          ["Kosakata", "[[The word 'significant' is closest in meaning to ...]]", "ganti dengan opsi dalam kalimat"],
          ["NOT/EXCEPT", "[[All of the following are mentioned EXCEPT ...]]", "coret opsi yang ada di teks"],
          ["Inferensi", "[[It can be inferred that ...]]", "simpulkan dari fakta, jangan menebak di luar teks"]]),
  gram("2. Strategi waktu",
   table=[["Langkah", "Isi"],
          ["1", "Baca sekilas judul dan kalimat pertama tiap paragraf (1 menit)"],
          ["2", "Baca soal, lalu scan jawaban"],
          ["3", "Jangan menghabiskan lebih dari 1 menit per soal"],
          ["4", "Sisakan 2 menit untuk soal yang ditandai"]]),
  tip("Pelajari kata penghubung teks", text="Kata seperti *however*, *for example*, *in contrast*, dan *therefore* membantu menemukan gagasan utama, contoh, dan kesimpulan."),
  summary(["Gagasan utama: kalimat pertama paragraf.", "Detail: scan kata kunci.", "NOT: coret yang ada di teks.", "Inferensi: simpulkan dari fakta di teks."])],
 [], [])
A = "Coral reefs are among the most diverse ecosystems on Earth, even though they cover less than one percent of the ocean floor. They protect coasts from storms, provide food for millions of people, and support a quarter of all marine species. However, rising ocean temperatures cause corals to lose the algae that give them colour and energy. This process, called bleaching, can kill an entire reef if the heat lasts too long. Scientists therefore urge governments to reduce carbon emissions, which warm the oceans."
B = "The printing press, invented in the fifteenth century, transformed how information spread. Before it, books were copied by hand, which made them rare and expensive. After the press appeared, books became cheaper, and literacy rates rose steadily. As a result, new ideas about science and religion travelled quickly across Europe. Some historians argue that this change played an important role in the Renaissance."
P = ask(A, [
 ("What is the main idea of the passage?", "Coral reefs are valuable but threatened by warming oceans", "Coral reefs cover most of the ocean", "Storms damage coasts every year", "Scientists study algae", "Gagasan utama."),
 ("According to the passage, what causes bleaching?", "Rising ocean temperatures", "Storms", "Fishing", "Lack of food", "Suhu laut naik."),
 ("The word 'urge' is closest in meaning to...", "strongly encourage", "ignore these days", "forbid", "warn against at that time", "Urge = mendesak."),
 ("All of the following are mentioned as benefits of reefs EXCEPT...", "providing electricity", "protecting coasts", "providing food", "supporting marine species", "Listrik tidak disebut."),
 ("The word 'This process' in the passage refers to...", "losing algae", "protecting coasts", "providing food", "reducing emissions", "Bleaching."),
 ("What can be inferred about carbon emissions?", "They contribute to warmer oceans", "They help coral grow these days", "They cool the oceans these days", "They are not harmful this week", "Menghangatkan laut."),
]) + ask(B, [
 ("What is the main topic of the passage?", "The effect of the printing press on information", "The history of books in Asia at the moment", "The invention of paper in general", "The decline of literacy at that time", "Dampak mesin cetak."),
 ("According to the passage, why were books expensive before the press?", "They were copied by hand", "Paper was rare at the moment", "Few people could read this week", "Taxes were high at the moment", "Disalin tangan."),
 ("The word 'rare' is closest in meaning to...", "uncommon", "heavy", "beautiful", "famous", "Rare = langka."),
 ("What happened to literacy rates after the press?", "They rose", "They fell", "They stayed the same", "They disappeared", "Meningkat."),
 ("What can be inferred about the Renaissance?", "New ideas spread more easily during it", "It happened before the press at the moment", "It ended literacy in general", "It was only in Asia at that time", "Gagasan baru menyebar."),
])
Q = P[-6:] + P[:2]
UNIT["practice"] = P
UNIT["quiz"] = Q
READ = [
 rstory("Coral Reefs Under Threat", "TOEFL Reading", A,
  "Terumbu karang termasuk ekosistem paling beragam di Bumi, meskipun menutupi kurang dari satu persen dasar laut. Terumbu melindungi pantai dari badai, menyediakan makanan bagi jutaan orang, dan menopang seperempat spesies laut. Namun, kenaikan suhu laut menyebabkan karang kehilangan alga yang memberi mereka warna dan energi. Proses ini, yang disebut pemutihan, dapat mematikan seluruh terumbu jika panas berlangsung terlalu lama. Karena itu para ilmuwan mendesak pemerintah mengurangi emisi karbon, yang menghangatkan lautan.",
  [("What is the main idea?", "Coral reefs are valuable but threatened by warming oceans", "Coral reefs cover most of the ocean", "Storms damage coasts every year", "Scientists study algae", "Gagasan utama."), ("What causes bleaching?", "Rising ocean temperatures", "Storms", "Fishing", "Lack of food", "Suhu naik."), ("What do scientists urge governments to do?", "Reduce carbon emissions", "Build bigger reefs", "Ban fishing", "Study algae", "Kurangi emisi.")], [],
  [("Terumbu menutupi kurang dari satu persen.", "Reefs cover less than one ___ of the ocean floor.", "percent", "One percent."), ("Pemutihan dapat mematikan terumbu.", "Bleaching can ___ an entire reef.", "kill", "Kill a reef.")]),
]
