READ = [{'id': 'Resepsionis: Selamat malam. Selamat datang di Hotel Grand Mulia. Apakah Anda sudah memesan?\n'
        'Tamu: Ya, atas nama Anwar Santoso. Saya memesan satu kamar single untuk tiga malam. Resepsionis: Mari saya periksa. Ya, Pak Santoso, kamar '
        '805 di lantai delapan. Sarapan disajikan pukul 06.30 sampai 10.00 di restoran lantai dasar. Waktu check-out pukul 12.00 siang. Ini kunci '
        'kartunya. Tamu: Terima kasih. Bisakah saya mendapat panggilan pagi pukul enam besok?',
  'qs': [{'answer': 0,
          'exp': 'Guest: "a single room for three nights."',
          'options': ['Three nights', 'One night', 'Five nights', 'A week'],
          'q': 'How long will Mr. Santoso stay?',
          'type': 'mcq'},
         {'answer': 0, 'exp': 'Receptionist: "room 805".', 'options': ['805', '508', '850', '815'], 'q': 'What is his room number?', 'type': 'mcq'},
         {'answer': 0,
          'exp': 'Receptionist: "restaurant on the ground floor."',
          'options': ['In the restaurant on the ground floor',
                      'In his own room on the eighth floor',
                      'On the eighth floor, next to the lift',
                      'In the lobby near the reception desk'],
          'q': 'Where is breakfast served?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Guest: "a wake-up call at six tomorrow."',
          'options': ['A wake-up call at six', 'A taxi', 'A late check-out', 'A free upgrade'],
          'q': 'What does the guest ask for?',
          'type': 'mcq'}],
  'text': 'Receptionist: Good evening. Welcome to Grand Mulia Hotel. Do you have a reservation?\n'
          'Guest: Yes, under the name Anwar Santoso. I booked a single room for three nights. Receptionist: Let me check. Yes, Mr. Santoso, room 805 '
          'on the eighth floor. Breakfast is served from 6.30 to 10.00 in the restaurant on the ground floor. Check-out time is 12.00 noon. Here is '
          'your key card. Guest: Thank you. Could I get a wake-up call at six tomorrow?',
  'title': 'At the Hotel Reception'},
 {'id': 'Hari 1 (Senin): Penerbangan GA 410 berangkat dari Jakarta pukul 07.00 dan tiba di Singapura pukul 09.50. Check-in di hotel, lalu menghadiri '
        'rapat klien pukul 14.00. Makan malam dengan tim Singapura pukul 19.00.\n'
        'Hari 2 (Selasa): Presentasi di kantor klien pukul 10.00, dilanjutkan kunjungan pabrik. Hari 3 (Rabu): Pagi bebas untuk berbelanja. '
        'Penerbangan pulang pukul 15.30 dan mendarat di Jakarta pukul 16.20. Mobil perusahaan akan menjemput Anda di bandara.',
  'qs': [{'answer': 0,
          'exp': 'Teks: "departs Jakarta at 7.00 a.m."',
          'options': ['7.00 a.m. on Monday', '9.50 a.m. on Monday', '2.00 p.m. on Monday', '7.00 p.m. on Tuesday'],
          'q': 'When does the flight to Singapore depart?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Teks: "Presentation at the client\'s office at 10.00 a.m."',
          'options': ["A presentation at the client's office",
                      "A factory visit at the client's other site",
                      'Shopping for souvenirs near the hotel',
                      'A flight back to Jakarta in the morning'],
          'q': 'What happens on Tuesday at 10.00 a.m.?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Teks: "Free morning for shopping."',
          'options': ['Go shopping', 'Attend a meeting', 'Visit the factory', 'Work in the office'],
          'q': 'What can the traveler do on Wednesday morning?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Teks: "A company car will pick you up".',
          'options': ['By company car', 'By taxi', 'By train', 'By bus'],
          'q': 'How will the traveler go from the Jakarta airport?',
          'type': 'mcq'}],
  'text': 'Day 1 (Monday): Flight GA 410 departs Jakarta at 7.00 a.m. and arrives in Singapore at 9.50 a.m. Check in at the hotel, then attend a '
          'client meeting at 2.00 p.m. Dinner with the Singapore team at 7.00 p.m.\n'
          "Day 2 (Tuesday): Presentation at the client's office at 10.00 a.m., followed by a factory visit. Day 3 (Wednesday): Free morning for "
          'shopping. Flight returns at 3.30 p.m. and lands in Jakarta at 4.20 p.m. A company car will pick you up at the airport.',
  'title': 'Business Trip Itinerary'}]
