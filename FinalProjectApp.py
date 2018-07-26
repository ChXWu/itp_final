from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
from kivy.graphics import Color, Rectangle

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from functools import partial
from random import randint as r

# Set the initial size of the login interface
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)
Config.write()

class StartMenuLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(StartMenuLayout,self).__init__(**kwargs)


class MainLayout(BoxLayout):
    title = Label(text = 'Eliminates the Jewels',size_hint_y = .1,font_size='25sp')
    # layout for the result section
    result_layout = BoxLayout(orientation = 'horizontal',size_hint_y = .05)
    btn_layout =  BoxLayout(orientation = 'horizontal',size_hint_y = .05)
    score = Label(text = 'Score: 0')
    time_passed = Label(text = 'Time Passed: 0')
    time_remaining = Label(text = 'Time Left: 100')
    btn_start_over = Button(text = 'Start Over')
    btn_return = Button(text = 'Return to Menu')

    #display_layout = GridLayout(padding = 10, spacing = 10, cols = 11, rows = 11)
    def __init__(self, **kwargs):
        super(MainLayout,self).__init__(**kwargs)
        self.result_layout.add_widget(self.score)
        self.result_layout.add_widget(self.time_passed)
        self.result_layout.add_widget(self.time_remaining)
        #with self.result_layout.canvas.before:
        #    Color(0, 1, 0, 1)
        #    self.result_layout.rect = Rectangle(size=self.result_layout.size,
        #                   pos=self.result_layout.pos)
        self.btn_layout.add_widget(self.btn_return)
        self.btn_layout.add_widget(self.btn_start_over)


        self.add_widget(self.title)
        self.add_widget(self.btn_layout)
        self.add_widget(self.result_layout)


        #self.add_widget(self.display_layout)

class FinalProjectApp(App):

    def init_board(self, gameboard_layout, nrows, ncols):
        # possible colors of the Jewels in rgba coodinates
        color_dict = []
        color_dict.append([1, 0, 0, .75])
        color_dict.append([0, 1, 0, .75])
        color_dict.append([0, 0, 1, .75])
        color_dict.append([1, 1, 0, .75])
        color_dict.append([1, 0, 1, .75])
        color_dict.append([0, 1, 1, .75])

        # initialize a matrix to record all the buttons
        btn_matrix = [[0 for j in range(ncols)] for i in range(nrows)]
        # build buttons with random color from the dictionary
        for i in range(nrows):
            for j in range(ncols):
                btn_matrix[i][j] = Button()#text = '({},{})'.format(i,j))
                btn_matrix[i][j].background_normal = ''
                self.init_btn_color(btn_matrix, color_dict, i,j)
                #btn_matrix[i][j].background_color = color_dict[r(0,len(color_dict)-1)]
                gameboard_layout.add_widget(btn_matrix[i][j])
        return btn_matrix

    def init_btn_color(self,btn_matrix, color_dict, i,j):
        used_bc = []
        if i < 2:
            pass
        elif btn_matrix[i-1][j].background_color == btn_matrix[i-2][j].background_color:
            #print (btn_matrix[i-1][j].background_color)
            used_bc.append(btn_matrix[i-1][j].background_color)
        if j < 2:
            pass
        elif btn_matrix[i][j-1].background_color == btn_matrix[i][j-2].background_color:
            #print (btn_matrix[i][j-1].background_color)
            used_bc.append(btn_matrix[i][j-1].background_color)
        for bc in used_bc:
            try:
                color_dict.remove(bc)
            except:
                pass
        btn_matrix[i][j].background_color = color_dict[r(0,len(color_dict)-1)]
        for bc in used_bc:
            color_dict.append(bc)

    def clear_the_layout(layout):
        pass

    def build(self):

        #Window.size = (500, 600)
        ncols,nrows = [10,10]

        # main layout of the game when user is playing
        root = MainLayout(orientation='vertical')
        # add the gameboard to the main layout
        gameboard_layout = GridLayout(padding = 10, spacing = 10, cols = ncols, rows = nrows)
        root.add_widget(gameboard_layout)
        #initialize tht board
        self.init_board(gameboard_layout, ncols, nrows)
        return root


if __name__ == '__main__':
    FinalProjectApp().run()
