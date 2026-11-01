from ub import *
C = ["I'd like a glass of {water}.", 'The shirt is {twenty} dollars.', 'She bought some {apples}.', 'Do you have a {larger} size?', 'The bill is {fifteen} dollars.', 'I will pay by {card}.', 'The soup is {hot}.', 'We need two {kilos} of rice.']
X3 = dict(practice=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[:6]], quiz=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[6:]])
