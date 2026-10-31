from qk import mko
ORD = dict(practice=mko([('Bisakah kita membuat janji temu?', 'Can we make an appointment?', 'makes', ''),
 ('Bagaimana kalau Selasa pukul sepuluh?', 'How about Tuesday at ten?', 'what', ''),
 ('Saya ingin menjadwal ulang rapat.', "I'd like to reschedule the meeting.", 'reschedules', ''),
 ('Saya perlu membatalkan janji kita.', 'I need to cancel our appointment.', 'cancels', ''),
 ('Apakah Anda senggang besok sore?', 'Are you free tomorrow afternoon?', 'Do', ''),
 ('Tenggat waktunya hari Jumat.', 'The deadline is Friday.', 'are', ''),
 ('Rapat diundur ke minggu depan.', 'The meeting was postponed to next week.', 'were', '')]), quiz=mko([('Mohon konfirmasi jadwalnya.', 'Please confirm the schedule.', 'confirms', ''),
 ('Waktu mana yang paling cocok bagi Anda?', 'What time suits you best?', 'suit', ''),
 ('Mari bertemu Rabu depan.', "Let's meet next Wednesday.", 'meets', '')]))
