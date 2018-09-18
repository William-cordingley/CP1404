from kivy.app import App
from kivy.lang import Builder


class GreeterProgram(App):
    def build(self):
        self.title = "Greeter Program"
        self.root = Builder.load_file("greeterprogram.kv")
        return self.root

    def show_name(self):
        result = self.root.ids.input.text
        self.root.ids.label_1.text = ("Hello {}".format(result))

    def clear_all(self):
        self.root.ids.label_1.text = "Hello"
        self.root.ids.input.text = "insert name here"


GreeterProgram().run()
