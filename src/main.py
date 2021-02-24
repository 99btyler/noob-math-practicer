import pygame
from random import randint


class Question():

	def __init__(self):

		self.current_question = "ENTER"

		self.font = pygame.font.SysFont(None, 150)
		self.label = self.font.render(self.current_question, True, color_text)
		self.label_rect = self.label.get_rect(center=(width / 2, height / 2))

		self.topics = ["addition", "subtraction", "multiplication", "division"]
		self.previous_topic = self.topics[0]

	def update(self):
		self.label = self.font.render(self.get_new_question(), True, color_text)
		self.label_rect = self.label.get_rect(center=(width / 2, height / 2))

	def get_new_question(self):

		current_topic = self.previous_topic
		while current_topic == self.previous_topic:
			current_topic = self.topics[randint(0, len(self.topics) - 1)]
		print(f"topic: {current_topic}")

		constant1 = randint(1, 12)
		constant2 = randint(1, 12)

		# 'addition'
		if current_topic == self.topics[0]:
			self.current_question = f"{constant1} + {constant2}"
		# 'subtraction'
		elif current_topic == self.topics[1]:
			if constant2 > constant1:
				i = constant1
				constant1 = constant2
				constant2 = i
			self.current_question = f"{constant1} - {constant2}"
		# 'multiplication'
		elif current_topic == self.topics[2]:
			self.current_question = f"{constant1} x {constant2}"
		# 'division'
		elif current_topic == self.topics[3]:
			i = constant1 * constant2
			self.current_question = f"{i} / {constant2}"

		self.previous_topic = current_topic

		return self.current_question


pygame.init()

color_background = (255, 255, 255)
color_text = (32, 32, 32)

width = 420
height = 180

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("noob-math-practicer")

question = Question()


running = True
while running:

	# EVENTS
	for event in pygame.event.get():

		# 'quit'
		if event.type == pygame.QUIT:
			running = False

		# 'keydown'
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				question.update()

	# DISPLAY
	screen.fill(color_background)
	screen.blit(question.label, question.label_rect)
	pygame.display.flip()

