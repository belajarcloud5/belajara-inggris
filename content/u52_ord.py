from qk import mko
ORD = dict(practice=mko([('Selamat pagi, ada yang bisa saya bantu?', 'Good morning, how can I help you?', 'helps', ''),
 ('Boleh saya tahu siapa yang menelepon?', "May I ask who's calling?", 'call', ''),
 ('Mohon tunggu, saya sambungkan.', "Please hold, I'll put you through.", 'holds', ''),
 ('Beliau sedang tidak di tempat.', 'He is not available right now.', 'are', ''),
 ('Bisakah saya meninggalkan pesan?', 'Can I leave a message?', 'leaves', ''),
 ('Bisakah Anda mengeja nama Anda?', 'Could you spell your name, please?', 'spells', ''),
 ('Saya akan menelepon balik nanti.', 'I will call you back later.', 'calls', '')]), quiz=mko([('Saya tidak bisa mendengar Anda dengan jelas.', "I can't hear you clearly.", 'hears', ''),
 ('Bisakah Anda berbicara lebih pelan?', 'Could you speak more slowly?', 'slow', ''),
 ('Terima kasih telah menelepon.', 'Thank you for calling.', 'called', '')]))
