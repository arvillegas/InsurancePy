from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition, FadeTransition
from kivy.properties import StringProperty, ListProperty
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ListProperty
from connected import Connected
from clientes.clientes import Clientes
from clientes.listaclientes import ListaClientes
from agentes.listaagentes import ListaAgentes
from polizas.listaPolizas import ListaPolizas
from agentes.agentes import Agentes
from polizas.poliza import Polizas
from usuarios.usuarioAdmin import AdminUser
from clientes.documentsclientes import DocumentosClientes
from kivy.lang import Builder
from kivy.config import Config
from test.mainDB import RV
from kivy.uix.popup import Popup
#from agentes.listaclientes import RV


import os

class MainScreen(ScreenManager):
    pass

class ListCliente(Screen, GridLayout):

    buttons = ListProperty([])

    def __init__(self, **kwargs):
        super(ListCliente, self).__init__(**kwargs)
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


class AseguradoraScreen(Screen):
    def do_register(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'agente'

    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        popup = Popup(title='Acceso',
                        content=Label(text='usuario y/o password incorrecto'),
                        size_hint=(None, None), size=(250, 200))

        app.username = loginText
        app.password = passwordText

        if (not (loginText == "agente1") or not (passwordText == "pas1")):
            popup.open()
        else:
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'connected'



        #app.config.read(app.get_application_config())
        #app.config.write()

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

class AseguradoraApp(App):
    username = StringProperty(None)
    password = StringProperty(None)
    screen_names = ListProperty([])

    def build(self):
        manager = ScreenManager()
        listScreen = ListCliente(name='list')
#
        #Window.clearcolor = (.25, .55, .77, .5)
        Window.clearcolor = (.40, .61, .77, .5)
        Window.set_title("Sistema de Aseguradora Demo")
        Window.size = (350, 550)
        #self.size = (400, 300)

        #self.available_screens = sorted([
        #    'Agentes Seguros', 'Clientes', 'Polizas', 'Usuario'])
        #self.screen_names = self.available_screens

        manager.add_widget(AseguradoraScreen(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(Clientes(name='cliente'))
        manager.add_widget(listScreen)
        manager.add_widget(Agentes(name='agente'))
        manager.add_widget(Polizas(name='poliza'))
        manager.add_widget(DocumentosClientes(name='documentsC'))
        manager.add_widget(AdminUser(name='adminUser'))
        manager.add_widget(ListaClientes(name='listaClientes'))
        manager.add_widget(ListaAgentes(name='listaAgentes'))
        manager.add_widget(ListaPolizas(name='listaPolizas'))
        Config.set('graphics', 'width', '200')
        Config.set('graphics', 'height', '200')
        return manager

    def get_application_config(self):
        print("username" + self.username)
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username
        print("conf  "  + conf_directory)

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )


if __name__ == '__main__':
    AseguradoraApp().run()