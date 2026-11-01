from ub import *
C = ['Today we will {discuss} a new topic.', 'This is {important} because it saves energy.', 'For {example}, plants need sunlight.', 'However, some people {disagree}.', 'In {conclusion}, practice is useful.', 'The study {shows} a clear pattern.', 'The main {idea} is simple.', 'Researchers {found} that sleep matters.']
X3 = dict(practice=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[:6]], quiz=[cloze(c, 'Kalimat lengkapnya diputar ulang.') for c in C[6:]])
