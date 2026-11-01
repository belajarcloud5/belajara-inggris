from ub import *
C = ['Turn {left} at the corner.', 'The bus stop is {opposite} the bank.', 'The train leaves at {nine}.', 'Go {straight} for two blocks.', 'The station is {near} here.', 'My flight is {delayed}.', 'Take the {second} street on the right.', 'We arrived at the {airport}.']
X3 = dict(practice=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[:6]], quiz=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[6:]])
