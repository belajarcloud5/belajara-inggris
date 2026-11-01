from ub import *
C = ['The city will build a new {bridge}.', 'Heavy rain is {expected} tomorrow.', 'The company {announced} new prices.', 'Scientists have {found} a new planet.', 'The festival {begins} on Friday.', 'Many people {attended} the concert.', 'The temperature will {rise} slowly.', 'The mayor {opened} the library.']
X3 = dict(practice=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[:6]], quiz=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[6:]])
