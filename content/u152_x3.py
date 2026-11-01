from ub import *
sets = [
 (["My cousin lives in Bandung.", "He have a small shop.", "He sells books and pens.", "Many students visit his shop."], 1, "He has."),
 (["We went to the zoo yesterday.", "The monkeys was very funny.", "We took many photographs.", "Then we ate ice cream."], 1, "monkeys were."),
 (["There are three eggs in the fridge.", "There is some milk too.", "There is two oranges on the table.", "I will make breakfast."], 2, "There are two oranges."),
 (["Dina can plays the piano.", "She practises every day.", "Her teacher is proud of her.", "She wants to join a contest."], 0, "can play."),
 (["I'm reading an interesting book.", "It tell a story about a pilot.", "The pilot flies across the sea.", "I can't stop reading."], 1, "It tells."),
 (["The weather was terrible last week.", "It rain every day.", "We stayed at home.", "We played board games."], 1, "It rained."),
 (["Tom has a brother and a sister.", "His brother is older than him.", "His sister are very kind.", "They live in Medan."], 2, "His sister is."),
 (["I need an umbrella today.", "It is going to rain.", "My mother buy a new one yesterday.", "I will take it with me."], 2, "bought."),
]
X3 = dict(practice=[spot(i, a, e) for i, a, e in sets], quiz=[spot(i, a, e) for i, a, e in sets[:3]])
