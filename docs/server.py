#!/usr/bin/python
# -*- coding: latin-1 -*

# Imports
import pygame
from pygame.locals import *
import sys, os, time
import socket

# Variables
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

# Initialization
pygame.init()
pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption("EES - Telescopic Arm Software - V 0.0.1 - © Ryan Warren 2015")
screen = pygame.display.set_mode((1, 1)) #800 - 600
clock = pygame.time.Clock()
FPS = 20

# Gamepad Settings
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joysticks[0].init()

# Font Settings
display_font = pygame.font.SysFont("monospace", 15)

# Setting the host and port that the server will be initialized on
HOST = "0.0.0.0"
PORT = 3443

# Creating the socket and prompting the user if it is successful
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[+] socket created"

# Trying to bind the socket to the specified host and port
try :
	s.bind((HOST, PORT))
# Catching the error message and displaying it to the user
except socket.error as msg :
	print "[+] Bind failed... Error Code: " + str(msg[0]) + " Message: " + msg[1]
	sys.exit()

# Else prompting the user that the bind was successful
print "[+] socket bind complete"

# Setting the server to listen for one client connection
s.listen(1)
print "[+] socket now listening for connections"

# Storing the connection and displaying the user with the connections IP adress
conn, addr = s.accept()
print "[+] connected with " + addr[0] + " : " + str(addr[1])

# Creating the main loop
while True :
	# Prompting the user to input a command
	data = raw_input("Enter data to send: ")
	
	# Checking if the data is equal to "joystickpos"
	if data == "joystickpos" :
		# Prompting the user with the command to quit the program
		print "[+] press ctrl+c to stop sending data"
		# Sending "joystickdata" to the client
		conn.send(data)
		
		# Creating the loop which will allow the server to continue to send the joystick data to the client
		while True :
			# Using a try / except function to take advantage of the KeyboardInterrup event to stop sending data
			try :
				# Checking if the pygame event is quit
				for event in pygame.event.get() :
					if event.type == QUIT :
						# Quitting pygame
						pygame.quit()
						# Sending quit twice - try to fix so that it only has to send once
						conn.send("quit")
						conn.send("quit")
						# Closing the socket
						s.close()
						# Exiting the program
						sys.exit()
				
				# Checking if the cooldown variable is equal to the maxcool down to prevent the constant sending of the trigger position
				# Also checking if the trigger is pressed
				if COOLDOWN == MAXCOOLDOWN and joysticks[0].get_axis(2) <= -0.5 and joysticks[0].get_axis(2) >= -1.0 : # use < -0.3 and get_axis(3) for XBOX Controller
					# Setting the trigger variable to the the triggers position
					TRIGGER = joysticks[0].get_axis(2)
					# Setting cooldown to 0 so that the cooldown can begin
					COOLDOWN = 0
				
				# formatting the string of data containing the joystick positions to send to the client
				joyposition = "{0}, {1}, {2}, {3}, {4}".format(joysticks[0].get_axis(1), joysticks[0].get_axis(3), TRIGGER, COOLDOWN, MAXCOOLDOWN)
				
				# Sending the joystick data to the client
				conn.send(joyposition)
				
				# Incrementing the cooldown if it is not equal to the maxcooldown
				if COOLDOWN != MAXCOOLDOWN :
					TRIGGER  = 0
					COOLDOWN += 1
				
				# Using the pygame clock function to limit the time the program loops per second
				clock.tick(FPS)
			
			# Waiting for the keyboard interrupt
			except KeyboardInterrupt :
				# Sending the quit command to the client
				conn.send("quit")
				break

	# Checking if the data is equal to quit
	elif data == "quit" :
			# Sending the quit command to the client
			conn.send("quit")
			# Displaying the quitting message
			print "[+] Quitting..."
			# Closing the socket
			s.close()
			# Exiting the script
			sys.exit()

# The 'if all else fails' quit expression
sys.exit()