import kivy

kivy.require("2.2.1")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

class HomeWidget(Widget):
    def __init__(self, **kwargs):
        super(HomeWidget, self).__init__(**kwargs)
        self.drawMyStuff()

        self.bind(pos=self.drawMyStuff) 
        self.bind(size=self.drawMyStuff)
    
    def drawMyStuff(self, *args):
        self.canvas.clear()

        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size)

class LeoApp(App):
    def build(self):
        return HomeWidget()

if __name__ == "__main__":
    LeoApp().run()
