from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivy.utils import get_color_from_hex
from kivymd.uix.floatlayout import MDFloatLayout
Window.size = (310, 580)


class Card(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class Slope(MDApp):

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("signin.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        return screen_manager
    
    def get_color(self, hex_code):
        rgb_code = get_color_from_hex(hex_code)
        return rgb_code


if __name__ == "__main__":
    Slope().run()