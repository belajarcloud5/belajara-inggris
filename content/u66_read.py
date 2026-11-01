READ = [{'focus': 'present perfect vs past simple',
  'id': 'Interviewer: Pernahkah Anda bekerja di bank?\n'
        'Maya: Ya, pernah. Saya bekerja di bank pada tahun 2019.\n'
        'Interviewer: Kapan Anda berhenti?\n'
        'Maya: Saya berhenti tahun lalu. Sejak itu, saya belajar.\n'
        'Interviewer: Sudahkah Anda menyelesaikan kursus?\n'
        'Maya: Belum. Saya sudah menyelesaikan dua modul, tetapi belum mengikuti ujian akhir.',
  'qs': [{'answer': 0,
          'exp': 'Maya: "I left last year".',
          'options': ['Last year', 'In 2019', 'Yesterday', 'Next month'],
          'q': 'When did Maya leave the bank?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'in 2019 → past simple.',
          'options': ['I have worked in a bank in 2019.',
                      'I worked in a bank in 2019.',
                      'Have you ever worked in a bank?',
                      "I haven't taken the final exam."],
          'q': 'Which sentence has a mistake?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'in 2019 → past simple.',
          'options': ['worked', 'have worked', 'work', 'am working'],
          'q': 'Choose the correct word: "I ___ in a bank in 2019."',
          'type': 'mcq'},
         {'answers': ['did'],
          'exp': 'When + did.',
          'hint': 'd _ _',
          'id': 'Lengkapi dengan did atau have:',
          'q': 'When ___ you leave?',
          'type': 'fill'},
         {'answers': ['have'],
          'exp': 'Hasil sekarang → perfect.',
          'hint': 'h _ _ _',
          'id': 'Lengkapi dengan have atau has:',
          'q': 'I ___ completed two modules.',
          'type': 'fill'},
         {'answer': 'Not yet. I have completed two modules.',
          'exp': 'Urutan: Not yet. I have completed two modules.',
          'extra': ['completed'],
          'q': 'Susun kalimat dari cerita: "Belum. Saya sudah menyelesaikan dua modul."',
          'type': 'order'}],
  'text': 'Interviewer: Have you ever worked in a bank?\n'
          'Maya: Yes, I have. I worked in a bank in 2019.\n'
          'Interviewer: When did you leave?\n'
          'Maya: I left last year. Since then, I have been studying.\n'
          'Interviewer: Have you finished your course?\n'
          "Maya: Not yet. I have completed two modules, but I haven't taken the final exam.",
  'title': 'A Job Interview'}]
