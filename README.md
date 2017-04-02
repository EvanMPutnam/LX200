# LX200
Telescope Control

Note that this is an in progress progect.  

Currently Controls:
  Speed
  Movement

Planned Features:
  Zoom




Dependencies:
  Kivy - Used for the interface to handle the commands
  PySerial - Used to interface with telescope
  
  
  
Server Device:
  Connect to the Telescopes serial port and other end to computers usb.
  The Telescope is instantiated with a serial port location.  Default is '/dev/ttyUSB0' on linux.
  May be different on your operating system.
  
  Wait for connection to be established via sockets with client and then good to go!
  
  
Client Device:
  Run the application and then use arrow keys to move telescope. 1,2,3,4 will specify speed.
