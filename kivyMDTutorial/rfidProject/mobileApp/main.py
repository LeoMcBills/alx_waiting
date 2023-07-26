from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivy.utils import get_color_from_hex
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

Window.size = (310, 580)

class Card(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class Slope(MDApp):
    dialog = None
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("menu.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("signin.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        screen_manager.add_widget(Builder.load_file("scan.kv"))
        screen_manager.add_widget(Builder.load_file("register.kv"))
        screen_manager.add_widget(Builder.load_file("patient.kv"))
        screen_manager.add_widget(Builder.load_file("repo.kv"))

        return screen_manager
    
    def get_color(self, hex_code):
        rgb_code = get_color_from_hex(hex_code)
        return rgb_code
    
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="NIRA API not configured. Please contact the administrator.",
                buttons=[
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.discard_draft,
                    ),
                ],
            )
        self.dialog.open()

    def discard_draft(self, instance):
        self.dialog.dismiss()

    def show_another_dialog(self):
        if self.dialog:  # If there's already a dialog open, you may want to handle this differently
            self.dialog = MDDialog(
                text="No RFID Printer detected.",
                buttons=[
                    MDFlatButton(
                        text="Cancel",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, instance):
        self.dialog.dismiss()


if __name__ == "__main__":
    Slope().run()