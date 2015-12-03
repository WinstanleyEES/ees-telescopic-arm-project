#!/usr/bin/python
import pygame

class Gui() :
	
	def __init__(self, width, height, colour, title, fps, icon) :
		self.width = width
		self.height = height
		self.colour = colour
		self.title = title
		self.fps = fps
		self.icon = icon
		self.clock = pygame.time.Clock()
		
		pygame.display.set_icon(icon)
		pygame.display.set_caption(title)
		
		self.screen = pygame.display.set_mode((width, height))
				
		self.background = pygame.Surface((width, height))
	
	def set_bgcolour(self, colour) :
		self.colour = colour
		
	def process_input(self) :
		# getting all the pygame events
		for event in pygame.event.get() :
			# checking if the event is to quit pygame - then quit the program
			if event.type == pygame.QUIT :
				self.terminate()
		
	def update(self) :
		self.background.fill(self.colour)
		
	def render(self, objects, strings) :
		self.screen.blit(self.background, (0, 0))
		
		for object in objects :
			pygame.draw.rect(self.screen, object.colour, (object.x, object.y, object.width, object.height))
		
		if len(strings) > 0 :
			for list in strings :
				for string in list :
					self.screen.blit(string[0], (string[1], string[2]))
		
		pygame.display.flip()
		
	def terminate(self) :
		pygame.quit()