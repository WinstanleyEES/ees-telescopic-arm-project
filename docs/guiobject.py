import pygame

class GuiObject() :

	def __init__(self, width, height, colour, x, y) :
		self.width = width
		self.height = height
		self.colour = colour
		self.x = x
		self.y = y
		
	def move(self, x, y) :
		self.x += x
		self.y += y