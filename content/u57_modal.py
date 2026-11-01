from qk import mk, mkf, mko
MODAL = dict(practice=mk([
 ('Pilih ungkapan yang paling sopan untuk menawarkan bantuan:', "May I help you?", "What you want?", "Tell me.", "You need help?", "May I help you? sopan."),
 ('Pilih ungkapan untuk meminta nomor pesanan dengan sopan:', "Could you give me your order number?", "Give me your order number.", "Order number?", "You give order number.", "Could you ... sopan."),
 ('Pilih kalimat yang menolak dengan sopan:', "I'm afraid we cannot refund this item.", "We cannot.", "No refund.", "We don't refund.", "I'm afraid ... lebih sopan."),
 ('Pilih jawaban yang benar: "We ___ send a new one." (menawarkan solusi)', "can", "mustn't", "needn't", "ought", "Menawarkan → We can."),
 ('Pilih jawaban yang benar: "Shall I ___ the order for you?"', "check", "checks", "to check", "checking", "Shall I + V1."),
 ('Pilih jawaban yang benar: "You ___ exchange it for another." (memberi pilihan)', "could", "mustn't", "can't to", "ought", "Memberi pilihan → You could."),
 ('Pilih kalimat yang SALAH:', "May I to help you?", "May I help you?", "Can I help you?", "Shall I help you?", "Setelah modal, V1 tanpa to."),
]) + mkf([
 ("Bisakah saya membantu Anda?", "___ I help you?", "May/Can/Shall", "May, Can, atau Shall."),
 ("Bisakah Anda memberi saya nomor Anda?", "___ you give me your number?", "Could/Can", "Could atau Can."),
 ("Maaf, kami tidak bisa mengembalikan uang.", "I'm afraid we ___ refund this.", "cannot/can't", "cannot atau can't."),
 ("Kami bisa mengirim yang baru.", "We ___ send a new one.", "can", "We can."),
]), quiz=mk([
 ('Pilih ungkapan yang paling sopan:', "Could you wait a moment, please?", "Wait.", "You wait.", "Wait a moment.", "Could you ... please sopan."),
 ('Pilih jawaban yang benar: "I\'m afraid we ___ do that." (tidak bisa)', "cannot", "can", "must", "needn't", "I'm afraid we cannot."),
 ('Pilih kalimat yang SALAH:', "Shall I to check?", "Shall I check?", "Can I check?", "May I check?", "Shall I + V1 tanpa to."),
]) + mkf([
 ("Anda bisa menukarnya dengan yang lain.", "You ___ exchange it.", "could/can", "could atau can."),
]))
