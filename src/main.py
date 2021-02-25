import pygame
from random import choice, randint


class Asker():

	def __init__(self):

		# [question, answer]
		self.current_ask = ["•••", None]

		self.font = pygame.font.SysFont(None, 150)
		self.label = self.font.render(self.current_ask[0], True, color_text)
		self.label_rect = self.label.get_rect(center=(width / 2, height / 2))

		self.topics = ["addition", "subtraction", "multiplication", "division"]
		self.previous_topic = self.topics[0]

		self.constants = [3, 4, 6, 7, 8, 9, 12]

	def update(self):
		self.label = self.font.render(self.get_new_ask()[0], True, color_text)
		self.label_rect = self.label.get_rect(center=(width / 2, height / 2))
		print(f"{self.current_ask[1]}")

	def get_new_ask(self):

		current_topic = self.previous_topic
		while current_topic == self.previous_topic:
			current_topic = self.topics[randint(0, len(self.topics) - 1)]
		print(f"current_topic: {current_topic}")

		constant1 = choice(self.constants)
		constant2 = choice(self.constants)

		# Addition
		if current_topic == self.topics[0]:
			self.current_ask[0] = f"{constant1} + {constant2}"
			self.current_ask[1] = f"{constant1 + constant2}"
		# Subtraction
		elif current_topic == self.topics[1]:
			# - prevent answer from being 0
			while constant1 == constant2:
				constant1 = choice(self.constants)
			# - prevent answer from being negative
			if constant2 > constant1:
				i = constant1
				constant1 = constant2
				constant2 = i
			self.current_ask[0] = f"{constant1} - {constant2}"
			self.current_ask[1] = f"{constant1 - constant2}"
		# Multiplication
		elif current_topic == self.topics[2]:
			self.current_ask[0] = f"{constant1} x {constant2}"
			self.current_ask[1] = f"{constant1 * constant2}"
		# Division
		elif current_topic == self.topics[3]:
			i = constant1 * constant2
			self.current_ask[0] = f"{i} / {constant2}"
			self.current_ask[1] = f"{i // constant2}"

		self.previous_topic = current_topic

		return self.current_ask


pygame.init()

color_background = (255, 255, 255)
color_text = (32, 32, 32)

width = 420
height = 180

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("noob-math-practicer")

asker = Asker()


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
				asker.update()

	# DISPLAY
	screen.fill(color_background)
	screen.blit(asker.label, asker.label_rect)
	pygame.display.flip()

