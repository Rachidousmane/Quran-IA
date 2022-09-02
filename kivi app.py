import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.0.0')
class Gamequran(BoxLayout):
    def __init__(self) -> None:
        super(Gamequran,self).__init__()
class qurapp(App):
    def build (self):
        return Gamequran()
qurap = qurapp(App)
qurap.run()
