READ3 = [{'focus': 'present simple vs continuous',
  'id': 'Waiter: Selamat siang. Mau pesan apa?\n'
        'Dina: Saya mau kopi, tolong. Saya suka yang kuat.\n'
        'Waiter: Ada yang lain? Hari ini kami punya kue segar.\n'
        'Dina: Saya akan makan siang dengan teman nanti, jadi kopi saja.\n'
        'Waiter: Baik. Apakah teman Anda akan datang sekarang?\n'
        'Dina: Ya, dia datang pukul satu. Dia bekerja di dekat sini, dan dia selalu tiba tepat waktu.',
  'qs': [{'answer': 0,
          'exp': 'Dina: "I like it strong".',
          'options': ['Strong coffee', 'Fresh cake with cream', 'Tea with milk and sugar', 'Cold juice with ice'],
          'q': 'What does Dina like?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'want tidak continuous.',
          'options': ['I am wanting a coffee.', 'I want a coffee.', "I'm having lunch with a friend.", 'She always arrives on time.'],
          'q': 'Which sentence has a mistake?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'want = stative.',
          'options': ['want', 'am wanting', 'have wanted', 'wanted'],
          'q': 'Choose the correct word: "I ___ a coffee, please."',
          'type': 'mcq'},
         {'answers': ['works'],
          'exp': 'Fakta tetap.',
          'hint': 'w _ _ _ _',
          'id': 'Lengkapi dengan works atau is working:',
          'q': 'She ___ near here.',
          'type': 'fill'},
         {'answers': ['arrives'],
          'exp': 'always → simple.',
          'hint': 'a _ _ _ _ _ _',
          'id': 'Lengkapi dengan arrives atau is arriving:',
          'q': 'She always ___ on time.',
          'type': 'fill'},
         {'answer': 'I like it strong.',
          'exp': 'Urutan: I like it strong.',
          'extra': ['am', 'liking'],
          'q': 'Susun kalimat dari cerita: "Saya suka yang kuat."',
          'type': 'order'}],
  'text': 'Waiter: Good afternoon. What would you like?\n'
          'Dina: I want a coffee, please. I like it strong.\n'
          'Waiter: Anything else? We have fresh cake today.\n'
          "Dina: I'm having lunch with a friend later, so just coffee.\n"
          'Waiter: Of course. Is your friend coming now?\n'
          'Dina: Yes, she is coming at one. She works near here, and she always arrives on time.',
  'title': 'At the Café'}]
