from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
from kivy.graphics import Color, Rectangle

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from functools import partial
from random import randint as r
import numpy as np
from functools import partial


class MainLayout(BoxLayout):
    # 参数设置
    play_layout_status, play_layout_btn, \
        play_label_title, play_label_score, \
        play_label_time_passed, play_label_time_left, \
        play_lable_copyright, \
        play_btn_startover, play_btn_return = [0 for i in range(9)]
    menu_btn_start, menu_picture = [0 for i in range(2)]

    def return_to_menu(self, instance):
        self.clear_widgets()
        Window.size = (500, 300)
        self.add_widget(self.menu_picture)
        self.add_widget(self.menu_btn_start)
        self.menu_btn_start.bind(on_press=self.start_game)

    def load_board(self):
        self.add_widget(self.play_label_title)
        self.add_widget(self.play_layout_btn)
        self.add_widget(self.play_layout_status)
        # add the gameboard to the main layout
        self.layout_gameboard = GridLayout(
            padding=10, spacing=10, cols=self.ncols, rows=self.nrows)
        self.add_widget(self.layout_gameboard)
        self.add_widget(self.play_lable_copyright)
        self.init_board()

    def button_action(self, i, j, *largs):
        if self.click_count % 2 == 0:
            temp_color = self.btn_matrix[i][j].background_color[:3]
            temp_color.append(1)
            self.btn_matrix[i][j].background_color = temp_color
            self.click_record = [i,j]
        else:
            last_position = self.click_record
            error = abs(last_position[0]-i)+abs(last_position[1]-j) 
            if error == 1:
                temp_button_color = self.btn_matrix[i][j].background_color
                self.btn_matrix[i][j].background_color = self.btn_matrix[last_position[0]][last_position[1]].background_color
                self.btn_matrix[last_position[0]][last_position[1]].background_color = temp_button_color
            elif error > 1:
                i,j = last_position
            temp_color = self.btn_matrix[i][j].background_color[:3]
            temp_color.append(0.75)
            self.btn_matrix[i][j].background_color = temp_color
        self.click_count += 1
        for _ in range(4):
            self.check_score()  


    def check_score(self):
        for i in range(self.nrows):
            for j in range(self.ncols):
                if j+2 < self.nrows:
                    if self.btn_matrix[i][j].background_color == self.btn_matrix[i][j+1].background_color:
                        if self.btn_matrix[i][j].background_color == self.btn_matrix[i][j+2].background_color:
                            self.score += 3
                            for x in range(3):
                                self.init_btn_color(i,j+x)
                if i+2 < self.ncols:
                    if self.btn_matrix[i][j].background_color == self.btn_matrix[i+1][j].background_color:
                        if self.btn_matrix[i][j].background_color == self.btn_matrix[i+2][j].background_color:
                            self.score += 3
                            for x in range(3):
                                self.init_btn_color(i+x,j)
        self.play_label_score.text = 'Score: %d'%self.score

    def init_board(self):
        # possible colors of the Jewels in rgba coodinates
        self.color_dict = []
        self.color_dict.append([1, 0, 0, .75])
        self.color_dict.append([0, 1, 0, .75])
        self.color_dict.append([0, 0, 1, .75])
        self.color_dict.append([1, 1, 0, .75])
        self.color_dict.append([1, 0, 1, .75])
        self.color_dict.append([0, 1, 1, .75])

        # initialize a matrix to record all the buttons
        self.btn_matrix = [
            [0 for j in range(self.ncols)] for i in range(self.nrows)]
        # build buttons with random color from the dictionary
        for i in range(self.nrows):
            for j in range(self.ncols):
                # text = '({},{})'.format(i,j))
                self.btn_matrix[i][j] = Button(
                    on_press=partial(self.button_action, i, j))

                self.btn_matrix[i][j].background_normal = ''
                self.layout_gameboard.add_widget(self.btn_matrix[i][j])
                self.init_btn_color(i, j)
        return self.btn_matrix

    def init_btn_color(self, i, j):
        used_bc = []
        if i < 2:
            pass
        elif self.btn_matrix[i - 1][j].background_color == self.btn_matrix[i - 2][j].background_color:
            used_bc.append(self.btn_matrix[i - 1][j].background_color)
        if j < 2:
            pass
        elif self.btn_matrix[i][j - 1].background_color == self.btn_matrix[i][j - 2].background_color:
            used_bc.append(self.btn_matrix[i][j - 1].background_color)
        for bc in used_bc:
            try:
                self.color_dict.remove(bc)
            except:
                pass
        self.btn_matrix[i][j].background_color = self.color_dict[r(
            0, len(self.color_dict) - 1)]
        for bc in used_bc:
            self.color_dict.append(bc)

    def start_game(self, instance):
        self.clear_widgets()
        self.restart_set()
        Window.size = (500, 500)
        # 1. initialize and load tht board
        self.load_board()
        Clock.schedule_interval(self.time_cal, 0.1)  # x s刷新一次

    def time_cal(self, dt):
        self.time_passed += dt
        self.time_left -= dt
        self.play_label_time_passed.text = 'Time Passed: %.1f' % self.time_passed
        self.play_label_time_left.text = 'Time Left: %.1f' % self.time_left
        self.play_label_score.text = 'Score: %d'%self.score
        if self.time_left <= 0:
            self.clear_widgets()
            self.restart_set()
            Window.size = (500, 500)
            # 1. initialize and load tht board
            self.load_board()

    def restart_set(self):
        self.ncols, self.nrows, self.score, self.time_passed, self.time_left = [
            10, 10, 0, 0, 100]
        self.click_count = 0

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        # 定义一些控件
        self.restart_set()
        self.play_label_title = Label(
            text='Eliminates the Jewels', size_hint_y=.1, font_size='25sp')
        # layout for the status section
        self.play_layout_status = BoxLayout(
            orientation='horizontal', size_hint_y=.05, spacing=10)
        self.play_layout_btn = BoxLayout(
            orientation='horizontal', size_hint_y=.05, spacing=5, padding=5)
        self.play_label_score = Label(text='Score: %d'%self.score)
        self.play_label_time_passed = Label(
            text='Time Passed: %.1f' % self.time_passed)
        self.play_label_time_left = Label(
            text='Time Left: %.1f' % self.time_left)
        self.play_lable_copyright = Label(
            text='Made by Changxuan Wu and Shuyang Deng in 2018',
            size_hint_y=.05)
        self.play_btn_startover = Button(text='Start Over',
                                         background_normal='', background_color=[1, 0, 0, .9], color=[0, 0, 0, 1])
        self.play_btn_return = Button(text='Return to Menu',
                                      background_normal='', background_color=[0, 1, 0, .75], color=[0, 0, 0, .8])

        self.menu_btn_start = Button(text='Start', size_hint_y=0.2)
        self.menu_picture = Label(text='Picture goes here')
        self.menu_textinput = TextInput(text='10')
        self.menu_textinput2 = TextInput(text='10')
        self.play_layout_status.add_widget(self.play_label_score)
        self.play_layout_status.add_widget(self.play_label_time_passed)
        self.play_layout_status.add_widget(self.play_label_time_left)

        self.play_layout_btn.add_widget(self.play_btn_return)
        self.play_layout_btn.add_widget(self.play_btn_startover)

        self.play_btn_return.bind(on_press=self.return_to_menu)
        self.play_btn_startover.bind(on_press=self.start_game)

        self.add_widget(self.menu_picture)
        self.add_widget(self.menu_btn_start)
        self.menu_btn_start.bind(on_press=self.start_game)


class FinalProjectApp(App):
    def build(self):
        # main layout of the game when user is playing
        root = MainLayout(orientation='vertical')
        return root


if __name__ == '__main__':
    FinalProjectApp().run()
