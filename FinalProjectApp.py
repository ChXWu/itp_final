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
    play_layout_status,play_layout_btn,\
    play_label_title,play_label_score, \
    play_label_time_passed,play_label_time_left,\
    play_lable_copyright,\
    play_btn_startover,play_btn_return = [0 for i in range(9)]
    menu_btn_start,menu_picture =  [0 for i in range(2)]
    ncols,nrows,score,time_passed,time_left = [10,10,0,0,100]

    def return_to_menu(self,instance):
        self.clear_widgets()
        Window.size = (500,300)
        self.add_widget(self.menu_picture)
        self.add_widget(self.menu_btn_start)
        self.menu_btn_start.bind(on_press = self.start_game)

    def load_board(self):
        self.add_widget(self.play_label_title)
        self.add_widget(self.play_layout_btn)
        self.add_widget(self.play_layout_status)
        # add the gameboard to the main layout
        layout_gameboard = GridLayout(padding = 10, spacing = 10, cols = self.ncols, rows = self.nrows)
        self.add_widget(layout_gameboard)
        self.add_widget(self.play_lable_copyright)
        init_board(layout_gameboard, self.ncols, self.nrows)

    def start_game(self,instance):
        self.clear_widgets()
        Window.size = (500,600)
        #1. initialize and load tht board
        self.load_board()
        # 2. When user click on first jewel, highlight it.
        # 3. If the user did not click on jewels surrunding the first one,
        # 	show warning and restart from 2
        # 4. Else try to switch the first jewel with the second, decide whether it is a succesful move
        # 5.	if it is
        # 6.		switch them,
        # 7.		eliminate aligned jewel,
        # 8.		make the jewels above the eliminated ones fall
        # 9.		add new jewels to the top
        # 9.5       if it causes new aligned jewls go back to 7
        # 10.		add some points for the move to player score
        # 11.		return to step 2
        # 12.	else
        # 13.		report failure
        # 14.		return to step 2

    def __init__(self, **kwargs):
        super(MainLayout,self).__init__(**kwargs)
        self.play_label_title = Label(text = 'Eliminates the Jewels',size_hint_y = .1,font_size='25sp')
        # layout for the status section
        self.play_layout_status = BoxLayout(orientation = 'horizontal',size_hint_y = .05,spacing = 10)
        self.play_layout_btn =  BoxLayout(orientation = 'horizontal',size_hint_y = .05,spacing = 5,padding = 5)
        self.play_label_score = Label(text = 'Score: 0')
        self.play_label_time_passed = Label(text = 'Time Passed: 0')
        self.play_label_time_left = Label(text = 'Time Left: 100')
        self.play_lable_copyright = Label(
            text = 'Made by Changxuan Wu and Shuyang Deng in 2018',
            size_hint_y = .05)
        self.play_btn_startover = Button(text = 'Start Over',
            background_normal = '',background_color = [1,0,0,.9], color = [0,0,0,1])
        self.play_btn_return = Button(text = 'Return to Menu',
            background_normal = '',background_color = [0,1,0,.75], color = [0,0,0,.8])

        self.menu_btn_start = Button(text = 'Start',size_hint_y = 0.2)
        self.menu_picture = Label(text = 'Picture goes here')
        self.menu_textinput = TextInput(text = '10')
        self.menu_textinput2 = TextInput(text = '10')
        self.play_layout_status.add_widget(self.play_label_score)
        self.play_layout_status.add_widget(self.play_label_time_passed)
        self.play_layout_status.add_widget(self.play_label_time_left)
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
