import kivy

kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.core.audio import SoundLoader

Builder.load_file('Try.kv')

class MyFloatLayout(FloatLayout):
    pass

class FondApp(App):
    def build(self):
        self.load_sound()
        return MyFloatLayout()

    def load_sound(self):
        self.sound = SoundLoader.load('D:\Game\Sounds\IGotLove.mp3')
        self.sound.play()

    def stop_sound(self):
        if self.sound is not None:
            self.sound.stop()

if __name__ == '__main__':
    FondApp().run()

