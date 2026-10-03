from kivy.app import App
from kivy.uix.label import Label
class NeonApp(App):
    def build(self):
        return Label(text='NEON BIXBY FUNCIONOU!')
NeonApp().run()
