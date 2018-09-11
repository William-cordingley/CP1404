miles_to_kilometers = 1.60934

from kivy.app import App
from kivy.lang import Builder


class Converter(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("converter.kv")
        return self.root

    def convert_m_to_k(self):
        value = self.get_miles()
        result = value * miles_to_kilometers
        self.root.ids.output_label.text = str(result)

    def get_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0
