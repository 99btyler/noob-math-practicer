import random

import pygame


class Asker():

	def __init__(self):

		self.color_background = (255, 255, 255)
		self.color_text = (32, 32, 32)
		self.width = 420
		self.height = 180

		self.topics = ["addition", "subtraction", "multiplication", "division"]
		self.previous_topic = self.topics[0]
		self.constants = [3, 4, 6, 7, 8, 9, 12]

		self.current_ask = ["1 + 1", "2"]
		self.current_ask_index = 0

		# Pygame screen
		pygame.init()
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption("noob-math-practicer")

		# Pygame widgets
		self.font = pygame.font.SysFont(None, 150)
		self.label = self.font.render(self.current_ask[self.current_ask_index], True, self.color_text)
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
						self.update()

			# - display
			self.screen.fill(self.color_background)
			self.screen.blit(self.label, self.label_rect)
			pygame.display.flip()

	def update(self):

		if self.current_ask_index == 0:
			self.current_ask_index = 1
		else:
			self.change_ask()
			self.current_ask_index = 0
			print(f"current_ask: [{self.current_ask[0]}] [{self.current_ask[1]}]")

		self.label = self.font.render(self.current_ask[self.current_ask_index], True, self.color_text)
		self.label_rect = self.label.get_rect(center=(self.width // 2, self.height // 2))

	def change_ask(self):
		
		current_topic = self.previous_topic
		while current_topic == self.previous_topic:
			current_topic = self.topics[random.randint(0, len(self.topics) - 1)]
		print(f"\ncurrent_topic: {current_topic}")

		constant1 = random.choice(self.constants)
		constant2 = random.choice(self.constants)

		# Addition
		if current_topic == self.topics[0]:
			self.current_ask[0] = f"{constant1} + {constant2}"
			self.current_ask[1] = f"{constant1 + constant2}"
		# Subtraction
		elif current_topic == self.topics[1]:
			# prevent answer from being 0
			while constant1 == constant2:
				constant1 = random.choice(self.constants)
			# prevent answer from being negative
			if constant2 > constant1:
				constant1, constant2 = constant2, constant1
			self.current_ask[0] = f"{constant1} - {constant2}"
			self.current_ask[1] = f"{constant1 - constant2}"
		# Multiplication
		elif current_topic == self.topics[2]:
			self.current_ask[0] = f"{constant1} x {constant2}"
			self.current_ask[1] = f"{constant1 * constant2}"
		elif current_topic == self.topics[3]:
			i = constant1 * constant2
			self.current_ask[0] = f"{i} / {constant2}"
			self.current_ask[1] = f"{i // constant2}"

		self.previous_topic = current_topic


Asker()

