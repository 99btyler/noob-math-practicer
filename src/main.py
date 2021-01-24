from random import choice


def get_decision(question, options):
	for i in range(len(options)):
		print(f"{i}. '{options[i]}'")
	print(question)
	# Get decision
	while True:
		# - make sure it's a number
		try:
			decision = int(input("Enter number: "))
		except ValueError:
			continue
		# - make sure it's valid
		if decision >= 0 and decision < len(options):
			break
	return options[decision]


topic_options = ["addition", "subtraction", "multiplication", "division"]
difficulty_options = ["easy", "medium"]

print("\n----")
print("noob-math-practicer")
topic = get_decision("Which one do you want to practice?", topic_options)
print("----")
difficulty = get_decision("Which difficulty do you want?", difficulty_options)
print("----\n")

# Factor in difficulty
range = None
if difficulty == difficulty_options[0]:
	range = [2, 5, 10, 11]
elif difficulty == difficulty_options[1]:
	range = [3, 4, 6, 7, 8, 9, 12]

# Start quiz
correct_answers = 0
while correct_answers < 10:
	# make the constants
	constant1 = choice(range)
	constant2 = choice(range)
	# build the question/answer
	question = None
	answer = None
	# 'addition'
	if topic == topic_options[0]:
		question = f"{constant1}+{constant2}="
		answer = constant1 + constant2
	# 'subtraction'
	if topic == topic_options[1]:
		if constant2 > constant1:
			i = constant1
			constant1 = constant2
			constant2 = i
		question = f"{constant1}-{constant2}="
		answer = constant1 - constant2
	# 'multiplication'
	if topic == topic_options[2]:
		question = f"{constant1}*{constant2}="
		answer = constant1 * constant2
	# 'division'
	if topic == topic_options[3]:
		i = constant1 * constant2
		question = f"{i}/{constant2}="
		answer = constant1
	# ask the question, get the guess
	while True:
		# - make sure guess is a number
		while True:
			try:
				guess = int(input(question))
				break
			except ValueError:
				print("error: number is required")
		# - make sure guess is correct
		if guess == answer:
			correct_answers += 1
			print("Correct\n")
			break
		else:
			print("WRONG!")

