from ub import *
C = ['The test is on {Monday}.', 'Please open your {books}.', 'The bell {rings} at ten.', 'Our teacher is {kind}.', 'I forgot my {homework}.', 'The library is {closed} today.', 'We have an English {lesson} now.', 'He sits in the {front} row.']
X3 = dict(practice=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[:6]], quiz=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[6:]])
