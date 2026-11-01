READ = [{'focus': 'klausa waktu',
  'id': 'Anna: Apa yang akan kamu lakukan ketika rapat selesai?\n'
        'Budi: Begitu rapat selesai, aku akan menelepon kakakku.\n'
        'Anna: Aku akan menunggu sampai kamu selesai.\n'
        'Budi: Terima kasih. Sebelum meninggalkan kantor, aku selalu mengunci mejaku.\n'
        'Anna: Ketika aku sampai di sini pagi ini, kamu sudah berangkat ke bandara.\n'
        'Budi: Ya, sementara aku menunggu di gerbang, aku sadar aku lupa membawa paspor!',
  'qs': [{'answer': 0,
          'exp': 'Budi: "I had forgotten my passport".',
          'options': ['His passport', 'His phone and his keys', 'His bag and his wallet', 'His car and his ticket'],
          'q': 'What did Budi forget?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Jangan will setelah as soon as.',
          'options': ['As soon as it will end, I will call my sister.',
                      'As soon as it ends, I will call my sister.',
                      'I will wait until you finish.',
                      'I always lock my desk.'],
          'q': 'Which sentence has a mistake?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'as soon as + present.',
          'options': ['ends', 'will end', 'ended', 'ending'],
          'q': 'Choose the correct word: "As soon as it ___, I will call my sister."',
          'type': 'mcq'},
         {'answers': ['was waiting'],
          'exp': 'while + continuous.',
          'hint': 'w _ _ / w _ _ _ _ _ _',
          'id': 'Lengkapi dengan was waiting atau waited:',
          'q': 'While I ___ at the gate, I realized I had forgotten my passport.',
          'type': 'fill'},
         {'answers': ['had'],
          'exp': 'Lebih dulu → had.',
          'hint': 'h _ _',
          'id': 'Lengkapi dengan had atau have:',
          'q': 'When I got here, you ___ already left.',
          'type': 'fill'},
         {'answer': 'I will wait until you finish.',
          'exp': 'Urutan: I will wait until you finish.',
          'extra': ['will', 'finish'],
          'q': 'Susun kalimat dari cerita: "Aku akan menunggu sampai kamu selesai."',
          'type': 'order'}],
  'text': 'Anna: What will you do when the meeting ends?\n'
          'Budi: As soon as it ends, I will call my sister.\n'
          'Anna: I will wait until you finish.\n'
          'Budi: Thanks. Before I leave the office, I always lock my desk.\n'
          'Anna: When I got here this morning, you had already left for the airport.\n'
          'Budi: Yes, while I was waiting at the gate, I realized I had forgotten my passport!',
  'title': 'Plans After the Meeting'}]
