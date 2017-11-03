import kivy
kivy.require('1.10.0')
from kivy.lang import Builder
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition

Builder.load_file('main.kv')

class MenuScreen(Screen):

    def changeScreen(self, next_screen):

        self.ids.screen_manager.current = next_screen

#--------------MainClass---------------

class MainApp(App):

    def build(self):
        self.load_sound()
        return MenuScreen()

    def load_sound(self):
        self.sound = SoundLoader.load('Music\IGotLove.mp3')
        self.sound.play()
        self.mute_index = True

    def stop_play_sound(self):
        if self.sound is not None and self.mute_index:
            self.sound.stop()
            self.mute_index = False
        else:
            self.sound.play()
            self.mute_index = True


    def create_text(self):
        self.arr = ['Первый пробный текст', 'Второй пробный текст', 'Третий пробный текст']
        self.pos = 0

    def text_show(self,x):

        if self.pos + x == -1 or self.pos + x == 3:
            pass
        else:
            self.pos += x

        if self.pos > -1 and self.pos < 3:
            return self.arr[self.pos]



if __name__ == '__main__':
    MainApp().run()