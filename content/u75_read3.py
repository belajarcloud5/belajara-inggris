READ3 = [{'focus': 'campuran semua tense',
  'id': 'Anna: Apa yang kamu lakukan kemarin?\n'
        'Budi: Aku bangun kesiangan. Sementara aku sarapan, temanku menelepon.\n'
        'Anna: Dia mau apa?\n'
        'Budi: Dia bertanya apakah aku sudah menyelesaikan PR. Belum, jadi aku mengerjakannya berjam-jam.\n'
        'Anna: Dan hari ini?\n'
        'Budi: Hari ini aku beristirahat. Aku sudah bekerja begitu banyak sampai perlu istirahat. Besok aku akan sedang bertemu dengannya pukul '
        'sepuluh.',
  'qs': [{'answer': 0,
          'exp': 'Budi: "Today I\'m resting".',
          'options': ['Resting', 'Working for hours', 'Eating breakfast', 'Meeting his friend'],
          'q': 'What is Budi doing today?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Latar continuous, memotong simple.',
          'options': ['While I ate breakfast, my friend was calling.',
                      'While I was eating breakfast, my friend called.',
                      'She asked if I had finished.',
                      "Tomorrow I'll be meeting her."],
          'q': 'Which sentence has a mistake?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'while + continuous.',
          'options': ['was eating', 'ate', 'eat', 'have eaten'],
          'q': 'Choose the correct word: "While I ___ breakfast, my friend called."',
          'type': 'mcq'},
         {'answers': ['had'],
          'exp': 'Reported + past perfect.',
          'hint': 'h _ _',
          'id': 'Lengkapi dengan had atau have:',
          'q': 'She asked if I ___ finished my homework.',
          'type': 'fill'},
         {'answers': ['been'],
          'exp': 'have been + V-ing.',
          'hint': 'b _ _ _',
          'id': 'Lengkapi dengan been atau be:',
          'q': "I've ___ working so much.",
          'type': 'fill'},
         {'answer': "Tomorrow I'll be meeting her at ten.",
          'exp': "Urutan: Tomorrow I'll be meeting her at ten.",
          'extra': ['will', 'meeting'],
          'q': 'Susun kalimat dari cerita: "Besok aku akan sedang bertemu dengannya pukul sepuluh."',
          'type': 'order'}],
  'text': 'Anna: What did you do yesterday?\n'
          'Budi: I woke up late. While I was eating breakfast, my friend called.\n'
          'Anna: What did she want?\n'
          "Budi: She asked if I had finished my homework. I hadn't, so I worked for hours.\n"
          'Anna: And today?\n'
          "Budi: Today I'm resting. I've been working so much that I need a break. Tomorrow I'll be meeting her at ten.",
  'title': 'A Day of Everything'}]
