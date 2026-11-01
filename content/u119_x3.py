from ub import *
import u119 as _b
text_qs = _b.text_qs
T6 = "Dear Residents, we are writing to {0} you that the water supply will be interrupted on Saturday from nine to noon. The repairs {1} necessary because of a damaged pipe. {2} you need water during this time, please use the tank near the gate. {3} We apologise for any inconvenience."
B6 = [("inform", "information", "informed", "informing", "To + kata kerja dasar."),
      ("are", "is being", "was", "being", "Subjek jamak the repairs."),
      ("If", "Although", "Unless", "Because", "If you need → permintaan."),
      ("The supply should return to normal by one o'clock.", "Pipes are made of metal.", "The tank is blue.", "I like swimming.", "Menyambung topik air.")]
T7 = "Thank you for applying for the position of sales assistant. We were {0} by your experience and would like to invite you for an interview. The interview {1} on Tuesday at ten o'clock. Please bring a copy of your resume {2} two references. {3} We look forward to meeting you."
B7 = [("impressed", "impress", "impression", "impressing", "Passive: were impressed."),
      ("will be held", "will hold", "held", "holds", "Passive masa depan."),
      ("and", "but", "so", "or", "Menambah item."),
      ("If you cannot attend, please let us know in advance.", "Sales are growing every year.", "The office has a new carpet.", "Interviews are always difficult.", "Menyambung undangan wawancara.")]
T8 = "Our company is proud to {0} its new online store. Customers can browse more than five hundred products, {1} orders, and track deliveries from their phones. As a launch offer, shipping is free for orders {2} fifty dollars. {3}"
B8 = [("announce", "announcement", "announced", "announcing", "To + kata kerja dasar."),
      ("place", "places", "placing", "placed", "Can browse, place, and track (paralel)."),
      ("over", "on", "at", "above to", "Over fifty dollars."),
      ("The offer ends on the last day of this month.", "Phones are very useful.", "Our founders came from Bali.", "Fifty is a round number.", "Menyambung tentang penawaran.")]
all3 = []
for title, t, b in (("pengumuman air", T6, B6), ("undangan wawancara", T7, B7), ("toko online", T8, B8)):
    all3 += text_qs(title, t, b)
X3 = dict(practice=all3[:8], quiz=all3[8:])
