
import socket
import Telescope


def commandDict(telescopeObj):
    '''
    UP DOWN LEFT RIGHT
    UP_END DOWN_END LEFT_END RIGHT_END

    :param telescopeObj:
    :return:
    '''
    command = {"UP":telescopeObj.startNorth, "DOWN":telescopeObj.startSouth,
                   "LEFT":telescopeObj.starWest, "RIGHT": telescopeObj.startEast,

                   "UP_END":telescopeObj.endNorth, "DOWN_END": telescopeObj.endSouth,
                   "LEFT_END":telescopeObj.endWest, "RIGHT_END":telescopeObj.endEast

                   }

    return command








def main():

    #Get host of the server
    host = input("Enter Host Address")
    port = 5000


    #Create the socket and bind it to the host/port
    s = socket.socket()
    s.bind((host, port))

    #Listen for one connection
    s.listen(1)


    #Get the client and address of client from socket
    client, addr = s.accept()
    print("Connection from: "+str(addr))


    #Create a telescope object
    t1 = Telescope.Telescope()

    #Get the command set
    commandSet = commandDict(t1)



    #Main loop for the connection...
    while True:
        data = client.recv(1024).decode('utf-8')
        if data:
            print(data)
            if(data in commandSet):
                commandSet[data]()

            #Might need to check speed
            if("SPEED" in data):
                d = data.split()
                t1.setSpeet(int(d[d.length-1]))

        if(data == "QUIT"):
            #Close the telescope connection and the socket connection
            t1.ser.close()
            client.close()
            break


if __name__ == '__main__':
    main()