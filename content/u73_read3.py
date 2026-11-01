READ3 = [{'focus': 'campuran past',
  'id': 'Detective: Kapan Anda menyadari jendela terbuka?\n'
        'Maid: Ketika saya masuk pukul delapan. Seseorang telah membukanya sebelum saya tiba.\n'
        'Detective: Apa yang sedang Anda lakukan ketika mendengar suara itu?\n'
        'Maid: Saya sedang membersihkan dapur. Saya sudah bekerja selama satu jam.\n'
        'Detective: Apakah Anda melihat seseorang?\n'
        'Maid: Tidak, tetapi pintu depan sudah tidak terkunci.',
  'qs': [{'answer': 0,
          'exp': 'Maid: "I was cleaning the kitchen".',
          'options': ['Cleaning the kitchen', 'Opening the window', 'Talking to a guest', 'Locking the door'],
          'q': 'What was the maid doing when she heard the noise?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Lebih dulu → had + V3.',
          'options': ['Someone has opened it before I arrived.',
                      'Someone had opened it before I arrived.',
                      'I was cleaning the kitchen.',
                      'I had been working for an hour.'],
          'q': 'Which sentence has a mistake?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Latar.',
          'options': ['was cleaning', 'cleaned', 'clean', 'had cleaned'],
          'q': 'Choose the correct word: "I ___ the kitchen when I heard the noise."',
          'type': 'mcq'},
         {'answers': ['had'],
          'exp': 'Lebih dulu.',
          'hint': 'h _ _',
          'id': 'Lengkapi dengan had atau has:',
          'q': 'Someone ___ opened the window.',
          'type': 'fill'},
         {'answers': ['had been'],
          'exp': 'had been + V-ing.',
          'hint': 'h _ _ / b _ _ _',
          'id': 'Lengkapi dengan had been atau have been:',
          'q': 'I ___ working for an hour.',
          'type': 'fill'},
         {'answer': 'I came in at eight.',
          'exp': 'Urutan: I came in at eight.',
          'extra': ['was', 'coming'],
          'q': 'Susun kalimat dari cerita: "Saya masuk pukul delapan."',
          'type': 'order'}],
  'text': 'Detective: When did you notice the window was open?\n'
          'Maid: When I came in at eight. Someone had opened it before I arrived.\n'
          'Detective: What were you doing when you heard the noise?\n'
          'Maid: I was cleaning the kitchen. I had been working for an hour.\n'
          'Detective: Did you see anyone?\n'
          'Maid: No, but the front door had been unlocked.',
  'title': "The Detective's Questions"}]
