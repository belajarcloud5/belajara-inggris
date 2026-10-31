from qk import mk
R3 = dict(practice=mk([
 ("Terjemahan \"Saya menulis untuk menanyakan status pesanan saya\":","I am writing to ask about the status of my order.","I writing ask about my order status.","I am write to asking status of order.","I write for ask the order status.","tr."),
 ("Terjemahan \"Mohon maaf atas keterlambatan balasan kami\":","We apologize for the delay in our reply.","We apology for delay of reply our.","We apologize about the late reply of us.","We are apologizing delay reply.","tr."),
 ("Terjemahan \"Kami lampirkan jadwal pelatihan\":","We have attached the training schedule.","We attach training schedule have.","We are attach the schedule training.","We attached have the training schedule.","tr."),
 ("Terjemahan \"Mohon kabari kami jika ada perubahan\":","Please let us know if there are any changes.","Please let us know if any change are there.","Please let know us if changes.","Please tell us know if change.","tr."),
 ("Terjemahan \"Terima kasih atas bantuan Anda\":","Thank you for your assistance.","Thank you for assist you.","Thanks you for assistances.","Thank for your assisting.","tr."),
 ("Terjemahan \"Kami menantikan tanggapan Anda\":","We look forward to your response.","We look forward your respond.","We looking forward to response you.","We look forward to responding yours.","tr."),
 ("Perbaiki: \"I attach the file in this email.\"","I have attached the file to this email.","I attach file on this email.","I attached file at this email.","I am attach the file.","fix."),
 ("Perbaiki: \"Please reply me soon.\"","Please reply to me soon.","Please reply me soon.","Please replying me soon.","Please replies to me.","fix."),
 ("Perbaiki: \"Dear Mr. Adi, I write to inform you ...\" (alasan sekarang)","I am writing to inform you ...","I writing to inform you ...","I am write to inform you ...","I writes to inform you ...","fix."),
 ("Perbaiki: \"Looking forward to hear from you.\"","Looking forward to hearing from you.","Looking forward hear from you.","Look forward to hearing you.","Looking forward to heard from.","fix."),
 ("Dialog: \"Did you get my email?\" – \"___\"","Yes, I replied this morning.","Yes, I replying this morning.","Yes, I reply this morning was.","Yes, I am replied morning.","dialog."),
 ("Dialog: \"Can you forward it to Dina?\" – \"___\"","Sure, I'll forward it now.","Sure, I forward it now will.","Sure, I forwarding now.","Sure, I'll forwarded it.","dialog."),
]), quiz=mk([
 ("\"Kotak masuk\":","inbox","outbox","trash","drafts","word."),
 ("\"Terkirim\":","sent","send","sand","scent","word."),
 ("\"Draf\":","draft","drift","drive","dress","word."),
 ("\"Tanda tangan\":","signature","signal","significance","silence","word."),
 ("\"Kepada Yth.\":","To whom it may concern","To whom they concerned","To who it concern","To whose concern it","word."),
 ("\"Dengan hormat,\":","Sincerely,","Casually,","Hurriedly,","Randomly,","word."),
 ("\"Balas semua\":","reply all","replay all","repeat all","reply every","word."),
 ("\"Penerima\":","recipient","receipt","reception","recipe","word."),
]))
