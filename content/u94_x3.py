from ub import *
def w(word, opts): return listen("Dengarkan. Kata mana yang kamu dengar?", word, opts, 0, f"Kata yang diucapkan: {word}.")
X3 = dict(practice=[w(a, b) for a, b in [
 ("jumped", ["jumped", "jump", "jumps"]), ("loved", ["loved", "love", "loves"]), ("raised", ["raised", "raise", "raises"]), ("laughed", ["laughed", "laugh", "laughs"]),
 ("kisses", ["kisses", "kiss", "kissed"]), ("cooks", ["cooks", "cook", "cooked"]), ("dreams", ["dreams", "dream", "dreamed"]), ("pushed", ["pushed", "push", "pushes"]),
 ("added", ["added", "add", "adds"]), ("hated", ["hated", "hate", "hates"]), ("tried", ["tried", "try", "tries"]), ("roses", ["roses", "rose", "rows"])]], quiz=[])
X3["practice"] += mk([
 ('Akhiran -s pada "laughs" dibaca...', '/s/', '/z/', '/ɪz/', '/f/', 'F tanpa getar.'),
 ('Akhiran -s pada "dreams" dibaca...', '/z/', '/s/', '/ɪz/', '/ms/', 'M bergetar.'),
 ('Akhiran -s pada "kisses" dibaca...', '/ɪz/', '/s/', '/z/', '/ses/', 'S desis.'),
 ('Akhiran -s pada "cups" dibaca...', '/s/', '/z/', '/ɪz/', '/ps/', 'P tanpa getar.'),
 ('Akhiran -s pada "pens" dibaca...', '/z/', '/s/', '/ɪz/', '/ns/', 'N bergetar.'),
 ('Akhiran -ed pada "jumped" dibaca...', '/t/', '/d/', '/ɪd/', '/ped/', 'P tanpa getar.'),
 ('Akhiran -ed pada "loved" dibaca...', '/d/', '/t/', '/ɪd/', '/ved/', 'V bergetar.'),
 ('Akhiran -ed pada "pushed" dibaca...', '/t/', '/d/', '/ɪd/', '/shed/', 'Sh tanpa getar.'),
 ('Akhiran -ed pada "added" dibaca...', '/ɪd/', '/t/', '/d/', '/ded/', 'D → /ɪd/.'),
 ('Akhiran -ed pada "tried" dibaca...', '/d/', '/t/', '/ɪd/', '/ied/', 'Vokal → /d/.'),
 ('Akhiran -ed pada "hated" dibaca...', '/ɪd/', '/t/', '/d/', '/ted/', 'T → /ɪd/.'),
 ('Kata mana yang akhirannya BERBEDA?', 'roses', 'cups', 'cats', 'books', 'Roses /ɪz/; lainnya /s/.'),
 ('Kata mana yang akhirannya BERBEDA?', 'tried', 'pushed', 'jumped', 'laughed', 'Tried /d/; lainnya /t/.'),
 ('Kata mana yang akhirannya BERBEDA?', 'hated', 'loved', 'cleaned', 'played', 'Hated /ɪd/; lainnya /d/.'),
 ('Berapa suku kata "added"?', '2', '1', '3', '4', 'Ad-ded.'),
 ('Berapa suku kata "roses"?', '2', '1', '3', '4', 'Ro-ses.'),
])
X3["quiz"] = [w("pushed", ["pushed", "push", "pushes"])] + mk([
 ('Akhiran -s pada "pens" dibaca...', '/z/', '/s/', '/ɪz/', '/ns/', 'N bergetar.'),
 ('Akhiran -ed pada "hated" dibaca...', '/ɪd/', '/t/', '/d/', '/ted/', 'T → /ɪd/.'),
 ('Akhiran -ed pada "jumped" dibaca...', '/t/', '/d/', '/ɪd/', '/ped/', 'P tanpa getar.'),
 ('Berapa suku kata "roses"?', '2', '1', '3', '4', 'Ro-ses.'),
 ('Kata mana yang akhirannya BERBEDA?', 'roses', 'cups', 'cats', 'books', 'Roses /ɪz/.'),
 ('Akhiran -s pada "laughs" dibaca...', '/s/', '/z/', '/ɪz/', '/f/', 'F tanpa getar.'),
 ('Kata mana yang akhirannya BERBEDA?', 'tried', 'pushed', 'jumped', 'laughed', 'Tried /d/.'),
])
