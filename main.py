from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class NeonApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(Label(text='NEON BIXBY', font_size=40, bold=True))
        layout.add_widget(Label(text='Chefe, FUNCIONOU!', font_size=24))
        btn = Button(text='MODO CINEMA', size_hint=(1, 0.3))
        btn.bind(on_press=lambda x: print("Modo cinema ativado!"))
        layout.add_widget(btn)
        return layout

NeonApp().run()
