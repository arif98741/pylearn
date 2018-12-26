from Question import Question

question_prompts = [
	"what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
	"what color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
	"what color are straberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
	Question(question_prompts[0],"a"),
	Question(question_prompts[1],"2"),
	Question(question_prompts[2],"b"),
]

def runTest(questions):
	score = 0
	for question in questions:
		answer = input(question.prompt)
		if answer == question.answer:
			score += 1
	print("You got "+str(score)+"/ "+str(len(questions)) + "correct")		

runTest(questions)