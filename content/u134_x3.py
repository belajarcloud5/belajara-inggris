from ub import *
C = ['Hello! My name {is} Rani.', 'I am {twelve} years old.', 'Today is {Tuesday}.', "It is {nine} o'clock.", 'This pen is {three} dollars.', 'My phone number is zero {eight}.', 'Nice to {meet} you.', 'She is from {Bali}.']
X3 = dict(practice=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[:6]], quiz=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[6:]])
