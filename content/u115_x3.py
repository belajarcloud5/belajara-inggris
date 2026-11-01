from ub import *
def q2(question, ans, w1, w2, exp):
    return listen('Dengarkan pertanyaan. Pilih jawaban terbaik.', question, [ans, w1, w2], 0, exp)
X3 = dict(practice=[
 q2('Where did you put the keys?', 'On the kitchen table.', 'At six o\'clock.', 'Yes, I did.', 'Where → tempat.'),
 q2('When is the next flight to Bali?', 'At two thirty.', 'It is very fast.', 'In the departure hall.', 'When → waktu.'),
 q2('Who will lead the training session?', 'Ms. Sari will.', 'Next Tuesday.', 'In Room B.', 'Who → orang.'),
 q2('Why is the store closed today?', 'It is a national holiday.', 'At the mall.', 'About two hours.', 'Why → alasan.'),
 q2('How often do you check your email?', 'Every morning.', 'In the office.', 'It is very long.', 'How often → frekuensi.'),
 q2('How many copies do you need?', 'Ten, please.', 'On the desk.', 'Yes, I do.', 'How many → jumlah.'),
 q2('Do you know when the bank opens?', 'At nine, I think.', 'Yes, it is a big bank.', 'It is near the park.', 'Indirect question.'),
 q2('Isn\'t the meeting at three?', 'No, it was moved to four.', 'In the conference room.', 'I have a meeting.', 'Negative question.'),
 q2('Would you rather take the bus or the train?', 'The train is faster.', 'Yes, I would.', 'At the station.', 'Pilihan.'),
 q2('Could you send me the schedule?', 'Of course, I\'ll do it now.', 'It is on Monday.', 'I like the schedule.', 'Permintaan.'),
 q2('Let\'s order some coffee.', 'Good idea.', 'It is hot.', 'At the cafe.', 'Saran.'),
 q2('Which printer is broken?', 'The one on the second floor.', 'At eleven o\'clock.', 'Yes, it is.', 'Which → pilihan.'),
 q2('Why don\'t we take a short break?', 'That sounds good.', 'On the second floor.', 'About ten dollars.', 'Saran.'),
 q2('What time does the bus leave?', 'In ten minutes.', 'To the station.', 'It is a long bus.', 'What time.'),
 q2('Who called me this morning?', 'Mr. Adi did.', 'At nine.', 'In my office.', 'Who.'),
 q2('Where can I find a taxi?', 'Outside the main entrance.', 'It costs ten dollars.', 'I took a taxi.', 'Where.'),
 q2('Has the order arrived yet?', 'Not yet, but it should come today.', 'Yes, it is an order.', 'In the warehouse.', 'Present perfect.'),
 q2('You work in the finance department, right?', 'No, I\'m in marketing.', 'At the bank.', 'It is very big.', 'Tag question.'),
], quiz=[
 q2('How long will the repair take?', 'About two days.', 'In the garage.', 'It is broken.', 'How long.'),
 q2('When did you arrive?', 'Yesterday evening.', 'At the hotel.', 'By taxi.', 'When.'),
 q2('Where is the nearest pharmacy?', 'Across the street.', 'At eight.', 'Yes, it is.', 'Where.'),
 q2('Would you like some water?', 'Yes, please.', 'It is cold.', 'In the glass.', 'Tawaran.'),
 q2('Who is the new manager?', 'Ms. Lopez.', 'On Monday.', 'In the office.', 'Who.'),
 q2('Why was the flight cancelled?', 'Because of a storm.', 'At gate six.', 'About two hours.', 'Why.'),
 q2('How do I get to the museum?', 'Take bus number five.', 'It is very old.', 'At ten.', 'How.'),
 q2('Can I borrow your pen?', 'Sure, here you are.', 'It is blue.', 'On the table.', 'Permintaan.'),
])
