from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


class MainWidget(Widget):
    pass

Builder.load_file("./TestLab.kv")

class TestLab(App):
    def build(self):
        return MainWidget()

TestLab().run()
