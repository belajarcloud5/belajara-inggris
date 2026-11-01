from ub import *
sets = [
 (["She is interested on science.", "She reads about space every night.", "She wants to be an astronaut.", "Her parents support her."], 0, "interested in."),
 (["He apologised for being late.", "He explained that the bus broke down.", "I suggested him to call next time.", "He promised to do that."], 2, "suggested that he call."),
 (["The more I practise, the better I get.", "The more I read, the more words I know.", "The most I listen, the easier it is.", "That's why I study every day."], 2, "The more I listen."),
 (["I have lived in Jakarta since 2018.", "I have worked here for three years.", "I have went to Bali twice.", "I love travelling."], 2, "have been/gone."),
 (["If I will have time, I will visit you.", "I miss you a lot.", "We can have dinner together.", "Please call me."], 0, "If I have time."),
 (["The students has finished the test.", "The teacher collected the papers.", "She marked them in the evening.", "The results are on the board."], 0, "have finished."),
 (["This is the girl who won the prize.", "This is the house which I bought.", "That is the man whose car was stolen.", "There is the book who is on the table."], 3, "the book that is on the table."),
 (["He asked me what was my name.", "I told him my name.", "He wrote it down.", "We shook hands."], 0, "what my name was."),
]
X3 = dict(practice=[spot(i, a, e) for i, a, e in sets], quiz=[spot(i, a, e) for i, a, e in sets[:3]])
