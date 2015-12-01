import pygame

class Gui() :
	
	def __init__(self, width, height, colour, title, fps) :
		self.width = width
		self.height = height
		self.colour = colour
		self.title = title
		self.fps = fps
		self.clock = pygame.time.Clock()
		
		self.SCREEN = pygame.display.set_mode((width, height))
		pygame.display.set_caption(title)
		
		self.background = pygame.Surface((width, height))
	
	def set_bgcolour(self, colour) :
		self.colour = colour
		
	def update(self) :
		self.background.fill(self.colour)
		
	def render(self, objects) :
		self.SCREEN.blit(self.background, (0, 0))
		
		for object in objects :
			pygame.draw.rect(self.SCREEN, object.colour, (object.x, object.y, object.width, object.height))
		
		pygame.display.flip()
		
	def terminate(self) :
		pygame.quit()