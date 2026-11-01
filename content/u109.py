from ub import *
UNIT = vocab_unit("u109",
 ["mempelajari kosakata **olahraga, musik, film, dan permainan**",
  "menyebut **kegiatan waktu luang** dalam bahasa Inggris",
  "mengenali kata melalui **arti, ejaan, dan pendengaran**",
  "memakai pola *I enjoy ...ing* dan *My favourite ... is ...*"],
 "Percakapan sehari-hari sering membahas hobi dan hiburan. Pelajari kata berikut dan pola **I enjoy playing football** serta **My favourite film is ...**",
 [("Olahraga", [
   ("football", "sepak bola", "We play football on Sunday."), ("badminton", "bulu tangkis", "He plays badminton every week."), ("swimming", "berenang", "Swimming is good exercise."),
   ("running", "berlari", "She likes running in the morning."), ("cycling", "bersepeda", "Cycling is fun."), ("match", "pertandingan", "The match starts at six."),
   ("team", "tim", "Our team won."), ("coach", "pelatih", "The coach is strict.")]),
  ("Musik dan film", [
   ("song", "lagu", "This song is my favourite."), ("singer", "penyanyi", "The singer is famous."), ("guitar", "gitar", "He plays the guitar."),
   ("concert", "konser", "We went to a concert."), ("film", "film", "We watched a funny film."), ("actor", "aktor", "The actor is very tall."),
   ("cinema", "bioskop", "Let's go to the cinema."), ("comedy", "komedi", "I like comedy films.")]),
  ("Permainan dan waktu luang", [
   ("game", "permainan", "This game is difficult."), ("puzzle", "teka-teki", "She does a puzzle."), ("chess", "catur", "My father plays chess."),
   ("hobby", "hobi", "My hobby is drawing."), ("collect", "mengoleksi", "He collects stamps."), ("draw", "menggambar", "She likes to draw animals."),
   ("camping", "berkemah", "We went camping last week."), ("gardening", "berkebun", "Gardening is her hobby.")])],
 "Dialog: Apa hobimu?",
 [("Dina", "What is your hobby, Tom?", "Apa hobimu, Tom?"), ("Tom", "I enjoy playing football and listening to songs.", "Aku suka bermain sepak bola dan mendengarkan lagu."),
  ("Dina", "Who is your favourite singer?", "Siapa penyanyi favoritmu?"), ("Tom", "I like many singers. What about you?", "Aku suka banyak penyanyi. Kalau kamu?"),
  ("Dina", "I love drawing and watching films.", "Aku suka menggambar dan menonton film."), ("Tom", "Let's go to the cinema this weekend!", "Ayo ke bioskop akhir pekan ini!")],
 "Buat daftar hobimu dalam bahasa Inggris dan tempelkan di dinding: *I enjoy ...ing*. Setiap minggu tambah satu kata baru yang terkait hobimu.", seed=109)
