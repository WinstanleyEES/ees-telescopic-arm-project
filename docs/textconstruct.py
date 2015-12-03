import pygame

class TextConstruct() :
	
	def __init__(self, font, size, colour) :
		self.font = pygame.font.SysFont(font, size)
		self.colour = colour
		self.length = 0
		self.individual_strings = []

	def draw_text_line(self, strings, colours, vertical_alignment, x, y, screen=None) :
		self.individual_strings = []
		self.textline = []
		
		if vertical_alignment == "left" :
			xpos = x
			ypos = y
			
			for s in xrange(0, len(strings)) :
			
				if len(colours) == len(strings) :
					c = s
				else :
					c = 0
					
				string = (self.font.render((strings[s]), True, colours[c]))
				self.textline.append([string, xpos, ypos])
				xpos += string.get_width()
				
		elif vertical_alignment == "centre" :
			totallength = 0
			xpos = x
			ypos = y
			
			screenx, screeny = screen.get_size()
			tmpstrings = []
			
			for s in xrange(0, len(strings)) :
				
				if len(colours) == len(strings) :
					c = s
				else :
					c = 0
					
				string = (self.font.render((strings[s]), True, colours[c]))
				tmpstrings.append(string)
				totallength += string.get_width()
				xpos += string.get_width()
				
			startingx = (screenx / 2) - (xpos / 2)
			xpos = startingx
			
			for s in xrange(0, len(tmpstrings)) :
				self.textline.append([tmpstrings[s], xpos, ypos])
				xpos += tmpstrings[s].get_width()
				
		elif vertical_alignment == "right" :
			xpos = x
			ypos = y
			
			screenx, screeny = screen.get_size()
			tmpstrings = []
			
			totallength = screenx
			
			for s in xrange(len(strings) - 1, -1, -1) :
			
				if len(colours) == len(strings) :
					c = s
				else :
					c = 0
					
				string = (self.font.render((strings[s]), True, colours[c]))
				tmpstrings.append(string)
				totallength -= string.get_width()			
			
			for s in xrange(0, len(tmpstrings)) :
				screenx -= tmpstrings[s].get_width()
				self.textline.append([tmpstrings[s], screenx, ypos])
			
		else :
			print "uh oh!"
			
		return self.textline
				
	
	def draw_text_single(self) :
		pass