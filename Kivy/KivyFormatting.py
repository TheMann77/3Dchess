import kivy
kivy.require('1.0.7')
from kivy.app import App

class MainApp(App):
    def build(self):
        self.a = 'Hi'
    pass

if __name__ == '__main__':
    MainApp().run()
