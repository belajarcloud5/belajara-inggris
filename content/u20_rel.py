from qk import mk, mkf, mko
REL = dict(practice=mk([
 ('Pilih kata yang tepat: "A tiger is a big cat ___ lives in Asia."', "that", "who", "whose", "where is", "Hewan → that/which."),
 ('Pilih kata yang tepat: "A farmer is a person ___ grows crops."', "who", "which", "whose", "where", "Orang → who."),
 ('Pilih kata yang tepat: "A whale is an animal ___ breathes air."', "which", "who", "whose", "where", "Hewan → which."),
 ('Pilih kata yang tepat: "A doctor is a person ___ treats patients."', "who", "which", "whose", "where", "Orang → who."),
 ('Pilih kalimat definisi yang benar:', "A volcano is a mountain which erupts.", "A volcano is a mountain who erupts.", "A volcano is mountain which erupts.", "A volcano is a mountain erupts which.", "Benda → which."),
 ('Pilih kalimat definisi yang SALAH:', "A teacher is a person which teaches students.", "A teacher is a person who teaches students.", "A teacher is a person that teaches students.", "A tiger is a cat which lives in Asia.", "Orang → who atau that, bukan which."),
 ('Pilih kalimat definisi yang SALAH:', "A bird is an animal who can fly.", "A bird is an animal which can fly.", "A bird is an animal that can fly.", "A farmer is a person who grows rice.", "Hewan → which/that."),
]) + mkf([
 ("Harimau adalah kucing besar yang hidup di Asia.", "A tiger is a big cat ___ lives in Asia.", "that/which", "Hewan → that atau which."),
 ("Petani adalah orang yang menanam padi.", "A farmer is a person ___ grows rice.", "who/that", "Orang → who atau that."),
 ("Paus adalah hewan yang bernapas dengan udara.", "A whale is an animal ___ breathes air.", "which/that", "Hewan → which atau that."),
 ("Dokter adalah orang yang merawat pasien.", "A doctor is a person ___ treats patients.", "who/that", "Orang → who atau that."),
]), quiz=mk([
 ('Pilih kata yang tepat: "A pilot is a person ___ flies planes."', "who", "which", "whose", "where", "Orang → who."),
 ('Pilih kata yang tepat: "An eagle is a bird ___ hunts small animals."', "which", "who", "whose", "where", "Hewan → which."),
 ('Pilih kalimat yang SALAH:', "A chef is a person which cooks food.", "A chef is a person who cooks food.", "A chef is a person that cooks food.", "A cook is someone who makes meals.", "Orang → who/that."),
]) + mkf([
 ("Gunung berapi adalah gunung yang meletus.", "A volcano is a mountain ___ erupts.", "which/that", "Benda → which atau that."),
]))
