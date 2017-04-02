from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window





import socket


class Screen(GridLayout):
    def __init__(self, socketObj, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self.keyboard.bind(on_key_down=self.on_keyboard_down)
        self.keyboard.bind(on_key_up=self.on_keyboard_up)

        #Socket
        self.socket = socketObj.s
        #Can then call tele.method()

        #Commands for the release on joysticks
        self.leftDown = False
        self.rightDown = False
        self.upDown = False
        self.downDown = False






    #Keyboard close stuff...
    def keyboard_closed(self):
        self.keyboard.unbind(on_key_down=self.on_keyboard_down)
        self.keyboard = None






    def on_keyboard_down(self, keyboard, keycode, text, modifiers):

        print(keycode)


        if keycode[1] == 'up':
            if(self.upDown == False):
                self.upDown = True
                print("Going Up")
                #Send command "upStart"
                message = "UP"
                self.socket.send(message.encode('utf-8'))

        elif keycode[1] == 'down':
            if(self.downDown == False):
                self.downDown = True
                print("Going Down")
                #Send command downStart
                message = "DOWN"
                self.socket.send(message.encode('utf-8'))

        elif keycode[1] == 'left':
            if(self.leftDown == False):
                self.leftDown = True
                print("Going Left")
                #Send command leftStart
                message = "LEFT"
                self.socket.send(message.encode('utf-8'))

        elif keycode[1] == 'right':
            if(self.rightDown == False):
                self.rightDown = True
                print("Going Right")
                #Send command startRight
                message = "RIGHT"
                self.socket.send(message.encode('utf-8'))



        #RIGHT HERE MAKE AN EXIT COMMAND
        #Escape charachter key.  Send the end command.  Close the socket.



        elif keycode[1] == '1':
            #Send speed1Start
            message = "SPEED_1"
            self.socket.send(message.encode('utf-8'))

        elif keycode[1] == '2':
            #Send speed2Start
            message = "SPEED_2"
            self.socket.send(message.encode('utf-8'))

        elif keycode[1] == '3':
            #Send speed3Start
            message = "SPEED_3"
            self.socket.send(message.encode('utf-8'))

        elif keycode[1] == '4':
            #Send speed4Start
            message = "SPEED_4"
            self.socket.send(message.encode('utf-8'))



        return True







    def on_keyboard_up(self, keyboard, keycode):
        if keycode[1] == 'up':
            self.upDown = False
            print("Release up")
            message = "UP_END"
            self.socket.send(message.encode('utf-8'))


        elif keycode[1] == 'down':
            self.downDown = False
            print("Release down")
            message = "DOWN_END"
            self.socket.send(message.encode('utf-8'))


        elif keycode[1] == 'left':
            self.leftDown = False
            print("Release left")
            message = "LEFT_END"
            self.socket.send(message.encode('utf-8'))


        elif keycode[1] == 'right':
            self.rightDown = False
            print("Release right")
            message = "RIGHT_END"
            self.socket.send(message.encode('utf-8'))


        return True







class MyApp(App):

    def __init__(self, SocketOBJ):
        #Creates the previous objects "Stuff"
        super(MyApp, self).__init__()
        self.socketObj = SocketOBJ#Some socket object

    def build(self):
        return Screen(self.socketObj)




class SocketClient():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket()
        self.s.connect((host, port))




if __name__ == '__main__':
    #Create socket object
    #host = "127.0.0.1"
    host = "129.21.159.120"
    port = 5000
    s1 = SocketClient(host, port)

    #Create app and pass reference to Telescope object
    m1 = MyApp(s1)

    #Run the app
    m1.run()

    #Close the port when the app is done...
    m1.socket.close()