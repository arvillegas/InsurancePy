from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition

class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def go_clientes(self):
	    self.manager.transition = SlideTransition(direction="left")
	    self.manager.current = 'cliente'

    def go_listClientes(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'listaClientes'
        #self.manager.current = 'list'

    def go_listAgentes(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'listaAgentes'

    def go_listPolizas(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'listaPolizas'

    def go_Agentes(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'agente'

    def go_Polizas(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'poliza'

    def go_User(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'adminUser'

    def go_CloseSesion(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()