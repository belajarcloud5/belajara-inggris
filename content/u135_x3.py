from ub import *
C = ['My mother is a {teacher}.', 'We have a small {garden}.', 'He {wakes} up at six.', 'The cat is {under} the table.', 'My sister {helps} in the kitchen.', 'I {brush} my teeth every night.', 'The window is {open}.', 'We eat dinner at {seven}.']
X3 = dict(practice=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[:6]], quiz=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[6:]])
