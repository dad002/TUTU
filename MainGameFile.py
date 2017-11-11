import kivy
kivy.require('1.10.0')
from kivy.lang import Builder
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition

#TODO перепишы screen manager

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


    def create_text(self, chapter):
        self.pos = 0
        input = open('Story\Chapter_'+str(chapter), 'r', encoding='UTF-8')
        self.A=[]
        while True:
            tmp = input.readline().rsplit()
            if tmp == []:
                break
            else:
                self.A.append(tmp)

        for i in range(len(self.A)):
            self.A[i]=" ".join(list(map(str,self.A[i])))





    def text_show(self,x):
        #TODO тута надо будет доделать чтобы после прочтения вызывался следующий экран и чтобы это работало для каждой главы

        if self.pos + x == -1 or self.pos + x == 3:
            pass
        else:
            self.pos += x

        if self.pos > -1 and self.pos < 3:
            return str(self.A[self.pos])



if __name__ == '__main__':
    MainApp().run()