from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
import socket
from plyer import gyroscope  # Para smartphone tipo ANDROID Y IOS

# KIVY

import time
from kivy.uix.textinput import TextInput



class Client(App):
    counter = 0
    def build(self):
        # 
        Bridge = autoclass('bridge')
        self.br = Bridge.alloc().init()
        self.br.gyroscope.enable()

        # ip para usar en socket.gethostbyname(socket.gethostname())
        g = GridLayout(cols=1)
        b = Button(on_release=self.go)
        self.l = Label()
        self.host = TextInput(text='192.168.0.6')
        g.add_widget(b)
        g.add_widget(self.host)
        g.add_widget(self.l)
        return g

    def go(self, *args):
        HOST = '192.168.0.6'  # DIRECCION IP
        HOST = self.host.text
        PORT = 65436  # PUERTOS
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
        self.s.connect((HOST, PORT))

        while True:
            time.sleep(.25)
            self.send_msg()

    def send_msg(self, *args):
        self.counter += 1
        gyro_data = gyroscope.rotation
        self.s.sendall(str(gyro_data))

    def on_stop(self):
        self.s.close()

Client().run()