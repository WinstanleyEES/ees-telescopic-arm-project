import pygame

class TextConstruct() :
	
	def __init__(self, font, size, colour) :
		self.font = pygame.font.SysFont(font, size)
		self.colour = colour
		self.length = 0
		self.individual_lengths = []
		self.individual_strings = []

	def draw_text_line(self, strings, colours, vertical_alignment, x, y) :
		self.individual_lengths = []
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
			pass
			
		elif vertical_alignment == "right" :
			pass
			
		else :
			print "uh oh!"
			
		return self.textline
				
	
	def draw_text_single(self) :
		pass