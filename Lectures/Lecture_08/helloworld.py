from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class HelloKv(App):
    message = StringProperty("status")

    def build(self):
        self.title = "Hello world!"
        self.root = Builder.load_file('widget.kv')
        return self.root

    def press_me(self, button):
        self.message = button.text
        # self.root.ids.label_1.text = button.text


# create and  run the program
HelloKv().run()
