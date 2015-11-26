# ees-telescopic-arm-project
Engineering project - these are the python files that will be used in conjunction with the raspberry pi and other controllers to control the telescopic arm.

The program will allow a user to send joystick / keyboard inputs over a server to a raspberry pi which will inturn control the telescopic arm.

The left thumb stick on the controller will move the telescopic arm in the Y axis and the right thumbstick will controll the line extension in the Z axis. The right trigger will control whether the electromagnet is on or off.

The implimentation of the left and right bumpers would allow the control of yaw in the telescopic arm giving a wider range of movement.

The GUI will allow the user to see real time where the arm is whilst remaining at a safe distance from the arm.

The data will be send from a main computer / laptop to a standalone raspberry pi which will connect via a portable mobile hotspot for demonstration purposes however this would ideally be connected via ethernet at it would allow for a more reliable connection.
