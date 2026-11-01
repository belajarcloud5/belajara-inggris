READ = [{'focus': 'tense dalam cerita dan laporan',
  'id': 'Reporter: Kebakaran menghancurkan pasar tadi malam.\n'
        'Officer: Api mulai pukul sembilan. Pada tengah malam, petugas pemadam sudah memadamkannya.\n'
        'Reporter: Apa kata pemiliknya?\n'
        'Officer: Dia bilang dia sangat sedih. Dia bilang dia akan membangun kembali tokonya.\n'
        'Reporter: Dan apa yang terjadi berikutnya?\n'
        'Officer: Kalau cuaca tetap kering, pembersihan akan selesai pada hari Jumat.',
  'qs': [{'answer': 0,
          'exp': 'Officer: "He said he would rebuild his shop".',
          'options': ['Rebuild his shop', 'Close his shop', 'Move to another city', 'Sell the land'],
          'q': 'What did the owner say he would do?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'will → would.',
          'options': ['He said he will rebuild his shop.',
                      'He said he would rebuild his shop.',
                      'The fire started at nine.',
                      'The firefighters had put it out.'],
          'q': 'Which sentence has a mistake?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Past simple.',
          'options': ['started', 'has started', 'starts', 'was start'],
          'q': 'Choose the correct word: "The fire ___ at nine."',
          'type': 'mcq'},
         {'answers': ['had'],
          'exp': 'Past perfect.',
          'hint': 'h _ _',
          'id': 'Lengkapi dengan had atau have:',
          'q': 'By midnight, the firefighters ___ put it out.',
          'type': 'fill'},
         {'answers': ['will'],
          'exp': 'Type 1.',
          'hint': 'w _ _ _',
          'id': 'Lengkapi dengan will atau would:',
          'q': 'If the weather stays dry, the cleanup ___ finish by Friday.',
          'type': 'fill'},
         {'answer': 'He said he was very sad.',
          'exp': 'Urutan: He said he was very sad.',
          'extra': ['is'],
          'q': 'Susun kalimat dari cerita: "Dia bilang dia sangat sedih."',
          'type': 'order'}],
  'text': 'Reporter: A fire destroyed the market last night.\n'
          'Officer: The fire started at nine. By midnight, the firefighters had put it out.\n'
          'Reporter: What did the owner say?\n'
          'Officer: He said he was very sad. He said he would rebuild his shop.\n'
          'Reporter: And what will happen next?\n'
          'Officer: If the weather stays dry, the cleanup will finish by Friday.',
  'title': 'News and Reports'}]
