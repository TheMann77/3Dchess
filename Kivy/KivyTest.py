from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import numpy as np

rows = 8
columns = 8
boards = 3
board = []
for a in range(boards):
    board.append([])
    for b in range(columns):
        board[-1].append([])
        for x in range(rows):
            board[-1][-1].append('  ')
board = np.array(board, dtype=object)
board[0,0,0] = 'R'

class MainApp(App):
    def build(self):
        self.main_layout = FloatLayout()

        for a in range(boards):
            for b in range(rows):
                for c in range(columns):
                    button = Button(text=board[a,b,c], font_size='20sp', pos_hint={'x':0.125*c, 'y':25/26-b/26-a*9/26}, size_hint=(.125, 1/26), background_color=[.96,.96,.78] if (a+b+c)%2 == 0 else [.88,.78,.6])
                    button.bind(on_press=self.on_button_press)
                    self.main_layout.add_widget(button)

        return self.main_layout

    def on_button_press(self, instance):
        board[0,0,1]='N'
        instance.text='N'

if __name__ == '__main__':
    app = MainApp()
    app.run()

