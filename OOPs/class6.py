import random
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.clock import Clock
from kivy.core.window import Window


class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 0.5, 0.5, 1)
        s = Scatter()
        f = FloatLayout()
        i = Image(source='lena.png', size_hint=(.1, .1), pos=(0, 0))
        f.add_widget(i)
        s.add_widget(f)
        return s
    

if __name__ == '__main__':
    MyApp().run()