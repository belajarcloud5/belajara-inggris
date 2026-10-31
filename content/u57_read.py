READ = [{'id': 'Pelanggan: Halo, saya memesan blender minggu lalu, tetapi barangnya tiba dalam keadaan rusak. Saya sangat kecewa.\n'
        'Agen: Saya sangat menyesal mendengarnya, Pak. Saya mengerti betapa menjengkelkannya hal itu. Bisakah Bapak memberikan nomor pesanan? '
        'Pelanggan: 7788. Agen: Terima kasih. Saya bisa mengirim penggantinya hari ini, atau memberikan pengembalian dana penuh. Mana yang Bapak '
        'pilih? Pelanggan: Pengganti, tolong. Agen: Baik. Barang akan tiba dalam tiga hari. Ada hal lain yang bisa saya bantu?',
  'qs': [{'answer': 0,
          'exp': 'Customer: "it arrived broken."',
          'options': ['It arrived broken.', 'It is too small.', 'It is the wrong color.', 'It is late.'],
          'q': 'What is wrong with the blender?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Agent: "a replacement... or a full refund."',
          'options': ['A replacement or a refund',
                      'A discount on the next order only',
                      "A new job at the company's main office",
                      'Nothing, because the company is closed'],
          'q': 'What does the agent offer?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Customer: "A replacement, please."',
          'options': ['A replacement', 'A refund', 'A discount', 'A call back'],
          'q': 'What does the customer choose?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Agent: "within three days."',
          'options': ['Within three days', 'Tomorrow', 'In a month', 'Today'],
          'q': 'When will the replacement arrive?',
          'type': 'mcq'}],
  'text': "Customer: Hello, I ordered a blender last week, but it arrived broken. I'm very disappointed.\n"
          "Agent: I'm so sorry to hear that, sir. I understand how frustrating it must be. Could you give me your order number? Customer: It's 7788. "
          'Agent: Thank you. I can send a replacement today, or I can give you a full refund. Which would you prefer? Customer: A replacement, '
          'please. Agent: Certainly. It will arrive within three days. Is there anything else I can help you with?',
  'title': 'Handling a Complaint'},
 {'id': 'Yth. Ibu Hartono, terima kasih telah menghubungi kami mengenai penginapan Ibu di hotel kami. Kami sungguh menyesal bahwa pendingin ruangan '
        'di kamar Ibu tidak berfungsi dan Ibu tidak segera dipindahkan ke kamar lain.\n'
        'Kami telah berbicara dengan tim pemeliharaan, dan masalahnya sudah diperbaiki. Sebagai tanda itikad baik, kami ingin menawarkan diskon 30 '
        'persen untuk penginapan Ibu berikutnya. Kami menghargai masukan Ibu dan berharap dapat menyambut Ibu lagi. Hormat kami, Manajer Hotel',
  'qs': [{'answer': 0,
          'exp': 'Teks: "the air conditioner in your room did not work".',
          'options': ['The air conditioner did not work.',
                      'The bed was dirty and the sheets were old.',
                      'The room was too small for two guests.',
                      'There was no hot water in the bathroom.'],
          'q': "What was the problem in Mrs. Hartono's room?",
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Teks: "the problem has been fixed."',
          'options': ['It has fixed it.', 'It has ignored it.', 'It has closed the room.', 'It has changed the manager.'],
          'q': 'What has the hotel done about the problem?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Teks: "a 30 percent discount on your next stay."',
          'options': ['A 30 percent discount', 'A free meal', 'A full refund', 'A free upgrade'],
          'q': 'What does the hotel offer?',
          'type': 'mcq'},
         {'answer': 0,
          'exp': 'Permintaan maaf dan bahasa sopan.',
          'options': ['Polite and apologetic',
                      'Angry and complaining about the guest',
                      'Funny and full of jokes about the hotel',
                      'Rude and not interested in the guest'],
          'q': 'What is the tone of the letter?',
          'type': 'mcq'}],
  'text': 'Dear Mrs. Hartono, thank you for contacting us about your hotel stay. We are truly sorry that the air conditioner in your room did not '
          'work and that you were not moved to another room promptly.\n'
          'We have spoken to our maintenance team, and the problem has been fixed. As a gesture of goodwill, we would like to offer you a 30 percent '
          'discount on your next stay. We value your feedback and hope to welcome you again. Sincerely, Hotel Manager',
  'title': 'A Reply to a Complaint'}]
