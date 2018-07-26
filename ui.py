from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window

from kivy.config import Config

from functools import partial
from random import randint as r

# Set the initial size of the login interface
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)
Config.write()

class FinalProject(App):

    def intialize_board(self, display_layout, nrows, ncols):
        # colors of the Jewels
        color_dict = {}
        color_dict['Red'] = [1, 0, 0, .75]
        color_dict['Green'] =[0, 1, 0, .75]
        color_dict['Blue'] = [0, 0, 1, .75]
        color_dict['Yellow'] =[1, 1, 0, .75]
        color_dict['Pink'] =[1, 0, 1, .75]
        color_dict['Cyan'] = [0, 1, 1, .75]

        # initialize a matrix to record all the buttons
        btn_matrix = [[0 for j in range(ncols)] for i in range(nrows)]
        # build buttons with random color from the dictionary

        for i in range(nrows):
            for j in range(ncols):
                btn_matrix[i][j] = Button(text = '({},{})'.format(i,j))
                btn_matrix[i][j].background_normal = ''
                btn_matrix[i][j].background_color = list(color_dict.values())[r(0,len(color_dict)-1)]
                display_layout.add_widget(btn_matrix[i][j])
        return btn_matrix

    def intialize_color(btn_matrix, color_dict, i,j):
        try :
            if btn_matrix[i - 2][j].background_color == btn_matrix[i - 1][j].background_color:
                
            pass
        except:
            btn_matrix[i][j].background_color = list(
            color_dict.values())[r(0,len(color_dict)-1)]
    def build(self):
        title = Label(text = 'Eliminates the Jewels',size_hint_y = .05)

        # layout for the result section
        result_layout = BoxLayout(orientation = 'horizontal',size_hint_y = .1)
        score = Label(text = 'Score: 0')
        time_passed = Label(text = 'Time Passed: 0')
        time_remaining = Label(text = 'Time Remaining: 100')
        result_layout.add_widget(score)
        result_layout.add_widget(time_passed)
        result_layout.add_widget(time_remaining)

        # layout for the game board
        # should be able to multify from initial interface
        nrows = 10
        ncols = 10
        display_layout = GridLayout(padding = 10, spacing = 10, cols = ncols, rows = nrows)

        self.intialize_board(display_layout, nrows, ncols)


        root = BoxLayout(orientation='vertical')
        root.add_widget(title)
        root.add_widget(result_layout)
        root.add_widget(display_layout)
        return root


if __name__ == '__main__':
    FinalProject().run()
