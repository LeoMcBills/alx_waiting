from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label


class StartScreen(Widget):
    pass

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

class vTrackerApp(App):
    def build(self):
        return StartScreen()
        
    
if __name__ == '__main__':
    vTrackerApp().run()