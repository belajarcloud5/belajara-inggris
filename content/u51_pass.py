from qk import mk, mkf, mko
PASS = dict(practice=mk([
 ('Pilih bentuk formal yang tepat: "Your order ___ sent."', "has been", "have been", "was be", "is have", "Tunggal → has been + V3."),
 ('Pilih bentuk formal yang tepat: "The date will ___ confirmed."', "be", "is", "been", "being", "will be + V3."),
 ('Pilih bentuk formal yang tepat: "The form must ___ submitted."', "be", "is", "been", "being", "must be + V3."),
 ('Pilih bentuk formal yang tepat: "Your payment ___ received."', "has been", "have been", "is been", "was be", "has been + V3."),
 ('Pilih pasif formal dari "We received your payment.":', "Your payment has been received.", "Your payment received.", "Your payment is received by we.", "Your payment have been received.", "has been + V3."),
 ('Pilih pasif formal dari "You must send the form.":', "The form must be sent.", "The form must sent.", "The form must be send.", "The form must been sent.", "must be + V3."),
 ('Pilih kalimat yang SALAH:', "Your request has receive.", "Your request has been received.", "Your requests have been received.", "Your request was received.", "has been received."),
]) + mkf([
 ("Pesanan Anda sudah dikirim.", "Your order has ___ sent.", "been", "has been + V3."),
 ("Tanggalnya akan dikonfirmasi.", "The date will be ___.", "confirmed", "will be + V3."),
 ("Formulir harus diserahkan.", "The form must be ___.", "submitted", "must be + V3."),
 ("Pembayaran Anda sudah diterima.", "Your payment has been ___.", "received", "has been + V3."),
]), quiz=mk([
 ('Pilih bentuk formal yang tepat: "Your request has been ___ and will be processed."', "received", "receive", "receiving", "receives", "has been + V3."),
 ('Pilih bentuk formal yang tepat: "The documents ___ attached."', "are", "is", "does", "has", "Jamak → are attached."),
 ('Pilih kalimat yang SALAH:', "The file have been sent.", "The file has been sent.", "The files have been sent.", "The file was sent.", "file tunggal → has."),
]) + mkf([
 ("Permintaan Anda akan diproses.", "Your request will be ___.", "processed", "will be + V3."),
]))
