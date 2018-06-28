from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)