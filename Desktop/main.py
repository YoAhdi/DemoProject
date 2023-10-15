import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self,**kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text = 'Student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)


        self.add_widget(Label (text='Student Grades'))
        self.s_grades = TextInput ()
        self.add_widget(self.s_grades)

        self.add_widget(Label(text='Student hometown'))
        self.s_city = TextInput()
        self.add_widget(self.s_city)

        self.press = Button(text = 'Done')
        self.press.bind(on_press = self.done)
        self.add_widget(self.press)

    def done(self, instance):
        print("Name of Student is " + self.s_name.text)
        print("Name of Student is " + self.s_grades.text)
        print("Name of Student is " + self.s_city.text)
        print("")

class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()



