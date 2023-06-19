from kivy.tests.common import GraphicUnitTest

class MyTestCase(GraphicalUnitTest):
    
    def test_runtouchapp(self):
        # non-integrated approach
        from kivy.app import runTOuchApp
        from kivy.uix.button import Button

        button = Button()
        runTouchApp(button)

        # get your window instance safely
        from kivy.base import EventLoop
        EventLoop.ensure_window()
        window = EventLoop.window

        # your asserts
        self.assertEqual(Window.children[0], button)
        self.assertEqual(
            window.children[0].height,
            window.height
        )
