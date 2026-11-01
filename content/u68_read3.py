READ3 = [{'focus': 'past perfect',
  'id': 'Reporter: Para penumpang menunggu di bandara berjam-jam kemarin.\n'
        'Official: Penerbangan itu telah tertunda dua kali sebelum akhirnya lepas landas.\n'
        'Reporter: Apa penyebab penundaan?\n'
        'Official: Hujan lebat telah menutup landasan, dan masalah teknis telah ditemukan pada salah satu mesin.\n'
        'Reporter: Bagaimana perasaan penumpang?\n'
        'Official: Banyak yang marah karena sudah menunggu sejak pagi.',
  'qs': [{'answer': 0,
          'exp': 'Official: "delayed twice".',
          'options': ['Twice', 'Once', 'Three times', 'Never'],
          'q': 'How many times had the flight been delayed?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'had + V3.',
          'options': ['Heavy rain has closed the runway before.',
                      'Heavy rain had closed the runway.',
                      'The flight had been delayed twice.',
                      'Many were angry because they had been waiting.'],
          'q': 'Which sentence has a mistake?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'had been + V3.',
          'options': ['had', 'has', 'have', 'was'],
          'q': 'Choose the correct word: "The flight ___ been delayed twice."',
          'type': 'mcq'},
         {'answers': ['had'],
          'exp': 'Lebih dulu.',
          'hint': 'h _ _',
          'id': 'Lengkapi dengan had atau has:',
          'q': 'Heavy rain ___ closed the runway.',
          'type': 'fill'},
         {'answers': ['had'],
          'exp': 'had been + V-ing.',
          'hint': 'h _ _',
          'id': 'Lengkapi dengan had atau have:',
          'q': 'They ___ been waiting since morning.',
          'type': 'fill'},
         {'answer': 'Many were angry because they had been waiting.',
          'exp': 'Urutan: Many were angry because they had been waiting.',
          'extra': ['have'],
          'q': 'Susun kalimat dari cerita: "Banyak yang marah karena sudah menunggu."',
          'type': 'order'}],
  'text': 'Reporter: Passengers waited at the airport for hours yesterday.\n'
          'Official: The flight had been delayed twice before it finally took off.\n'
          'Reporter: What had caused the delay?\n'
          'Official: Heavy rain had closed the runway, and a technical problem had been found in one engine.\n'
          'Reporter: How did passengers feel?\n'
          'Official: Many were angry because they had been waiting since morning.',
  'title': 'The Late Flight'}]
