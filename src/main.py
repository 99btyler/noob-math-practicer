import random

import pygame


class Asker():

	def __init__(self):

		self.color_background = (255, 255, 255)
		self.color_text = (32, 32, 32)
		self.width = 420
		self.height = 180

		self.topics = ["addition", "subtraction", "multiplication", "division"]
		self.current_topic = self.topics[0]

		self.constants = [3, 4, 6, 7, 8, 9, 12]
		self.current_question = ["1 + 1", "2"]
		self.is_asking = True

		# Pygame screen
		pygame.init()
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption("noob-math-practicer")

		# Pygame widgets
		self.font = pygame.font.SysFont(None, 150)
		self.label = self.font.render(self.current_question[0 if self.is_asking else 1], True, self.color_text)
		self.label_rect = self.label.get_rect(center=(self.width // 2, self.height // 2))

		# Pygame loop
		running = True
		while running:

			# - events
			for event in pygame.event.get():

				# 'quit'
				if event.type == pygame.QUIT:
					running = False

				# 'keydown'
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						self.update_screen()

			# - display
			self.screen.fill(self.color_background)
			self.screen.blit(self.label, self.label_rect)
			pygame.display.flip()

	def update_screen(self):

		self.switch_current_question()

		self.label = self.font.render(self.current_question[0 if self.is_asking else 1], True, self.color_text)
		self.label_rect = self.label.get_rect(center=(self.width // 2, self.height // 2))
	
	def switch_current_question(self):

		self.is_asking = not self.is_asking

		if self.is_asking:

			# update current_topic
			new_topic = self.current_topic
			while new_topic == self.current_topic:
				new_topic = self.topics[random.randint(0, len(self.topics) - 1)]
			self.current_topic = new_topic
			print(f"\ncurrent_topic: {self.current_topic}")

			# update current_question
			self.current_question = self.get_new_question()
			print(f"current_question: [{self.current_question[0]}] [{self.current_question[1]}]")

	def get_new_question(self):

		new_question = ["question", "answer"]

		constant1 = random.choice(self.constants)
		constant2 = random.choice(self.constants)

		if self.current_topic == "addition":
			new_question[0] = f"{constant1} + {constant2}"
			new_question[1] = f"{constant1 + constant2}"
		elif self.current_topic == "subtraction":
			# prevent answer from being 0
			while constant1 == constant2:
				constant1 = random.choice(self.constants)
			# prevent answer from being negative
			if constant2 > constant1:
				constant1, constant2 = constant2, constant1
			new_question[0] = f"{constant1} - {constant2}"
			new_question[1] = f"{constant1 - constant2}"
		elif self.current_topic == "multiplication":
			new_question[0] = f"{constant1} x {constant2}"
			new_question[1] = f"{constant1 * constant2}"
		elif self.current_topic == "division":
			i = constant1 * constant2
			new_question[0] = f"{i} / {constant2}"
			new_question[1] = f"{i // constant2}"

		return new_question


Asker()

