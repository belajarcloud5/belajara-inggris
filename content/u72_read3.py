READ3 = [{'focus': 'campuran present',
  'id': 'Interviewer: Apa pekerjaan Anda?\n'
        'Maya: Saya bekerja sebagai perawat. Saya sudah bekerja di rumah sakit ini selama enam tahun.\n'
        'Interviewer: Apa yang sedang Anda lakukan saat ini?\n'
        'Maya: Saya sedang mengikuti kursus pada malam hari. Saya belajar sejak bulan Maret.\n'
        'Interviewer: Sudahkah Anda selesai?\n'
        'Maya: Belum. Saya sudah menyelesaikan tiga modul, dan sekarang saya tahu dasar-dasarnya.',
  'qs': [{'answer': 0,
          'exp': 'Maya: "I have worked at this hospital for six years".',
          'options': ['For six years', 'Since March', 'For three months', 'For two years'],
          'q': 'How long has Maya worked at the hospital?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'know tidak continuous.',
          'options': ['I am knowing the basics now.', 'I know the basics now.', 'I work as a nurse.', "I've been studying since March."],
          'q': 'Which sentence has a mistake?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'for + durasi.',
          'options': ['have worked', 'work', 'worked', 'am working'],
          'q': 'Choose the correct word: "I ___ at this hospital for six years."',
          'type': 'mcq'},
         {'answers': ["'m taking"],
          'exp': 'Sementara/sekarang.',
          'hint': "' _ / t _ _ _ _ _",
          'id': "Lengkapi dengan 'm taking atau take:",
          'q': 'I ___ a course in the evenings. (sekarang)',
          'type': 'fill'},
         {'answers': ['since'],
          'exp': 'since + titik awal.',
          'hint': 's _ _ _ _',
          'id': 'Lengkapi dengan since atau for:',
          'q': "I've been studying ___ March.",
          'type': 'fill'},
         {'answer': "I've completed three modules.",
          'exp': "Urutan: I've completed three modules.",
          'extra': ['was', 'complete'],
          'q': 'Susun kalimat dari cerita: "Saya sudah menyelesaikan tiga modul."',
          'type': 'order'}],
  'text': 'Interviewer: What do you do?\n'
          'Maya: I work as a nurse. I have worked at this hospital for six years.\n'
          'Interviewer: What are you doing at the moment?\n'
          "Maya: I'm taking a course in the evenings. I've been studying since March.\n"
          'Interviewer: Have you finished?\n'
          "Maya: Not yet. I've completed three modules, and I know the basics now.",
  'title': 'How Long Have You...?'}]
