from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, StringProperty

class StartScreen(GridLayout):
    pass
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         for i in range(0, 100):
#             size = dp(100)
#         b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
#         self.add_widget(b)

class LoginScreen(Widget):
    pass

class RegisterScreen(Widget):
    pass

class MainScreen(Widget):
    pass

class ScanScreen(Widget):
    pass

class RegisterPatientScreen(Widget):
    pass

class PatientScreen(Widget):
    pass

class TrackerApp(App):
    kv_file = 'tracker.kv'

if __name__ == '__main__':
    TrackerApp().run()