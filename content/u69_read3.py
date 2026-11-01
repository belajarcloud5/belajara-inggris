READ3 = [{'focus': 'will vs be going to',
  'id': 'Agent: Ke mana Anda akan berlibur?\n'
        'Dina: Kami akan terbang ke Bali. Kami sudah memesan hotel.\n'
        'Agent: Penerbangan berangkat pukul tujuh besok pagi.\n'
        'Dina: Saya akan check-in daring malam ini. Bagaimana cuacanya nanti?\n'
        'Agent: Menurut saya akan cerah, tetapi mungkin hujan di sore hari.\n'
        'Dina: Kalau begitu saya akan membawa payung.',
  'qs': [{'answer': 0,
          'exp': 'Agent: "The flight leaves at seven tomorrow morning".',
          'options': ['At seven tomorrow morning', 'At seven tonight at six', 'At nine tomorrow morning', 'Next week on Monday'],
          'q': 'When does the flight leave?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Jadwal → simple.',
          'options': ['The flight will leaves at seven.', 'The flight leaves at seven.', "We're going to fly to Bali.", 'I think it will be sunny.'],
          'q': 'Which sentence has a mistake?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Rencana.',
          'options': ['are going to', 'will', 'would', 'fly'],
          'q': 'Choose the correct word: "We ___ fly to Bali. It\'s planned."',
          'type': 'mcq'},
         {'answers': ['leaves'],
          'exp': 'Jadwal.',
          'hint': 'l _ _ _ _ _',
          'id': 'Lengkapi dengan leaves atau will leaves:',
          'q': 'The flight ___ at seven tomorrow.',
          'type': 'fill'},
         {'answers': ['will'],
          'exp': 'Prediksi/opini → will.',
          'hint': 'w _ _ _',
          'id': 'Lengkapi dengan will atau is going:',
          'q': 'I think it ___ be sunny.',
          'type': 'fill'},
         {'answer': "I'll check in online tonight.",
          'exp': "Urutan: I'll check in online tonight.",
          'extra': ['am', 'check'],
          'q': 'Susun kalimat dari cerita: "Saya akan check-in daring malam ini."',
          'type': 'order'}],
  'text': 'Agent: Where are you going on holiday?\n'
          "Dina: We're going to fly to Bali. We've already booked the hotel.\n"
          'Agent: The flight leaves at seven tomorrow morning.\n'
          "Dina: I'll check in online tonight. What will the weather be like?\n"
          'Agent: I think it will be sunny, but it may rain in the afternoon.\n'
          "Dina: Then I'm going to pack an umbrella.",
  'title': 'At the Travel Agent'}]
