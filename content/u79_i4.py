from ielts_h import ask
T = "Paragraph A: The invention of the printing press in the fifteenth century made books cheaper and more widely available. Before that, every book was copied by hand, which took months. Paragraph B: As more people learned to read, new ideas spread quickly across Europe. Scientists could share discoveries, and ordinary people could read the news. Paragraph C: Today, digital technology is changing reading again. Many people now read on screens, and some experts worry that this makes it harder to concentrate."
I4 = dict(practice=ask(T, [
 ("Heading terbaik untuk Paragraph A?", "A cheaper way to make books", "The danger of reading from screens", "News that ordinary people can read", "Scientists who live in Europe", "A membahas mesin cetak."),
 ("Heading terbaik untuk Paragraph B?", "How reading spread new ideas", "Hand-copied books", "A problem with concentration", "The first printing press", "B membahas penyebaran gagasan."),
 ("Heading terbaik untuk Paragraph C?", "Reading in the digital age", "Why books became cheap", "The history of Europe", "Learning to copy by hand", "C membahas membaca digital."),
 ("Isian (NO MORE THAN TWO WORDS): 'Before printing, every book was copied ___.'", "by hand", "very slowly by machine", "in a factory", "with computers", "Teks: copied by hand."),
 ("Isian (NO MORE THAN TWO WORDS): 'Scientists could share ___.'", "discoveries", "their homes and books", "newspapers", "the invention", "Teks: share discoveries."),
 ("Isian (NO MORE THAN TWO WORDS): 'Some experts worry about ___.'", "concentration", "the price of books", "printing presses", "reading news", "Teks: harder to concentrate."),
 ("Kata 'widely available' paling dekat dengan...", "mudah didapat banyak orang", "sangat langka dan jarang", "sangat mahal harganya", "hanya untuk para ilmuwan", "Widely available."),
 ("Mengapa heading 'The danger of screens' terlalu sempit untuk Paragraph C?", "C juga membahas pembacaan digital secara umum", "C tidak menyebut layar sama sekali", "C membahas mesin cetak abad kelima belas", "C hanya membahas buku kertas lama", "Heading harus mencakup seluruh paragraf.")]),
 quiz=ask(T, [
 ("Paragraf mana yang menyebut ilmuwan?", "Paragraph B", "Paragraph A", "Paragraph C", "tidak ada", "B menyebut scientists."),
 ("Pilih kata pengisi (NO MORE THAN TWO WORDS): 'New ideas spread ___.'", "quickly", "very quickly and widely", "the Europe", "a book", "Teks: spread quickly."),
 ("Kata 'concentrate' paling dekat dengan...", "memusatkan perhatian", "menyalin", "menjual", "menghafal", "Concentrate = berkonsentrasi."),
 ("Sebuah soal matching heading menanyakan...", "gagasan utama paragraf", "satu kata acak di paragraf", "jumlah kata dalam paragraf", "nama penulis paragraf itu", "Heading = ide utama.")]))
