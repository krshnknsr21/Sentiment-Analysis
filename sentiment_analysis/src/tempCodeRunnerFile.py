class CustomLabel(Label):
    start_value = NumericProperty(0)
    end_value = NumericProperty(0)
    
    def draw_pie(self, pos_data):
        x = int((pos_data/30)*360)
        self.end_value = x
    
    def update(self):
        return 150