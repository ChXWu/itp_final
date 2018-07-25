from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.anchorlayout import AnchorLayout

from kivy.core.window import Window
from functools import partial

class UserInputLayout(BoxLayout):
    user_input = TextInput(multiline = False)
    def __init__(self, **kwargs):
        super(UserInputLayout, self).__init__(**kwargs)
        self.user_input = TextInput(text = "Enter Something", multiline = False)
        self.add_widget(self.user_input)
        self.btn_start = Button(text='Start', size_hint_x = .3)
        self.add_widget(self.btn_start)


class FinalProject(App):
    def display_user_input(self, display_layout, input_layout,*largs):
        display_layout.add_widget(Label(text= input_layout.user_input.text))

    def build(self):
        Window.size = (500, 400)

        display_layout = GridLayout(cols = 3)
        user_input_layout = UserInputLayout(
            spacing = 5, padding = 5,orientation='horizontal', size_hint_y = .2)

        user_input_layout.btn_start.bind(on_press = partial(
            self.display_user_input,display_layout,user_input_layout))


        root = BoxLayout(orientation='vertical', size = (200,100))
        root.add_widget(display_layout)
        root.add_widget(user_input_layout)
        return root


if __name__ == '__main__':
    FinalProject().run()
