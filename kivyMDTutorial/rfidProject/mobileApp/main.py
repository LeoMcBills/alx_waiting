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
from kivymd.uix.screen import MDScreen

Window.size = (310, 580)

class Card(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class ScanPage(MDScreen):

    def on_enter(self, *args):
        Clock.schedule_once(self.open_next_page, 2)

    def open_next_page(self, dt):
        self.manager.current = "patient"

class Slope(MDApp):
    dialog = None
    arduino = None
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("menu.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("signin.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        screen_manager.add_widget(ScanPage(name="scan"))
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
            size_hint_x=(Window.width - (dp(10) * 2)) / Window.width,
            duration=0.8
        )
        snackbar.open()
    
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

    def detect_arduino(self):
        # Use pyfirmata.util to auto-detect the Arduino port
        try:
            arduino = Arduino('/dev/ttyACM0')  # or Arduino('COM3') on Windows
            return arduino
        except Exception as e:
            print("Error:", e)
            self.show_snackbar()
            return None

    def on_start(self):
        self.arduino = self.detect_arduino()  # Detect Arduino and store in self.arduino
        if self.arduino is not None:
            Clock.schedule_interval(self.read_rfid, 1.0)

    def read_rfid(self, dt):
        if self.arduino is not None:
            # The Arduino object doesn't have an iter_read() method, so we don't need it
            # Just read the data directly from the serial port
            data = self.arduino.analog[0].read()
            print(data)
            if data == None:
                self.root.current = "patient"

if __name__ == "__main__":
    Slope().run()