from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)
    directory = StringProperty()