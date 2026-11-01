from ub import *
UNIT = mkunit("u159",
 ["menemukan **bagian yang salah** dalam kalimat (Written Expression)",
  "mengenali kesalahan **subjek–kata kerja, jamak, preposisi, paralel, dan kata keterangan**",
  "memakai strategi **membaca bagian bergaris bawah (A)–(D)**",
  "menjawab satu soal dalam sekitar **30 detik**"],
 [intro("Pada **Written Expression**, setiap kalimat memiliki empat bagian bergaris bawah yang ditandai (A) sampai (D). Satu bagian salah. Tugasmu memilih bagian yang salah itu. Di sini bagian bertanda ditulis dengan huruf dalam tanda kurung."),
  gram("1. Kesalahan yang paling sering diuji",
   table=[["Jenis", "Contoh salah", "Perbaikan"],
          ["Subjek–kata kerja", "[[The number of students are increasing]]", "is increasing"],
          ["Kata benda tak terhitung", "[[many informations]]", "much information"],
          ["Preposisi", "[[discuss about]], [[depend of]]", "discuss, depend on"],
          ["Paralel", "[[reading, to write, and speaking]]", "reading, writing, and speaking"],
          ["Kata keterangan", "[[drives careful]]", "carefully"],
          ["Tense/durasi", "[[for last year]]", "since last year"],
          ["Kata hubung ganda", "[[Although ..., but ...]]", "buang but"],
          ["Bentuk kata kerja", "[[did not went]]", "did not go"]]),
  tip("Cek empat bagian secara berurutan", text="Baca seluruh kalimat dulu untuk maknanya. Lalu periksa (A), (B), (C), (D) satu per satu terhadap daftar kesalahan di atas."),
  summary(["Empat bagian bertanda; satu salah.", "Cek subjek–kata kerja, jamak, preposisi, paralel, kata keterangan.", "Strategi: baca utuh, lalu periksa tiap bagian."])],
 [], [])
W = [
 ("The (A) number of students (B) are increasing (C) every year (D) in this city.", "B", "(B) are increasing", "Number → is increasing."),
 ("She (A) has been (B) working here (C) from (D) 2015.", "C", "(C) from", "Seharusnya since 2015."),
 ("(A) Despite of (B) the rain, (C) the match (D) continued.", "A", "(A) Despite of", "Despite tanpa of."),
 ("The (A) informations (B) in this report (C) are (D) very useful.", "A", "(A) informations", "Information tak terhitung."),
 ("He (A) suggested (B) me (C) to read (D) more books.", "B", "(B) me", "Suggested that I read / suggested reading."),
 ("(A) Although it (B) was raining, (C) but (D) we went out.", "C", "(C) but", "Although tanpa but."),
 ("The (A) children (B) was playing (C) in the (D) garden.", "B", "(B) was playing", "Children → were."),
 ("I (A) look forward (B) to meet (C) you (D) next week.", "B", "(B) to meet", "to meeting."),
 ("Most of the (A) students (B) in my class (C) is (D) very hardworking.", "C", "(C) is", "Most of the students → are."),
 ("She (A) is (B) more taller (C) than (D) her sister.", "B", "(B) more taller", "taller."),
 ("The teacher (A) asked us (B) to not (C) talk (D) during the test.", "B", "(B) to not", "not to talk."),
 ("He (A) drives (B) very (C) careful (D) on rainy days.", "C", "(C) careful", "carefully."),
 ("There (A) is (B) many (C) reasons (D) for this decision.", "A", "(A) is", "There are many reasons."),
 ("She (A) speaks (B) English (C) very good (D) now.", "C", "(C) very good", "very well."),
 ("The book (A) which (B) I bought (C) it (D) yesterday is interesting.", "C", "(C) it", "Tidak perlu kata ganti objek."),
 ("The (A) sooner you start, the (B) easier (C) is (D) it.", "C", "(C) is", "the easier it is."),
 ("He (A) did not (B) went (C) to school (D) yesterday.", "B", "(B) went", "did not go."),
 ("(A) During I was (B) walking, I (C) saw (D) an accident.", "A", "(A) During", "While."),
 ("My brother, (A) who (B) live (C) in Jakarta, (D) is a doctor.", "B", "(B) live", "who lives."),
 ("We (A) discussed (B) about (C) the plan (D) yesterday.", "B", "(B) about", "discuss tanpa about."),
 ("The (A) price (B) of the tickets (C) have (D) increased.", "C", "(C) have", "The price → has."),
 ("I (A) will (B) call you (C) when (D) I will arrive.", "D", "(D) I will arrive", "Klausa waktu: when I arrive."),
 ("She (A) enjoys (B) to swim (C) in the (D) morning.", "B", "(B) to swim", "enjoys swimming."),
 ("It is (A) important that he (B) arrives (C) on time (D) tomorrow.", "B", "(B) arrives", "Subjunctive: arrive."),
]
import random
rng = random.Random(159)
L = {"A": 0, "B": 1, "C": 2, "D": 3}
items = []
for sent, letter, right, exp in W:
    opts = [right]
    import re
    parts = dict(re.findall(r"\(([A-D])\)\s*([^()]*?)(?=\s*\([A-D]\)|$)", sent))
    # pilihan: empat bagian bertanda
    others = [f"({k}) {v.strip().rstrip(',.')}" if v.strip() else f"({k})" for k, v in parts.items() if k != letter]
    if len(others) < 3:
        others += ["(none)"] * (3 - len(others))
    items.append(mcq(f'Written Expression. Pilih bagian yang salah: {sent}', [right] + others[:3], 0, exp))
UNIT["practice"] = items[:16]
UNIT["quiz"] = items[16:]
