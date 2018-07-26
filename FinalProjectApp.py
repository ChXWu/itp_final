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
Config.set('graphics', 'height', '300')
Config.set('graphics', 'resizable', False)
Config.write()

class MainLayout(BoxLayout):
    play_label_title = Label(text = 'Eliminates the Jewels',size_hint_y = .1,font_size='25sp')
    # layout for the result section
    play_layout_result = BoxLayout(orientation = 'horizontal',size_hint_y = .05,spacing = 10)
    play_layout_btn =  BoxLayout(orientation = 'horizontal',size_hint_y = .05,spacing = 5,padding = 5)
    play_label_score = Label(text = 'Score: 0')
    play_label_time_passed = Label(text = 'Time Passed: 0')
    play_label_time_left = Label(text = 'Time Left: 100')
    play_lable_copyright = Label(
        text = 'Made by Changxuan Wu and Shuyang Deng in 2018',
        size_hint_y = .05)
    play_btn_startover = Button(text = 'Start Over',
        background_normal = '',background_color = [1,0,0,.9], color = [0,0,0,1])
    play_btn_return = Button(text = 'Return to Menu',
        background_normal = '',background_color = [0,1,0,.75], color = [0,0,0,.8])

    menu_btn_start = Button(text = 'Start',size_hint_y = 0.2)
    menu_picture = Label(text = 'Picture goes here')
    menu_textinput = TextInput(text = '10')
    menu_textinput2 = TextInput(text = '10')
    ncols,nrows,score,time_passed,time_left = [10,10,0,0,100]

    def return_to_menu(self,instance):
        self.clear_widgets()
        Window.size = (500,300)
        self.add_widget(self.menu_picture)
        self.add_widget(self.menu_btn_start)
        self.menu_btn_start.bind(on_press = self.start_game)

    def start_game(self,instance):
        self.clear_widgets()
        Window.size = (500,600)
        self.add_widget(self.play_label_title)
        self.add_widget(self.play_layout_btn)
        self.add_widget(self.play_layout_result)
        # add the gameboard to the main layout
        layout_gameboard = GridLayout(padding = 10, spacing = 10, cols = self.ncols, rows = self.nrows)
        self.add_widget(layout_gameboard)
        self.add_widget(self.play_lable_copyright)
        #initialize tht board
        init_board(layout_gameboard, self.ncols, self.nrows)
    #display_layout = GridLayout(padding = 10, spacing = 10, cols = 11, rows = 11)
    def __init__(self, **kwargs):
        super(MainLayout,self).__init__(**kwargs)
        self.play_layout_result.add_widget(self.play_label_score)
        self.play_layout_result.add_widget(self.play_label_time_passed)
        self.play_layout_result.add_widget(self.play_label_time_left)
        #with self.result_layout.canvas.before:
        #    Color(0, 1, 0, 1)
        #    self.result_layout.rect = Rectangle(size=self.result_layout.size,
        #                   pos=self.result_layout.pos)
        self.play_layout_btn.add_widget(self.play_btn_return)
        self.play_layout_btn.add_widget(self.play_btn_startover)

        self.play_btn_return.bind(on_press = self.return_to_menu)
        self.play_btn_startover.bind(on_press = self.start_game)

        self.add_widget(self.menu_picture)
        self.add_widget(self.menu_btn_start)
        self.menu_btn_start.bind(on_press = self.start_game)


        #self.add_widget(self.display_layout)

def init_board(gameboard_layout, nrows, ncols):
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
            init_btn_color(btn_matrix, color_dict, i,j)
            #btn_matrix[i][j].background_color = color_dict[r(0,len(color_dict)-1)]
            gameboard_layout.add_widget(btn_matrix[i][j])
    return btn_matrix

def init_btn_color(btn_matrix, color_dict, i,j):
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

class FinalProjectApp(App):
    def build(self):
        ncols,nrows = [10,10]
        # main layout of the game when user is playing
        root = MainLayout(orientation='vertical')
        return root


if __name__ == '__main__':
    FinalProjectApp().run()
