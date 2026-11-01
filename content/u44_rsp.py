from qk import mk, mkf, mko
RSP = dict(practice=mk([
 ('Ubah: "Why do you want this job?" → She asked me why I ___ that job.', "wanted", "want", "do want", "did want", "Urutan berita + past."),
 ('Ubah: "Can you start next week?" → She asked ___ I could start the next week.', "if", "that", "what", "do", "Ya/tidak → if atau whether."),
 ('Ubah: "Have you worked abroad?" → She asked whether I ___ worked abroad.', "had", "have", "did", "was", "present perfect → past perfect."),
 ('Ubah: "Where do you live?" → She asked me where I ___.', "lived", "did live", "live do", "do live", "Urutan berita, tanpa do."),
 ('Pilih kalimat yang benar:', "She asked where I lived.", "She asked where did I live.", "She asked where I do live.", "She asked where lived I.", "Tanpa do/did."),
 ('Pilih kalimat yang benar:', "He asked if I was ready.", "He asked that I was ready.", "He asked was I ready.", "He asked if was I ready.", "Ya/tidak → if."),
 ('Pilih kalimat yang SALAH:', "She asked what was my weakness.", "She asked what my weakness was.", "She asked me what I thought.", "She asked whether I could work late.", "Urutan berita: what my weakness was."),
 ('Pilih kalimat yang SALAH:', "He asked me did I like the job.", "He asked me if I liked the job.", "He asked me whether I liked the job.", "He asked me why I liked the job.", "Ya/tidak → if atau whether."),
]) + mkf([
 ("Dia bertanya mengapa aku menginginkan pekerjaan itu.", "She asked me why I ___ that job.", "wanted", "Urutan berita + past."),
 ("Dia bertanya apakah aku bisa mulai minggu depan.", "She asked ___ I could start next week.", "if/whether", "if atau whether."),
 ("Dia bertanya di mana aku tinggal.", "She asked me where I ___.", "lived", "Urutan berita + past."),
 ("Dia bertanya apakah aku sudah bekerja di luar negeri.", "She asked whether I ___ worked abroad.", "had", "present perfect → past perfect."),
]), quiz=mk([
 ('Ubah: "What is your name?" → He asked me what my name ___.', "was", "is", "did", "do", "Urutan berita + past."),
 ('Ubah: "Do you like coffee?" → He asked me ___ I liked coffee.', "if", "that", "do", "what", "Ya/tidak → if."),
 ('Pilih kalimat yang SALAH:', "She asked me where did I work.", "She asked me where I worked.", "She asked me if I worked there.", "She asked me what I did.", "Urutan berita, tanpa did."),
]) + mkf([
 ("Dia bertanya apa kelemahanku.", "She asked what my weakness ___.", "was", "Urutan berita + past."),
]))
