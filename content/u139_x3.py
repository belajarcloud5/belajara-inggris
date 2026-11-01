from ub import *
C = ["I'm calling about your {order}.", 'Please leave a {message}.', 'I will call you {back}.', 'The line is {busy}.', 'Can I {speak} to Mr. Adi?', 'He is not {available}.', 'My number is {zero} eight one.', 'Thank you for {calling}.']
X3 = dict(practice=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[:6]], quiz=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[6:]])
