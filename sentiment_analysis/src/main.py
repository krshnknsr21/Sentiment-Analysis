import kivy
kivy.require('2.0.0')
from Function_Files.Text_Input import Analyzer
from Function_Files.Movie_Review import MovieReviewAnalyzer

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivymd.uix.label import MDLabel

from kivy.properties import ColorProperty, NumericProperty, ListProperty
from kivy.animation import Animation
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivymd.uix.behaviors import RectangularElevationBehavior, FocusBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu

from kivy.uix.label import Label

Builder.load_file('Kivy_files/text_in.kv') 
Builder.load_file('Kivy_files/voice_in.kv')
Builder.load_file('Kivy_files/movies_in.kv')

class AnalyzeApp(MDApp):

    def build(self):
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_file('analyze.kv')

    def process_text_in(self, text):
        text_analysis = Analyzer.testAnalyze(text)
        if(text_analysis == 'Positive'):
            self.root.ids.text_screen.ids.text_in_label.text = text_analysis
            self.root.ids.text_screen.ids.text_in_label.rgb_color = 0, 1, 0, 1
        elif(text_analysis == 'Negative'):
            self.root.ids.text_screen.ids.text_in_label.foreground_color = (0,1,0,1)
            self.root.ids.text_screen.ids.text_in_label.text = text_analysis
        else:
            self.root.ids.text_screen.ids.text_in_label.foreground_color = (0,1,0,1)
            self.root.ids.text_screen.ids.text_in_label.text = text_analysis

    def process_movies_in(self, text):
        in_data = MovieReviewAnalyzer.reviewAnalyzer(text)

        positive_num = in_data[0]['Positive Reviews']
        negative_num = in_data[0]['Negative Reviews']
        neutral_num = in_data[0]['Neutral Reviews']
        
        pos_end = int((positive_num/30)*360)
        neg_end = int(((negative_num/30)*360) + pos_end)
        
        positive_percentage = ((positive_num / 30) * 100)
        negative_percentage = ((negative_num / 30) * 100)
        neutral_percentage = ((neutral_num / 30) * 100)

        print(in_data)

        self.root.ids.movie_screen.ids.pie_chart_pos.start_value = 0
        self.root.ids.movie_screen.ids.pie_chart_pos.end_value = pos_end
        self.root.ids.movie_screen.ids.review_legend_pos.text = ('{:.2f}% Positive Reviews'.format(positive_percentage))
        
        self.root.ids.movie_screen.ids.pie_chart_neg.start_value = pos_end
        self.root.ids.movie_screen.ids.pie_chart_neg.end_value = neg_end
        self.root.ids.movie_screen.ids.review_legend_neg.text = ('{:.2f}% Negative Reviews'.format(negative_percentage))
        
        self.root.ids.movie_screen.ids.pie_chart_nu.start_value = neg_end
        self.root.ids.movie_screen.ids.pie_chart_nu.end_value = 360
        self.root.ids.movie_screen.ids.review_legend_neu.text = ('{:.2f}% Neutral Reviews'.format(neutral_percentage))
        
        self.root.ids.movie_screen.ids.movies_in_label.text = in_data[1]


class CustomLabel(Label):
    start_value = NumericProperty(0)
    end_value = NumericProperty(0)

class CustomTextLabel(Label):
    rgb_color = ColorProperty([1,1,1,1])

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

class CustomLabelInput(Label):
    border_color = ColorProperty([0, 0, 0, 0])
    rect = ListProperty([0, 0, 0, 0])
    _foreground_color = ColorProperty([1, 1, 1, 0])
    lower_border_inactive_color = ColorProperty([.5, .5, .5, 0])

    def _on_label_focused(self, _, active):
        if active:
            self.lower_border_inactive_color = [0, 0, 0, 0]
            self._foreground_color = [1, 1, 1, 1]
            self.border_color = [28/255, 226/255, 231/255, 1]
            Animation(
                d=.3, t='out_bounce',
                rect=[self.x, self.y, self.width, self.height]
                ).start(self)
        else:
            self.border_color = [0, 0, 0, 0]
            self.rect = [
                self.x - dp(10), self.y - dp(10),
                self.width + dp(20), self.height + dp(20)
            ]
            self._foreground_color = [1, 1, 1, 1]
            Animation(lower_border_inactive_color=[.5, .5, .5, 0], d=.3).start(self)
        

if __name__ == "__main__":
    AnalyzeApp().run()