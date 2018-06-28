from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.logger import Logger


def do_nothing():
    pass

class SlideControl(BoxLayout):
    label = StringProperty()
    value_label = StringProperty()
    value = NumericProperty()
    min = NumericProperty()
    max = NumericProperty()
    step = NumericProperty()
    update = ObjectProperty(do_nothing)

    def on_touch_up(self, touch):
        collision = self.slider.collide_point(*touch.pos)
        if collision:
            self.update()
        
        return collision