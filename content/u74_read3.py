READ3 = [{'focus': 'tense dalam cerita dan laporan',
  'id': 'Dina: Apakah kamu berbicara dengan manajer?\n'
        'Tom: Ya. Dia bilang rapat akan dimulai pukul sepuluh.\n'
        'Dina: Apa lagi yang dia katakan?\n'
        'Tom: Dia memberitahuku bahwa penjualan naik sepuluh persen.\n'
        'Dina: Kabar baik! Apakah dia menyebut bonus?\n'
        'Tom: Dia bilang kalau kita mencapai target, kita akan mendapatkannya.',
  'qs': [{'answer': 0,
          'exp': 'Tom: "the meeting would start at ten".',
          'options': ['The meeting', 'The sale', 'The bonus', 'The target'],
          'q': 'What did the manager say would start at ten?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'will → would.',
          'options': ['He said that the meeting will start at ten.',
                      'He said that the meeting would start at ten.',
                      'He told me that sales had increased.',
                      'If we reached the target, we would get one.'],
          'q': 'Which sentence has a mistake?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'will → would.',
          'options': ['would', 'will', 'can', 'does'],
          'q': 'Choose the correct word: "He said the meeting ___ start at ten."',
          'type': 'mcq'},
         {'answers': ['had'],
          'exp': 'Present perfect → past perfect.',
          'hint': 'h _ _',
          'id': 'Lengkapi dengan had atau has:',
          'q': 'He told me that sales ___ increased.',
          'type': 'fill'},
         {'answers': ['would'],
          'exp': 'Type 2.',
          'hint': 'w _ _ _ _',
          'id': 'Lengkapi dengan would atau will:',
          'q': 'If we reached the target, we ___ get a bonus.',
          'type': 'fill'},
         {'answer': 'He said that the meeting would start at ten.',
          'exp': 'Urutan: He said that the meeting would start at ten.',
          'extra': ['will'],
          'q': 'Susun kalimat dari cerita: "Dia bilang rapat akan dimulai pukul sepuluh."',
          'type': 'order'}],
  'text': 'Dina: Did you talk to the manager?\n'
          'Tom: Yes. He said that the meeting would start at ten.\n'
          'Dina: What else did he say?\n'
          'Tom: He told me that sales had increased by ten percent.\n'
          'Dina: Good news! Did he mention the bonus?\n'
          'Tom: He said that if we reached the target, we would get one.',
  'title': 'Reported Conversation'}]
