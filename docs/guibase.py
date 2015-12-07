#!/usr/bin/python
# importing the pygame module
import pygame
from guiobject import GuiObject

# The gui class that contains the functions for the gui object
class Gui() :
	
	# initializing the settings for the gui
	def __init__(self, width, height, colour, title, fps, icon) :
		# setting the specified icon to be displayed on the gui
		pygame.display.set_icon(icon)
		# setting the specified caption to be displayed on the gui
		pygame.display.set_caption(title)
		
		# setting the gui variables
		self.width = width
		self.height = height
		self.colour = colour
		self.title = title
		self.fps = fps
		self.icon = icon
		self.clock = pygame.time.Clock()
		
		# setting the screen variable to the gui display that takes the parameters of the specified width and height
		self.screen = pygame.display.set_mode((width, height))
		self.background = pygame.Surface((width, height))
	
	# this function allows the script to change the colour of the background
	def set_bgcolour(self, colour) :
		# setting the gui's colour property to colour
		self.colour = colour
	
	# this function handles all of the pygame inputs and handles the event checking
	def process_input(self, objects) :	
		# getting all the pygame events
		for event in pygame.event.get() :
			# checking if the event is to quit pygame - then quit the program
			if event.type == pygame.QUIT :
				# running the terminate command if the 'X' is pressed
				self.terminate()
			elif event.type == pygame.KEYDOWN :
				if event.key == pygame.K_RIGHT :
					print "Right"
					objects[0].move_to(480,40)
					objects[1].move_increment(20,20)
				elif event.key == pygame.K_LEFT :
					print "Left"
					objects[0].move_to(0,40)
					objects[1].move_increment(-20,-20)
					
	# the update function updates all the variables but doesn't commit anything new to the gui
	def update(self) :
		# setting the background colour to the inputted colour
		self.background.fill(self.colour)

	# the render function takes all the objects and draws them to the screen
	def render(self, objects, strings) :
		# rendering the background
		self.screen.blit(self.background, (0, 0))
		
		# rendering all the objects in the scene
		# checking if objects need to be rendered
		if len(objects) > 0 :
			# looping through the objects in the object list
			for object in objects :
				# drawing the object as a rectangle to the gui
				pygame.draw.rect(self.screen, object.colour, (object.x, object.y, object.width, object.height))
		
		# rendering all the strings to the screen
		# checking if strings need to be rendered
		if len(strings) > 0 :
			for list in strings :
				for string in list :
					# drawing the strings to the gui
					self.screen.blit(string[0], (string[1], string[2]))
		
		# updating the display
		pygame.display.flip()
	
	# the terminate function will quit the application
	def terminate(self) :
		# quitting pygame
		pygame.quit()