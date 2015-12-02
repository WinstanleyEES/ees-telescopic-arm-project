#!/usr/bin/python
import pygame

# the main gui object class
class GuiObject() :

	# the init function sets the height, width, colour, x and y of the gui object
	def __init__(self, width, height, colour, x, y) :
		self.width = width
		self.height = height
		self.colour = colour
		self.x = x
		self.y = y
	
	# the move function will allpw the gui object to move by a specified x and y value
	def move(self, x, y) :
		self.x += x
		self.y += y
