from qk import mk, mkf, mko
GER = dict(practice=mk([
 ('Pilih jawaban yang benar: "I suggest ___ the deadline."', "moving", "to move", "move", "moved", "suggest + V-ing."),
 ('Pilih jawaban yang benar: "We agreed ___ in June."', "to start", "starting", "start", "started", "agree + to V1."),
 ('Pilih jawaban yang benar: "The team decided ___ two people."', "to hire", "hiring", "hire", "hired", "decide + to V1."),
 ('Pilih jawaban yang benar: "We should avoid ___ too much."', "spending", "to spend", "spend", "spent", "avoid + V-ing."),
 ('Pilih jawaban yang benar: "We plan ___ by Friday."', "to finish", "finishing", "finish", "finished", "plan + to V1."),
 ('Pilih jawaban yang benar: "Let\'s consider ___ the budget."', "reducing", "to reduce", "reduce", "reduced", "consider + V-ing."),
 ('Pilih kalimat yang SALAH:', "Anna suggested to reduce costs.", "Anna suggested reducing costs.", "Anna agreed to reduce costs.", "Anna decided to reduce costs.", "suggest + V-ing."),
 ('Pilih kalimat yang SALAH:', "We agreed starting in June.", "We agreed to start in June.", "We planned to start in June.", "We decided to start in June.", "agree + to V1."),
]) + mkf([
 ("Saya menyarankan memindahkan tenggat.", "I suggest ___ the deadline.", "moving", "suggest + V-ing."),
 ("Kami sepakat untuk mulai bulan Juni.", "We agreed ___ start in June.", "to", "agree + to V1."),
 ("Kita sebaiknya menghindari pengeluaran berlebihan.", "We should avoid ___ too much.", "spending", "avoid + V-ing."),
 ("Kami berencana selesai sebelum Jumat.", "We plan ___ finish by Friday.", "to", "plan + to V1."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "Sam recommended ___ the plan."', "changing", "to change", "change", "changed", "recommend + V-ing."),
 ('Pilih jawaban yang benar: "They postponed ___ the meeting."', "holding", "to hold", "hold", "held", "postpone + V-ing."),
 ('Pilih kalimat yang SALAH:', "We decided postponing the launch.", "We decided to postpone the launch.", "We considered postponing the launch.", "We agreed to postpone the launch.", "decide + to V1."),
]) + mkf([
 ("Kami memutuskan untuk meninjau anggaran.", "We decided ___ review the budget.", "to", "decide + to V1."),
]))
