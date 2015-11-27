#!/usr/bin/python
# Imports
import socket
import sys
import time
import sys, os
import RPi.GPIO as GPIO

# Setting up the GPIO pins on the raspberry pi
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Turning all of the outputs to false
GPIO.cleanup()
# Setting the specific GPIO pins as an output
GPIO.setup(17, GPIO.OUT) # Y
GPIO.setup(27, GPIO.OUT) # Z
GPIO.setup(22, GPIO.OUT) # T
GPIO.setup(10, GPIO.OUT) # Z
GPIO.setup(9, GPIO.OUT)  # Y
GPIO.setup(11, GPIO.OUT) # T

# Variables for checking whether or not the light is one
LIGHTONY = False
LIGHTONZ = False
LIGHTONT = False
MAGSTATE = False

# Setting the port that the client will connect to
HOST = "192.168.43.141"
# Setting the port that the client will connect to
PORT = 3443

# Initializing the soket with the specified settings
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Attempting to connect to the server
c.connect((HOST, PORT))

# Creating the main loop
while True :
	# storing the servers data to the clients
	data = c.recv(1024)
	
	# Checking if the data is not equal to nothing
	if len(data) > 0 :
		# Checking if the data is equal to joysickpos which will initialize the collection of the joystick data positions
		if data == "joystickpos" :
			print "[+] getting joystick data."
			while True :
				# Storing the data sent from the server in the variable joyaxis
				joyaxis = c.recv(1024)
				# Checking that the user isn't trying to quit the program
				if joyaxis != "quit" :
					# Splitting the data into and array allowing the program to access the positions seperately
					joydata = joyaxis.split(",")
					
					# Grabbing the data that is stored in the array and storing it in a new temporary variable with the appropriate data type
					Y = float((joydata[0])[:5])
					Z = float((joydata[1])[:5])
					T = float((joydata[2])[:5])
					C = int((joydata[3])[:2])
					M = int((joydata[4])[:2])

					# Checking if the left thumb stick is pushed forwards
					if Y <= -0.5 :
						# Toggling which GPIO is outputting a high voltage and a low voltage
						GPIO.output(27, GPIO.HIGH)
						GPIO.output(10, GPIO.LOW)
					
					# Checking if the left thumbstick is pulled back
					elif Y >= 0.5 :
						# Toggling which GPIO is outputting a high voltage and a low voltage
						GPIO.output(10, GPIO.HIGH)
						GPIO.output(27, GPIO.LOW)
					
					# Otherwise setting both GPIO to emmit a low voltage
					else :
						GPIO.output(27, GPIO.LOW)
						GPIO.output(10, GPIO.LOW)

					# Checking if the right thumb stick is pushed forwards
					if Z <= -0.5 :
						# Toggling which GPIO is outputting a high voltage and a low voltage
						GPIO.output(17, GPIO.HIGH)
						GPIO.output(9, GPIO.LOW)
					
					# Checking if the right thumbstick is pulled back
					elif Z >= 0.5 :
						# Toggling which GPIO is outputting a high voltage and a low voltage
						GPIO.output(9, GPIO.HIGH)
						GPIO.output(17, GPIO.LOW)
					
					# Otherwise setting both GPIO to emmit a low voltage
					else :
						GPIO.output(17, GPIO.LOW)
						GPIO.output(9, GPIO.LOW)

					# Checking if the trigger is pressed and that the magnet isn't already turned on
					if T <= -0.5 and T >= -1.0 and MAGSTATE == False :
						# Toggling which GPIO is outputting a high voltage and a low voltage
						GPIO.output(22, GPIO.HIGH)
						GPIO.output(11, GPIO.LOW)
						# Setting the magnet to on
						MAGSTATE = True
					
					# Checking if the trigger is pressed and the magnet is turned on
					elif T <= -0.5 and T >= -1.0 and MAGSTATE == True :
						# Toggling which GPIO is outputting a high voltage and a low voltage
						GPIO.output(22, GPIO.LOW)
						GPIO.output(11, GPIO.HIGH)
						# Setting the magnet to off
						MAGSTATE = False
				
				# Otherwise cleaning up the GPIO pins and breaking out of the loop					
				else :
					GPIO.cleanup()
					break
		
		# If the server sends the quit command the program exits
		elif data == "quit" :
			sys.exit()

# Fail safe close
sys.exit()