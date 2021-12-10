import pygame

screen = pygame.display.set_mode((500, 500))

run = True

class Fish(pygame.sprite.Sprite):

	def __init__(self, x, y, g):

		super().__init__()

		self.image = pygame.image.load('resources/graphics/Cards/card_jalapeno.png')

		self.rect = self.image.get_rect()

		self.rect.center = (x, y)

		self.clicked = False

		self.g = g


	def reset(self):

		for i in self.g:

			i.rect.x -= 100


	def update(self):

		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos) and not self.clicked:

			keys = pygame.mouse.get_pressed()

			if keys[0]:

				self.kill()
				self.reset()


g = pygame.sprite.Group()


aa = Fish(100, 200, g)
bb = Fish(200, 200, g)

g.add(aa)
g.add(bb)

while run:

	screen.fill('white')
	g.draw(screen)
	g.update()

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False


	pygame.display.update()

pygame.quit()
