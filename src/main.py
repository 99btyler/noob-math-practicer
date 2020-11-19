from random import choice


class Quiz():

	def __init__(self):

		self.correct_answers = 0

		self.operator = None

		self.difficulty = None
		self.easy_range = [2, 5, 10, 11]
		self.medium_range = [3, 4, 6, 7, 8, 9, 12]

		self.__setup()

	def __setup(self):
		print("\n----")
		print("noob-math-practicer")
		print("1. addition")
		print("2. subtraction")
		print("3. multiplication")
		print("4. division")
		while True:
			# Get decision and make sure it's a number
			try:
				decision = int(input("Enter number to start: "))
			except ValueError:
				continue
			# Check if decision is valid
			if decision == 1:
				self.operator = "ADDITION"
				break
			elif decision == 2:
				self.operator = "SUBTRACTION"
				break
			elif decision == 3:
				self.operator = "MULTIPLICATION"
				break
			elif decision == 4:
				self.operator = "DIVISION"
				break
			else:
				print("error: not an option")
		print("----")
		print("1. easy")
		print("2. medium")
		while True:
			# Get decision and make sure it's a number
			try:
				decision = int(input("Enter number to start: "))
			except ValueError:
				continue
			# Check if decision is valid
			if decision == 1:
				self.difficulty = "EASY"
				break
			elif decision == 2:
				self.difficulty = "MEDIUM"
				break
			else:
				print("error: not an option")
		print("----")
		print(f"Starting {self.operator} quiz on {self.difficulty} level")
		print("")
		self.__build_questions()

	def __build_questions(self):
		while self.correct_answers < 10:
			# Factor in difficulty
			constant1 = None
			constant2 = None
			if self.difficulty == "EASY":
				constant1 = choice(self.easy_range)
				constant2 = choice(self.easy_range)
			elif self.difficulty == "MEDIUM":
				constant1 = choice(self.medium_range)
				constant2 = choice(self.medium_range)
			# Build the question and answer
			question = None
			answer = None
			if self.operator == "ADDITION":
				question = f"{constant1}+{constant2}="
				answer = constant1 + constant2
			if self.operator == "SUBTRACTION":
				if constant2 > constant1:
					i = constant1
					constant1 = constant2
					constant2 = i
				question = f"{constant1}-{constant2}="
				answer = constant1 - constant2
			if self.operator == "MULTIPLICATION":
				question = f"{constant1}*{constant2}="
				answer = constant1 * constant2
			if self.operator == "DIVISION":
				i = constant1 * constant2
				question = f"{i}/{constant2}="
				answer = constant1
			# Ask the question
			if self.__ask_question(question, answer):
				self.correct_answers += 1

	def __ask_question(self, question, answer):
		while True:
			# Receive guess and make sure it's a number
			while True:
				try:
					guess = int(input(question))
					break
				except ValueError:
					print("error: number is required")
			# Check if guess is correct
			if guess == answer:
				print("Correct\n")
				return True
			else:
				print("WRONG!")


quiz = Quiz()