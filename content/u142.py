from ub import *
from ielts_h import rstory
UNIT = vocab_unit("u142",
 ["membaca **cerita sangat pendek** (4 sampai 6 kalimat)",
  "mengenali **kata dasar**: warna, hewan, kata kerja sederhana",
  "menjawab **pertanyaan pemahaman** sederhana",
  "memakai popup kata untuk membantu membaca"],
 "Tahap 1 berisi cerita sangat pendek dengan kata-kata dasar. Baca ceritanya di tab **Bacaan**, klik kata yang belum kamu kenal, lalu jawab pertanyaannya. Di sini kamu belajar kata-kata kuncinya dulu.",
 [("Kata-kata cerita tahap 1", [
   ("cat", "kucing", "My cat is small and white."), ("dog", "anjing", "The dog runs in the park."), ("ball", "bola", "Tom has a red ball."),
   ("big", "besar", "The ball is big."), ("small", "kecil", "She is small and white."), ("run", "berlari", "The dog likes to run."),
   ("eat", "makan", "The cat eats fish."), ("sleep", "tidur", "She sleeps on my bed."), ("sun", "matahari", "The sun is hot today."),
   ("happy", "senang", "They are happy."), ("friend", "teman", "Dina is my friend."), ("park", "taman", "We play in the park.")])],
 "Dialog: Anjingku",
 [("Tom", "Look! This is my dog.", "Lihat! Ini anjingku."), ("Dina", "He is big! What is his name?", "Besar sekali! Siapa namanya?"), ("Tom", "His name is Max. He likes to run.", "Namanya Max. Dia suka berlari."), ("Dina", "Can I play with him?", "Boleh aku bermain dengannya?")],
 "Baca setiap cerita dua kali: pertama untuk gambaran, kedua sambil mengetuk kata baru.", seed=142)
READ = [
 rstory("The Red Ball", "Tahap 1", "Tom has a red ball. The ball is big. He plays with his dog. The dog runs and runs. Tom is happy.",
  "Tom punya bola merah. Bolanya besar. Dia bermain dengan anjingnya. Anjing itu berlari dan berlari. Tom senang.",
  [("What colour is the ball?", "Red", "Blue", "White", "Green", "Bola merah."), ("Who plays with Tom?", "His dog", "His cat", "His sister", "His teacher", "Dengan anjingnya."), ("How is Tom?", "Happy", "Sad", "Angry", "Tired", "Tom senang.")], [],
  [("Tom punya bola merah.", "Tom has a ___ ball.", "red", "A red ball."), ("Anjing itu berlari.", "The dog ___ and runs.", "runs", "Runs and runs.")]),
 rstory("My Cat", "Tahap 1", "I have a cat. Her name is Mimi. She is small and white. Mimi eats fish. She sleeps on my bed.",
  "Aku punya kucing. Namanya Mimi. Dia kecil dan putih. Mimi makan ikan. Dia tidur di tempat tidurku.",
  [("What is the cat's name?", "Mimi", "Max", "Milo", "Momo", "Namanya Mimi."), ("What does Mimi eat?", "Fish", "Rice", "Meat", "Bread", "Makan ikan."), ("Where does Mimi sleep?", "On the bed", "In the box", "On the chair", "In the garden", "Di tempat tidur.")], [],
  [("Mimi kecil dan putih.", "Mimi is small and ___.", "white", "White."), ("Mimi makan ikan.", "Mimi ___ fish.", "eats", "Eats fish.")]),
 rstory("A Sunny Day", "Tahap 1", "It is a sunny day. The sun is hot. Dina and Rani go to the park. They play and eat ice cream. They are happy.",
  "Hari ini cerah. Matahari panas. Dina dan Rani pergi ke taman. Mereka bermain dan makan es krim. Mereka senang.",
  [("How is the weather?", "Sunny", "Rainy", "Cold", "Windy", "Cerah."), ("Where do Dina and Rani go?", "To the park", "To school", "To the market", "To the beach", "Ke taman."), ("What do they eat?", "Ice cream", "Fried rice", "Noodles", "Cake", "Es krim.")], [],
  [("Matahari panas.", "The sun is ___.", "hot", "The sun is hot."), ("Mereka pergi ke taman.", "They go to the ___.", "park", "To the park.")]),
]
