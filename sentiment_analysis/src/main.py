import kivy
kivy.require('2.0.0')
import Text_Voice_Input as process_text
import Movie_Review as process_movies

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

Builder.load_file('Kivy_files/text_in.kv') 
Builder.load_file('Kivy_files/voice_in.kv')
Builder.load_file('Kivy_files/movies_in.kv')
Builder.load_file('Kivy_files/nav_bar.kv')
Builder.load_file('Kivy_files/main_window.kv')

class Analyze(AnchorLayout):
    pass

class AnalyzeApp(App):
    analysis = ['hello']

    global_widgets = {}
    ''' interface for  global widget access '''
    def register_widget(self, widget_object):
        if widget_object.gid not in self.global_widgets:
            self.global_widgets[widget_object.gid] = widget_object
    
    def get_widget(self, widget_gid):
        ''' returns widget if it is registered '''
        if widget_gid in self.global_widgets:
            return self.global_widgets[widget_gid]
        else:
            return None
    
    def build(self):
        return Analyze()
    
    def process_text_in(self, text):
        self.get_widget('text_in_label').text =  process_text.Analyzer.testAnalyze(text)

    def process_movies_in(self, text):
        self.get_widget('movies_in_label').text =  process_movies.MovieReviewAnalyzer.reviewAnalyzer(text)


if __name__ == "__main__":
    AnalyzeApp().run()