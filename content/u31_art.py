from qk import mk, mkf, mko
ART = dict(practice=mk([
 ('Pilih article yang tepat: "Once upon a time, there was ___ king."', "a", "an", "the", "no article", "Pertama disebut → a."),
 ('Pilih article yang tepat: "A boy found a cave. He went into ___ cave."', "the", "a", "an", "no article", "Gua yang sudah disebut → the."),
 ('Pilih article yang tepat: "___ sun was setting when he left the forest."', "The", "A", "An", "No article", "Benda unik → the."),
 ('Pilih article yang tepat: "Long ago, there lived ___ old woman in a village."', "an", "a", "the", "no article", "old diawali vokal → an."),
 ('Pilih article yang tepat: "Arya lived in ___ Java."', "no article", "the", "a", "an", "Nama tempat tanpa article."),
]) + mkf([
 ("Dahulu ada seorang pangeran.", "Once upon a time, there was ___ prince.", "a", "Pertama disebut → a."),
 ("Pangeran itu baik hati. (sudah disebut sebelumnya)", "___ prince was kind.", "The", "Sudah disebut → the."),
 ("Ada seekor naga di gua itu.", "There was ___ dragon in the cave.", "a", "Pertama disebut → a."),
]) + mko([
 ("Ada seorang raja di desa itu.", "There was a king in the village.", "an", ""),
]), quiz=mk([
 ('Pilih article yang tepat: "She had ___ apple. She gave the apple to the boy."', "an", "a", "the", "no article", "Pertama disebut dan diawali vokal → an."),
 ('Pilih article yang tepat: "The mouse ran away. ___ lion woke up."', "The", "A", "An", "No article", "Singa yang tertentu dalam cerita → the."),
]))
