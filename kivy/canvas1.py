#!/usr/bin/python3

import kivy
kivy.require("2.2.1")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

class Home(Widget):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        self.draw_my_stuff()

        self.bind(pos=self.draw_my_stuff)
        self.bind(size=self.draw_my_stuff)

    def draw_my_stuff(self, *args):
        self.canvas.clear()

        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size)

class Leo(App):
    def build(self):
        return Home()

if __name__ == "__main__":
    Leo().run()
