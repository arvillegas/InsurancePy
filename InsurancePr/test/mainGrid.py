import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty

kivy.require('1.9.1')


class VelhaGame(Screen):

    buttons = ListProperty([])

    def __init__(self, **kwargs):
        super(VelhaGame, self).__init__(**kwargs)

        self.game_window = BoxLayout(orientation="vertical")
        self.add_widget(self.game_window)

        self.game_table = GridLayout(cols=3,rows=3)

        for i in range(9):
            button = Button(text='', font_size="100sp")
            button.bind(on_release=self.player_turn)
            self.game_table.add_widget(button)
            self.buttons.append(button)

        self.player1 = True

        self.clear_button = Button(on_press=self.clear,text='Clear', font_size="40sp")

        self.game_window.add_widget(self.game_table)
        self.game_window.add_widget(self.clear_button)


    def clear(self,*args):
        for button in self.buttons:
            button.text = ""


    def player_turn(self, button, *args):
        if self.player1 and button.text == '':
            self.player1 = False
            button.text = 'X'
        elif not self.player1 and button.text == '':
            self.player1 = True
            button.text = 'O'


class MainMenu(GridLayout, Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 2
        self.button_play = Button(text='PLAY', font_size="40sp")
        self.button_play.bind(on_release=self.play)
        self.add_widget(self.button_play)
        self.button_exit = Button(text='EXIT', font_size=40)
        self.button_exit.bind(on_release=self.exit)
        self.add_widget(self.button_exit)

    def play(self, *args):
        screen_manager.current = 'velhaPage'

    def exit(self, *args):
        App.get_running_app().stop()


screen_manager = ScreenManager()
screen_manager.add_widget(MainMenu(name='menu'))
screen_manager.add_widget(VelhaGame(name='velhaPage'))


class VelhaGameApp(App):
    def build(self):
        return screen_manager

if __name__ == '__main__':
    VelhaGameApp().run()