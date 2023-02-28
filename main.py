import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class InsertScreen(Screen):
    def __init__ (self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text ='insert screen'))
                

class PlotScreen(Screen):
    def __init__ (self,**kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text ='titulo'))
        layout.add_widget(Label(text ='grafico'))
        layout.add_widget(Button(text = 'Insert',on_press = self.go_to_insert_screen))
        self.add_widget (layout)
    def go_to_insert_screen(self, *args):
        self.manager.current = 'insert'


        

class ScreenManagement(ScreenManager):
    pass

class MyApp(App):

    def build(self):
        screen_manager = ScreenManagement()
        screen_manager.add_widget(PlotScreen(name = 'plot'))
        screen_manager.add_widget(InsertScreen(name = 'insert'))
        return screen_manager



if __name__ == '__main__':
    MyApp().run()

# class Animal():
#     def __init__(self, nome):
#         self.nome = nome
#     def comunicarse(self):
#         print('Gestos')

# class Cachorro(Animal):
#     def __init__(self, nome, raca):
#         self.nome = nome
#         self.raca = raca
#     def comunicarse(self):
#         super().comunicarse()
#         print('latir')

# luna = Cachorro('Luna', 'Vira lata')