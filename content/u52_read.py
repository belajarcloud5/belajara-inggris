READ = [{'id': 'Resepsionis: Selamat siang, PT Maju Jaya. Ada yang bisa saya bantu?\n'
        'Penelepon: Selamat siang. Bolehkah saya berbicara dengan Pak Budi dari departemen Pembelian?\n'
        'Resepsionis: Boleh saya tahu siapa yang menelepon? Penelepon: Ini Anna dari PT Global. Resepsionis: Mohon tunggu sebentar. Maaf, saluran '
        'beliau sedang sibuk. Apakah Anda mau menunggu, atau saya catat pesan? Penelepon: Tolong catat pesan. Bisakah Anda memintanya menelepon '
        'balik saya di 021-555-0123?',
  'qs': [{'answer': 0,
          'exp': 'Caller: "speak to Mr. Budi".',
          'options': ['Mr. Budi', 'The receptionist', 'Anna', 'The director'],
          'q': 'Who does the caller want to speak to?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Receptionist: "his line is busy."',
          'options': ['His line is busy.', 'He is on holiday.', 'He is in a meeting abroad.', 'He quit.'],
          'q': "Why can't the caller speak to him now?",
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Caller: "I\'ll leave a message".',
          'options': ['Leave a message', 'Hold the line', 'Call tomorrow', 'Send an email'],
          'q': 'What does the caller decide to do?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Caller: "ask him to call me back".',
          'options': ['Call her back', 'Send an email', 'Visit her office', 'Cancel the order'],
          'q': 'What does the caller ask Mr. Budi to do?',
          'type': 'mcq'}],
  'text': 'Receptionist: Good afternoon, PT Maju Jaya. How can I help you?\n'
          'Caller: Good afternoon. May I speak to Mr. Budi from the Purchasing department, please?\n'
          "Receptionist: May I ask who's calling? Caller: This is Anna from PT Global. Receptionist: One moment, please. I'm afraid his line is "
          "busy. Would you like to hold, or shall I take a message? Caller: I'll leave a message, please. Could you ask him to call me back at "
          '021-555-0123?',
  'title': 'A Phone Call'},
 {'id': 'Halo, ini Rina dari Sinar Print. Saya menelepon mengenai pesanan Anda nomor 4521. Sayangnya, poster akan terlambat dua hari karena masalah '
        'pada mesin cetak. Poster seharusnya siap Jumat pagi.\n'
        'Mohon maaf atas ketidaknyamanannya. Jika hari Jumat terlalu lambat, silakan telepon balik saya di 0812-9876-5432 dan kita akan mencari '
        'solusi lain. Terima kasih, dan semoga hari Anda menyenangkan.',
  'qs': [{'answer': 0,
          'exp': 'Teks: "the posters will be delayed by two days".',
          'options': ['A delayed order', 'A new job', 'A meeting invitation', 'A price list'],
          'q': 'What is the voicemail about?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Teks: "because of a printer problem."',
          'options': ['A printer problem', 'A traffic jam', 'A holiday', 'A lost file'],
          'q': 'Why is the order delayed?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Teks: "ready on Friday morning."',
          'options': ['On Friday morning', 'On Wednesday', 'On Monday', 'Tonight'],
          'q': 'When should the posters be ready?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Teks: "please call me back".',
          'options': ['Call Rina back', 'Wait quietly', 'Cancel and forget', 'Send a letter'],
          'q': 'What should the customer do if Friday is too late?',
          'type': 'mcq'}],
  'text': "Hello, this is Rina from Sinar Print. I'm calling about your order number 4521. Unfortunately, the posters will be delayed by two days "
          'because of a printer problem. They should be ready on Friday morning.\n'
          "I'm very sorry for the inconvenience. If Friday is too late, please call me back on 0812-9876-5432 and we will find another solution. "
          'Thank you, and have a nice day.',
  'title': 'A Voicemail'}]
