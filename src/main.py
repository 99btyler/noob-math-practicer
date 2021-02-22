import pygame
pygame.init()


class Question():

	def __init__(self):
		self.font = pygame.font.SysFont(None, 150)
		self.label = self.font.render("ENTER", True, color_text)
		self.label_rect = self.label.get_rect(center=(width / 2, height / 2))

	def update(self):
		self.label = self.font.render(self.get_new_question(), True, color_text)
		self.label_rect = self.label.get_rect(center=(width / 2, height / 2))

	def get_new_question(self):
		return "?"


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

