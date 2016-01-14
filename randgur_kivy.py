import sys
import string
import webbrowser
import urllib.request
import kivy
# kivy.require('1.0.6')

from os import system
from urllib.error import HTTPError
from random import choice
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage

class MainFrame(GridLayout):
    def __init__(self, **kwargs):
        super(MainFrame, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Placeholder 1'))
        self.add_widget(Label(text='Placeholder 2'))
        # self.add_widget(AsyncImage(source= self.rand_img_url()))
        self.add_widget(AsyncImage(source='http://i.imgur.com/hHAGpTm.jpg'))


    def rand_img_url(self):
        # while True:
        #     successful = False
        #     chars = string.ascii_letters + string.digits
        #     tempchar = [choice(chars) for n in range(7)]
        #     imgID = "".join(tempchar)
        #     url = "http://i.imgur.com/" + imgID + ".jpg"
        #     try:
        #         opener.open(url)
        #         successful = True
        #     except:
        #         pass
        #     if successful:
        #         return url
        pass

class MyApp(App):
    def build(self):
        return MainFrame()



if __name__ == '__main__':
    MyApp().run()
