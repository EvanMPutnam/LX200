import serial
import time



class Telescope:
    def __init__(self, timeOut, serialPort, baud = 9600):


        self.ser = serial.Serial(
            port = serialPort,
            baudrate = baud,
            parity = serial.PARITY_NONE,
            bytesize = serial.EIGHTBITS,
            stopbits = serial.STOPBITS_ONE,
            timeout = timeOut
        )





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




def main():
    #sudo chmod 666 /dev/ttyUSB0
    #lsusb
    #ls -l /sys/bus/usb-serial/devices
    t1 = Telescope(10, 'COM3')
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
