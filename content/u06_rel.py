from qk import mk, mkf, mko
REL = dict(practice=mk([
 ('Pilih kata yang tepat: "I have a friend ___ is very tall."', "who", "which", "whose", "where", "Orang → who."),
 ('Pilih kata yang tepat: "This is the bag ___ is blue."', "which", "who", "whose", "where", "Benda → which."),
 ('Pilih kata yang tepat: "The boy ___ wears glasses is my brother."', "who", "which", "where", "whose", "Orang → who."),
 ('Pilih kata yang tepat: "The cat ___ has a long tail is mine."', "which", "who", "whose", "where", "Hewan → which."),
 ('Pilih kata yang tepat: "The girl ___ sits next to me is kind."', "who", "which", "whose", "where", "Orang → who."),
 ('Pilih kalimat yang benar:', "The girl who is tall is my sister.", "The girl who she is tall is my sister.", "The girl which is tall is my sister.", "The girl is who tall is my sister.", "Jangan mengulang she; orang → who."),
 ('Pilih kalimat yang SALAH:', "The book who is on the table is mine.", "The book which is on the table is mine.", "The book that is on the table is mine.", "I like the book which is red.", "Benda → which atau that, bukan who."),
 ('Pilih kalimat yang SALAH:', "The man who he lives here is kind.", "The man who lives here is kind.", "The man that lives here is kind.", "I know the man who lives here.", "Jangan mengulang he."),
]) + mkf([
 ("Aku punya teman yang sangat tinggi.", "I have a friend ___ is very tall.", "who/that", "Orang → who atau that."),
 ("Ini tas yang berwarna biru.", "This is the bag ___ is blue.", "which/that", "Benda → which atau that."),
 ("Anak yang memakai kacamata itu adikku.", "The boy ___ wears glasses is my brother.", "who/that", "Orang → who atau that."),
 ("Kucing yang punya ekor panjang itu milikku.", "The cat ___ has a long tail is mine.", "which/that", "Hewan → which atau that."),
]), quiz=mk([
 ('Pilih kata yang tepat: "The woman ___ teaches us English is kind."', "who", "which", "whose", "where", "Orang → who."),
 ('Pilih kata yang tepat: "I like the shoes ___ are new."', "which", "who", "whose", "where", "Benda → which."),
 ('Pilih kalimat yang SALAH:', "The dog who barks is loud.", "The dog which barks is loud.", "The dog that barks is loud.", "I hear the dog which barks.", "Hewan → which/that."),
]) + mkf([
 ("Gadis yang tinggi itu temanku.", "The girl ___ is tall is my friend.", "who/that", "Orang → who atau that."),
]))
