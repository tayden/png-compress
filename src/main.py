from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.logger import Logger

import os
from core import load_img, save_img, quantize_colors

from components.load_dialog import LoadDialog
from components.save_dialog import SaveDialog
from components.slide_control import SlideControl
from components.img_preview import ImgPreview


class Root(BoxLayout):
    img_preview = ObjectProperty(None)

    filename = StringProperty()
    color = ObjectProperty(None)
    compression = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup, directory=os.path.dirname(self.filename))
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        self.filename = os.path.join(path, filename[0])
        self.img_orig = load_img(self.filename)
        self.img = self.img_orig.copy()
        self.update_preview()
        self.dismiss_popup()

    def save(self, path, filename):
        save_path = os.path.join(path, filename)
        save_img(self.img, self.compression.slider.value, save_path)
        
        self.dismiss_popup()

    def update_preview(self):
        Logger.debug("Preview: updated")
        if hasattr(self, 'img_orig'):
            self.img = quantize_colors(self.img_orig, 2**self.colors.slider.value)
            self.img_preview.update(self.img)
    

class CompressApp(App):
        def build(self):
            return Root()


Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    CompressApp().run()