from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics.texture import Texture

import numpy as np


class ImgPreview(Widget):
    img_texture = ObjectProperty(None)

    def update(self, img):
        self.canvas.before.clear()
        img = np.rot90(np.swapaxes(img, 0, 1))
        self.img_texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='rgb')
        self.img_texture.blit_buffer(img.tostring(), colorfmt='bgr', bufferfmt='ubyte')