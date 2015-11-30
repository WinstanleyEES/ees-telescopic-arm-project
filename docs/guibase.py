import pygame

class Gui() :
	
	def __init__(self, width, height, colour, title, fps) :
		self.width = width
		self.height = height
		self.colour = colour
		self.title = title
		self.fps = fps
		
		self.SCREEN = pygame.display.set_mode((width, height))
		pygame.display.set_caption(title)
		
		self.background = pygame.Surface((width, height))
		self.background.fill(colour)
		
	def update(self) :
		pass
		
	def render(self) :
		self.SCREEN.blit(self.background, (0, 0))
		pygame.display.flip()
		
	def terminate(self) :
		pygame.quit()