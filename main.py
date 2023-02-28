import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label

class InsertScreen(Screen):
    def __init__ (self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text ='insert screen'))
                

class PlotScreen(Screen):
    def __init__ (self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text ='plot screen'))

class ScreenManagement(ScreenManager):
    pass

class MyApp(App):

    def build(self):
        screen_manager = ScreenManagement()
        screen_manager.add_widget(InsertScreen(name = 'insert'))
        screen_manager.add_widget(PlotScreen(name = 'plot'))
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