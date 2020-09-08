import random


def do_question(question, answer):
	while True:
		try:
			guess = int(input(question))
		except ValueError:
			continue
		if guess == answer:
			return 1


def choice_1():
	print("choice_1: \"Addition 2-9 (when sum > 10)\"")
	corrects = 0
	while True:
		i = random.randint(2, 9)
		ii = random.randint(9-i+2, 9)
		corrects += do_question(f"{i}+{ii}=", i+ii)
		if corrects == 10:
			break

def choice_2():
	print("choice_2: \"Multiplication 1-12 (custom_range)\"")
	corrects = 0
	while True:
		custom_range = [3, 4, 6, 7, 8, 9, 12]
		i = random.choice(custom_range)
		custom_range.remove(i)
		ii = random.choice(custom_range)
		corrects += do_question(f"{i}*{ii}=", i*ii)
		if corrects == 10:
			break

def choice_3():
	print("choice_3: \"Division 1-12 (custom_range)\"")
	corrects = 0
	while True:
		custom_range = [3, 4, 6, 7, 8, 9, 12]
		i = random.choice(custom_range)
		custom_range.remove(i)
		ii = random.choice(custom_range)
		iii = i * ii
		corrects += do_question(f"{iii}/{ii}=", iii//ii)
		if corrects == 10:
			break


print("----")
print("noob-math-practicer")
print("1. Addition 2-9 (when sum > 10)")
print("2. Multiplication 1-12 (custom_range)")
print("3. Division 1-12 (custom_range)")
while True:
	try:
		choice = int(input("Enter number to start: "))
	except ValueError:
		continue
	if choice > 0 and choice <= 3:
		break
print("----")

if choice == 1:
	choice_1()
elif choice == 2:
	choice_2()
elif choice == 3:
	choice_3()

