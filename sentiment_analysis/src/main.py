import kivy
kivy.require('2.0.0')
from Function_Files.Text_Input import Analyzer
from Function_Files.Movie_Review import MovieReviewAnalyzer

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.properties import ObjectProperty

from kivy.properties import ColorProperty, NumericProperty, ListProperty
from kivy.animation import Animation
from kivy.uix.textinput import TextInput
from kivy.metrics import dp

from kivy.graphics import Ellipse, Color, Rectangle
from kivy.vector import Vector

from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.label import Label
from kivy.uix.button import Button

from random import random
from math import atan2, sqrt, pow, degrees, sin, cos, radians

Builder.load_file('Kivy_files/text_in.kv') 
Builder.load_file('Kivy_files/voice_in.kv')
Builder.load_file('Kivy_files/movies_in.kv')

class AnalyzeApp(MDApp):
    x = None

    def build(self):
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        return Builder.load_file('analyze.kv')
        
    def process_text_in(self, text):
        #print(self.root.ids.movie_screen.ids.movies_in_label)
        self.root.ids.text_screen.ids.text_in_label.text = Analyzer.testAnalyze(text)

    def input_angle_start(self):
        return 

    def input_angle_end(self):
        return int(input("end"))

    def process_movies_in(self, text):
        in_data = MovieReviewAnalyzer.reviewAnalyzer(text)
        print(in_data)
        self.root.ids.movie_screen.ids.movies_in_label.text = in_data[1]#MovieReviewAnalyzer.reviewAnalyzer(text)
        #in_data[0]#MovieReviewAnalyzer.reviewAnalyzer('Joker')

class CustomTextInput(TextInput):
    border_color = ColorProperty([0, 0, 0, 0])
    rect = ListProperty([0, 0, 0, 0])
    _foreground_color = ColorProperty([1, 1, 1, 0])
    lower_border_inactive_color = ColorProperty([.5, .5, .5, 0])

    def _on_textinput_focused(self, _, active):
        if active:
            self.lower_border_inactive_color = [0, 0, 0, 0]
            self._foreground_color = [1, 1, 1, 1]
            self.border_color = [28/255, 226/255, 231/255, 1]
            Animation(
                d=.3, t='out_bounce',
                rect=[self.x, self.y, self.width, self.height]
                ).start(self)
            self.hint_text = 'Enter Your Sentence Here'
        else:
            self.border_color = [0, 0, 0, 0]
            self.rect = [
                self.x - dp(10), self.y - dp(10),
                self.width + dp(20), self.height + dp(20)
            ]
            self._foreground_color = [1, 1, 1, 1]
            Animation(lower_border_inactive_color=[.5, .5, .5, 0], d=.3).start(self)
            self.hint_text = "Enter Your Sentence Here"
        

if __name__ == "__main__":
    AnalyzeApp().run()