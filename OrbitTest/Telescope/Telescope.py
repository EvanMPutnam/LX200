import serial
import time

from pyorbital.orbital import Orbital
from datetime import datetime
import time
import numpy
from astropy.coordinates import SkyCoord



def convertCartesianToRaDec(x, y, z):
    '''
    Returns RA/DECin degrees in decimal notation
    :param x:
    :param y:
    :param z:
    :return:
    '''
    a = None
    if(y > 0 and x > 0):
        a = numpy.degrees(numpy.arctan(y/x))
    elif (x < 0):
        a = 180+numpy.degrees(numpy.arctan(y/x))
    elif (x >0 and y < 0):
        a = 360 + numpy.degrees(numpy.arctan(y/x))
    r = numpy.sqrt(x**2+y**2+z**2)
    d = numpy.degrees(numpy.arcsin(z/r))
    #print("RA:"+str(a) +" Dec:"+ str(d))
    c = SkyCoord(a, d, frame='icrs', unit='deg')
    return c.ra.hms, c.dec.dms

class Telescope:
    def __init__(self, timeOut, serialPort, baud = 9600, orbit = None, test = False):

        if (test == False):
            self.ser = serial.Serial(
                port = serialPort,
                baudrate = baud,
                parity = serial.PARITY_NONE,
                bytesize = serial.EIGHTBITS,
                stopbits = serial.STOPBITS_ONE,
                timeout = timeOut
            )
        else:
            self.ser = None
        self.orbit = None

    def getSerialPort(self):
        print(self.ser)


    def telescopeTime(self):
        print("Getting Telescope Time:")
        commandVal = ":Ga#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
        s = self.ser.read(20)
        print(s)
        print()



    def telescopeAutoAlign(self):
        print("Aligning telescope:")
        print("If it is not moving then it is not working...")
        #If you have timeout set for a couple minutes then it will return a 1
        commandVal = ":Aa#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
        time.sleep(1)
        s = self.ser.read(20)
        print(s)
        print()


    def telescopeMoveWest(self, moveTime):
        print("Moving West by ",moveTime)
        commandValStartSlew = ":Mw#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)
        print("Moving")
        time.sleep(moveTime)
        commandValStopSlew = ":Qw#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)
        print("Ending Movement")
        print()

    def telescopeMoveNorth(self, moveTime):
        print("Moving North by ",moveTime)
        commandValStartSlew = ":Mn#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)
        print("Moving")
        time.sleep(moveTime)
        commandValStopSlew = ":Qn#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)
        print("Ending Movement")
        print()

    def telescopeMoveSouth(self, moveTime):
        print("Moving South by ",moveTime)
        commandValStartSlew = ":Ms#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)
        print("Moving")
        time.sleep(moveTime)
        commandValStopSlew = ":Qs#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)
        print("Ending Movement")
        print()

    def telescopeMoveEast(self, moveTime):
        print("Moving East by ",moveTime)
        commandValStartSlew = ":Me#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)
        print("Moving")
        time.sleep(moveTime)
        commandValStopSlew = ":Qe#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)
        print("Ending Movement")
        print()


    def startEast(self):
        commandValStartSlew = ":Me#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)

    def endEast(self):
        commandValStopSlew = ":Qe#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)

    def startWest(self):
        commandValStartSlew = ":Mw#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)

    def endWest(self):
        commandValStopSlew = ":Qw#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)

    def startNorth(self):
        commandValStartSlew = ":Mn#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)

    def endNorth(self):
        commandValStopSlew = ":Qn#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)

    def startSouth(self):
        commandValStartSlew = ":Ms#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)

    def endSouth(self):
        commandValStopSlew = ":Qs#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)

    def setGPS(self):
        commandValSetGPS = ":gT#"
        commandValSetGPS = str.encode(commandValSetGPS)
        self.ser.write(commandValSetGPS)

    def setSpeed(self, num):
        commsList = [":RG#", ":RC#", ":RM#", ":RS#"]
        if(num in [0, 1, 2, 3]):
            commandValSpeed = commsList[num]
            commandValSpeed = str.encode(commandValSpeed)
            self.ser.write(commandValSpeed)

    def track(self):
        if self.orbit != None:
            now = datetime.utcnow()
            coords = (self.orbit.get_position(now)[0])
            ra, dec = convertCartesianToRaDec(coords[0], coords[1], coords[2])
            print(ra, dec)

            d = str(int(dec.d))
            if(len(d) == 1):
                d = "0"+d

            m = str(int(dec.m))
            if (len(m) == 1):
                m = "0" + m

            s = str(int(dec.s)).split(".")[0]
            if (len(s) == 1):
                s = "0" + s

            decU = ":S"+d+"*"+m+":"+s
            print("Setting target dec " + decU)
            decU = str.encode(decU)
            self.ser.write(decU)
            print("Set target dec")


            hour = str(int(ra.h))
            if(len(hour) == 1):
                hour = "0"+hour

            min = str(int(ra.m))
            if (len(min) == 1):
                min = "0" + min

            sec = str(int(ra.s)).split(".")[0]
            if (len(sec) == 1):
                sce = "0" + sec

            raU = hour + ":" + min + ":" + sec + "#"
            raU = ":Sr"+raU
            print("Setting target ra "+raU)
            raU = str.encode(raU)
            self.ser.write(raU)
            print("Set target ra")
            

            #GO command
            s = ":MS#"
            s = str.encode(s)
            print("MOVING")
            self.ser.write(s)
            time.sleep(1)
            print("MOVED")
            print(self.ser.read(20))



def main():
    #sudo chmod 666 /dev/ttyUSB0
    #lsusb
    #ls -l /sys/bus/usb-serial/devices
    t1 = Telescope(10, '/dev/ttyUSB0')
    t1.telescopeTime()
    #t1.telescopeAutoAlign()
    #t1.telescopeMoveWest(3)
    #t1.telescopeMoveNorth(3)
    #t1.telescopeMoveEast(3)
    #t1.telescopeMoveSouth(3)
    #t1.setGPS()
    #t1.ser.close()
    t1.ser.close()





if __name__ == '__main__':
    main()