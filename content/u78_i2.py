from ielts_h import tfn
A = "The city library opened in 1998. It has more than 50,000 books and a children's section on the second floor. Members can borrow up to five books for two weeks. The library is closed on Sundays."
B = "Solar panels convert sunlight into electricity. In 2010 only 2 percent of households in the town used them, but by 2020 the figure had risen to 18 percent. Experts say the main reason is falling prices. Some residents, however, worry that panels are difficult to clean."
C = "Most adults need seven to nine hours of sleep. A study of 500 students found that those who slept eight hours scored higher in tests than those who slept five hours. The researchers did not study the effect of exercise. Caffeine is known to make falling asleep harder."
D = "Bamboo grows very quickly, and some types can grow almost one metre in a day. It is used to make furniture, paper, and floors. Many farmers like bamboo because it needs little water. However, it can spread into nearby fields if it is not controlled."
I2 = dict(practice=tfn(A, [
 ("The library opened in the 1990s.", 'T', "1998 termasuk tahun 1990-an."),
 ("The library has more than 60,000 books.", 'F', "Teks: more than 50,000."),
 ("The children's section is on the ground floor.", 'F', "Teks: second floor."),
 ("Members can borrow ten books.", 'F', "Teks: up to five books."),
 ("The library is closed on Sundays.", 'T', "Teks menyebutnya langsung."),
 ("The library offers free internet.", 'N', "Internet tidak disebut."),
 ("Members can keep books for a month.", 'F', "Teks: two weeks.")]) + tfn(B, [
 ("Solar panels turn sunlight into electricity.", 'T', "convert = mengubah."),
 ("In 2010 fewer than 5 percent of households used panels.", 'T', "2 percent < 5 percent."),
 ("By 2020 more than 25 percent used panels.", 'F', "Teks: 18 percent."),
 ("Experts say falling prices are the main reason.", 'T', "Disebut langsung."),
 ("The government pays part of the cost of panels.", 'N', "Tidak disebut."),
 ("All residents are happy with the panels.", 'F', "Some residents worry."),
 ("Some residents think panels are hard to clean.", 'T', "difficult to clean.")]) + tfn(C, [
 ("Adults need at least ten hours of sleep.", 'F', "Teks: seven to nine."),
 ("The study included 500 students.", 'T', "Disebut langsung."),
 ("Students who slept five hours scored higher.", 'F', "Yang tidur delapan jam lebih tinggi."),
 ("The researchers studied the effect of exercise.", 'F', "Teks: did not study."),
 ("Caffeine can make it harder to fall asleep.", 'T', "Disebut langsung."),
 ("The study was carried out in 2019.", 'N', "Tahun tidak disebut."),
 ("Teenagers need more sleep than adults.", 'N', "Tidak dibandingkan.")]),
 quiz=tfn(D, [
 ("Bamboo can grow almost a metre in one day.", 'T', "Disebut langsung."),
 ("Bamboo is only used to make paper.", 'F', "Furniture, paper, floors."),
 ("Bamboo needs a lot of water.", 'F', "Teks: little water."),
 ("Bamboo is cheaper than wood.", 'N', "Harga tidak dibandingkan."),
 ("Bamboo may spread into nearby fields.", 'T', "can spread."),
 ("Farmers in Asia grow the most bamboo.", 'N', "Tidak disebut.")]))
