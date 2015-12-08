#!/usr/bin/python
# importing the pygame module
import pygame

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
				print objects[2].moveable
				
				if event.key == pygame.K_RIGHT :
					#print "Right"
					#objects[0].move_to(480,40)
					#objects[1].move_increment(20,20)
					
					objects[0].move_increment(20,0)
					objects[1].move_increment(20,0)
					objects[2].move_increment(20,0)
					
					objects[1].proximity(objects[2])
					
				elif event.key == pygame.K_LEFT :
					#print "Left"
					#objects[0].move_to(0,40)
					#objects[1].move_increment(-20,-20)
					
					objects[0].move_increment(-20,0)
					objects[1].move_increment(-20,0)
					objects[2].move_increment(-20,0)
					
					objects[1].proximity(objects[2])
				
				elif event.key == pygame.K_DOWN :
					objects[1].extend(40)
					objects[2].move_increment(0,40)
					
					objects[1].proximity(objects[2])
					
				elif event.key == pygame.K_UP :
					objects[1].extend(-40)
					objects[2].move_increment(0,-40)
					
					objects[1].proximity(objects[2])
					
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
				if object.border == True :
					pygame.draw.line(self.screen, object.border_colour, (object.x, object.height-object.border_thickness), (object.width, object.height-object.border_thickness), object.border_thickness)
		
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
		
# the main gui object class
class GuiObject() :

	# the init function sets the height, width, colour, x and y of the gui object
	def __init__(self, width, height, colour, x, y, moveable, physics, ground, border=False, border_colour=None, border_thickness=0) :
		# setting the gui objects variables
		self.width = width
		self.height = height
		self.colour = colour
		self.x = x
		self.y = y
		self.border = border
		self.border_colour = border_colour
		self.border_thickness = border_thickness
		self.moveable = moveable
		self.physics = physics
		self.ground = ground
		self.attached = False
	
	# the move function will allow the gui object to move by a specified x and y value
	def move_increment(self, x, y) :
		if self.moveable :
			# setting the gui objects x to increment by the inputted x
			self.x += x
			# setting the gui objects y to increment by the inputted y
			self.y += y
		
	# the move function will allow the gui object to move to a specified x and y value
	def move_to(self, x, y) :
		if self.moveable :
			# setting the gui objects x to the inputted x
			self.x = x
			# setting the gui objects y to the inputted y
			self.y = y
		
	def extend(self, increment) :
		self.height += increment
		
	def proximity(self, object_to_move) :
		otc_y = self.height + self.y
		otc_x = self.x - 17
		print otc_x
		#print object_to_move.y
		
		if otc_y == object_to_move.y and otc_x == object_to_move.x:
			object_to_move.moveable = True
		else :
			object_to_move.moveable = False
			
		# print object_to_move.moveable

	#def attach(self) :
	#	if self.moveable :
	#		self.attached = True
		
	#def gravity(self) :
	#	
		
# The textconstructor class that contains the functions for the gui text functions
class TextConstruct() :

	# the init function sets the font, size and colour of the text
	def __init__(self, font, size, colour, bold=False) :
		self.font = pygame.font.SysFont(font, size, bold)
		self.colour = colour
		self.length = 0
		self.individual_strings = []

	# the function that draws a multiple strings of text to the gui
	def draw_text_line(self, strings, colours, vertical_alignment, x, y, padding, screen=None) :
		self.individual_strings = []
		self.textline = []
		
		# checking if the alignment is left
		if vertical_alignment == "left" :
			# setting the x and y positions to those pre-determined by the user
			xpos = x
			ypos = y
			
			# looping through the list of strings
			for s in xrange(0, len(strings)) :
				
				# setting the colours to be the matching colour or one colour throughout
				if len(colours) == len(strings) :
					c = s
				else :
					c = 0
				
				# setting the temporary variable string to be a pygame object
				string = (self.font.render((strings[s]), True, colours[c]))
				# appending the string to the sentence array with the objects x and y positions
				self.textline.append([string, padding + xpos, ypos])
				# incrementing the xposition by the width of the current string
				xpos += string.get_width()
				
		# checking if the alignment is centre	
		elif vertical_alignment == "centre" :
			# setting the total length to 0 and the x and y postitions to those pre-determined by the user
			totallength = 0
			xpos = x
			ypos = y
			
			# storing the screens width and height to their respected temporary variables
			screenx, screeny = screen.get_size()
			# setting tmpstrings to be a blank array
			tmpstrings = []
			
			# looping through the list of strings
			for s in xrange(0, len(strings)) :
				
				# setting the colours to be the matching colour or one colour throughout
				if len(colours) == len(strings) :
					c = s
				else :
					c = 0
					
				# setting the temporary variable string to be a pygame object	
				string = (self.font.render((strings[s]), True, colours[c]))
				# appending the string to the temporary string array
				tmpstrings.append(string)
				# incrementing the total width variable by adding the length of the current string
				totallength += string.get_width()
				# incrementing the x position by the width of the current string
				xpos += string.get_width()
				
			# setting the starting x to be half the width of the screen minus half the total length of the strings
			startingx = (screenx / 2) - (xpos / 2)
			#setting the x positon to the starting x position
			xpos = startingx
			
			# looping through the list of temporary strings
			for s in xrange(0, len(tmpstrings)) :
			
				# appending the string to the textline variable along with the x and y positions
				self.textline.append([tmpstrings[s], xpos, ypos])
				# incrementing the xposition by the width of the current string
				xpos += tmpstrings[s].get_width()
			
		# checking if the alignment is right
		elif vertical_alignment == "right" :
			# setting the x and y positions to those pre-determined by the user
			xpos = x
			ypos = y
			
			# storing the screens width and height to their respected temporary variables
			screenx, screeny = screen.get_size()
			tmpstrings = []
			
			# setting the total length of the screen equal to the width of the screen
			totallength = screenx
			
			# looping through the list of strings backwards
			for s in xrange(len(strings) - 1, -1, -1) :
				
				# setting the colours to be the matching colour or one colour throughout
				if len(colours) == len(strings) :
					c = s
				else :
					c = 0
				
				# setting the temporary variable string to be a pygame object
				string = (self.font.render((strings[s]), True, colours[c]))
				# appending the string to the temporary string array
				tmpstrings.append(string)
				# negating the current strings width from the total length
				totallength -= string.get_width()			
			
			# looping through the list of temporary strings
			for s in xrange(0, len(tmpstrings)) :
			
				# negating the width of the current string from the screens width
				screenx -= tmpstrings[s].get_width()
				# appending the string to the textline variable along with the x and y positions 
				self.textline.append([tmpstrings[s], screenx - padding, ypos])
		
		# printing out the error message
		else :
			print "uh oh!"
		
		# returning the textline array
		return self.textline
				
	# the function that draws a single string of text to the gui - needs implementing
	def draw_text_single(self) :
		pass