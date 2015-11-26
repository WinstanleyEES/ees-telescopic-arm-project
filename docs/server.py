#!/usr/bin/python
# -*- coding: latin-1 -*

import pygame
from pygame.locals import *
import sys, os, time
import socket

Y_COORDS = 0
Z_COORDS = 100

MIN_Y = 0
MAX_Y = 200
MIN_Z = 0
MAX_Z = 100
SAFE_Z = 20

MAG_STATE = False
COOLDOWN = 30
MAXCOOLDOWN = 30
TRIGGER = 0

pygame.init()
pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption("EES - Telescopic Arm Software - V 0.0.1 - © Ryan Warren 2015")
screen = pygame.display.set_mode((1, 1)) #800 - 600
clock = pygame.time.Clock()
FPS = 20

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joysticks[0].init()

display_font = pygame.font.SysFont("monospace", 15)

HOST = "0.0.0.0"
PORT = 3443

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[+] socket created"

try :
	s.bind((HOST, PORT))
except socket.error as msg :
	print "[+] Bind failed... Error Code: " + str(msg[0]) + " Message: " + msg[1]
	sys.exit
	
print "[+] socket bind complete"

s.listen(1)
print "[+] socket now listening for connections"

conn, addr = s.accept()
print "[+] connected with " + addr[0] + " : " + str(addr[1])

while True :
	data = raw_input("Enter data to send: ")
	
	if data == "joystickpos" :
		print "[+] press ctrl+c to stop sending data"
		conn.send(data)
		
		while True :
			try :
				for event in pygame.event.get() :
					if event.type == QUIT :
						pygame.quit()
						conn.send("quit")
						conn.send("quit")
						s.close()
						sys.exit()
				
				if COOLDOWN == MAXCOOLDOWN and joysticks[0].get_axis(2) <= -0.5 and joysticks[0].get_axis(2) >= -1.0 : # use < -0.3 and get_axis(3) for XBOX Controller
					TRIGGER = joysticks[0].get_axis(2)
					COOLDOWN = 0
						
				joyposition = "{0}, {1}, {2}, {3}, {4}".format(joysticks[0].get_axis(1), joysticks[0].get_axis(3), TRIGGER, COOLDOWN, MAXCOOLDOWN)
				
				conn.send(joyposition)
				
				if COOLDOWN != MAXCOOLDOWN :
					TRIGGER  = 0
					COOLDOWN += 1
					
				print COOLDOWN
				
				clock.tick(FPS)
				
			except KeyboardInterrupt :
				conn.send("quit")
				break
				
	elif data == "quit" :
			conn.send("quit")
			print "[+] Quitting..."
			s.close()
			sys.exit()

sys.exit()