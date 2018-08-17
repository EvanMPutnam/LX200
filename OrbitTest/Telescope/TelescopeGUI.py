from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

from pyorbital.orbital import Orbital

import Telescope


class Screen(GridLayout):
    def __init__(self, telescopeOBJ, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self.keyboard.bind(on_key_down=self.on_keyboard_down)
        self.keyboard.bind(on_key_up=self.on_keyboard_up)

        #SerialPort
        self.tele = telescopeOBJ
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
        if keycode[1] == 'up':
            if(self.upDown == False):
                self.upDown = True
                print("Going Up")
                self.tele.startNorth()
        elif keycode[1] == 'down':
            if(self.downDown == False):
                self.downDown = True
                print("Going Down")
                self.tele.startSouth()
        elif keycode[1] == 'left':
            if(self.leftDown == False):
                self.leftDown = True
                print("Going Left")
                self.tele.startWest()
        elif keycode[1] == 'right':
            if(self.rightDown == False):
                self.rightDown = True
                print("Going Right")
                self.tele.startEast()
        elif keycode[1] == '1':
            self.tele.setSpeed(0)
        elif keycode[1] == '2':
            self.tele.setSpeed(1)
        elif keycode[1] == '3':
            self.tele.setSpeed(2)
        elif keycode[1] == '4':
            self.tele.setSpeed(3)
        elif keycode[1] == '5':
            self.tele.track()

        return True

    def on_keyboard_up(self, keyboard, keycode):
        if keycode[1] == 'up':
            self.upDown = False
            print("Release up")
            self.tele.endNorth()
        elif keycode[1] == 'down':
            self.downDown = False
            print("Release down")
            self.tele.endSouth()
        elif keycode[1] == 'left':
            self.leftDown = False
            print("Release left")
            self.tele.endWest()
        elif keycode[1] == 'right':
            self.rightDown = False
            print("Release right")
            self.tele.endEast()
        return True







class MyApp(App):

    def __init__(self, TelescopeOBJ):
        #Creates the previous objects "Stuff"
        super(MyApp, self).__init__()
        self.tele = TelescopeOBJ

    def build(self):
        return Screen(self.tele)






if __name__ == '__main__':
    #Create port
    t1 = Telescope.Telescope(1,'/dev/tty.usbserial')

    #Create tle
    orbit = Orbital('ISS', 'orbit.txt')
    t1.orbit = orbit


    #Create app and pass reference to Telescope object
    m1 = MyApp(t1)

    #Run the app
    m1.run()

    #Close the port when the app is done...
    m1.tele.ser.close()