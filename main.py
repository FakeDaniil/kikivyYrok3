from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
#Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '500')


class CalculatorApp(App):
    def build(self):
        self.formula = '0'
        if(self.formula == '0'):
            self.formula = ''

        bl = BoxLayout(orientation = 'vertical', padding=5)
        gl = GridLayout(cols=4, spacing=1.1, size_hint=(1, .65))

        self.lbl = Label(text = '0',font_size=40,halign='right',size_hint=(1, .35),text_size=(400 - 50, 500 * .4 -50))

        bl.add_widget(self.lbl)

        gl.add_widget(Button(text="%", font_size=30))
        gl.add_widget(Button(text="", font_size=30))
        gl.add_widget(Button(text="C", font_size=30, on_press=self.c))
        gl.add_widget(Button(text="delet", font_size=30, on_press=self.delet))

        gl.add_widget(Button(text="7",font_size=30,on_press=self.nomber))
        gl.add_widget(Button(text="8",font_size=30,on_press=self.nomber))
        gl.add_widget(Button(text="9",font_size=30,on_press=self.nomber))
        gl.add_widget(Button(text="*",font_size=30,on_press=self.operation))

        gl.add_widget(Button(text="4",font_size=30,on_press=self.nomber))
        gl.add_widget(Button(text="5",font_size=30,on_press=self.nomber))
        gl.add_widget(Button(text="6",font_size=30,on_press=self.nomber))
        gl.add_widget(Button(text="-",font_size=30,on_press=self.operation))

        gl.add_widget(Button(text="1",font_size=30,on_press=self.nomber))
        gl.add_widget(Button(text="2",font_size=30,on_press=self.nomber))
        gl.add_widget(Button(text="3",font_size=30,on_press=self.nomber))
        gl.add_widget(Button(text="+",font_size=30,on_press=self.operation))

        gl.add_widget(Button(text="/",font_size=30,on_press=self.operation))
        gl.add_widget(Button(text="0",font_size=30,on_press=self.nomber))
        gl.add_widget(Button(text=".",font_size=30,on_press=self.nomber))
        gl.add_widget(Button(text="=",font_size=30,on_press=self.result))

        bl.add_widget(gl)

        return bl

    def update_label(self):
        self.lbl.text = self.formula

    def nomber(self,instance):
        self.formula += str(instance.text)
        print(self.formula)
        self.update_label()

    def operation(self,instance):
        self.formula += str(instance.text)
        self.update_label()

    def result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = str(eval(self.lbl.text))

    def delet(self, instance):
        a = len(self.formula) - 1
        self.lbl.text = self.formula[:a]
        self.formula = self.formula[:a]

    def c(self, instance):
        self.lbl.text = ""
        self.formula = ""

if __name__ == "__main__":
    CalculatorApp().run()
