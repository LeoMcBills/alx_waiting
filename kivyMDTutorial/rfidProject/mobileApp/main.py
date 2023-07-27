from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivy.utils import get_color_from_hex
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock
from kivy.metrics import dp
from pyfirmata import Arduino, util

Window.size = (310, 580)

# Arduino
arduino = Arduino('COMX')
it = util.Iterator(arduino)
it.start()

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
    
    def show_snackbar(self):
        snackbar = Snackbar(
            text="[color=#ddbb34]Feature unavailable![/color]",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=(Window.width - (dp(10) * 2)) / Window.width
        )
        snackbar.open()

        Clock.schedule_once(lambda dt: snackbar.dismiss(), .8)
    
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
        if self.dialog:
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

    def on_start(self):
        Clock.schedule_interval(self.read_rfid, 1.0)
        
    def read_rfid(self, dt):
        # Read the RFID tag ID from the Arduino
        # Replace 'A0' with the appropriate pin to which your RFID reader is connected
        tag_id = arduino.analog[0].read()
        print(tag_id)


if __name__ == "__main__":
    Slope().run()