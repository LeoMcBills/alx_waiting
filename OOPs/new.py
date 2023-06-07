import kivy
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import Property, NemericalProperty, ReferenceListProperty
from kivy.uix.scatter import Scatter
from kivy.uix.float import FloatLayout


class Dragger(App):
    def build(self):
        s = Scatter()
        f = FloatLayout()
        i = Image(source='lena.png', size_hint=(.1, .1), pos=(0, 0))
        f.add_widget(i)
        s.add_widget(f)
        return s
