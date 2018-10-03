from kivy.uix.screenmanager import Screen, SlideTransition
from test.mainDB import RV
from kivy.uix.button import Button

class ListaClientes(Screen):
    def __init__(self, **kwargs):
    	super(ListaClientes, self).__init__(**kwargs)
    	button = Button(text='Regresar',size_hint=(None,None), width=200, height=100)
    	button.bind(on_release=self.go_back)
    	rv = RV()
    	self.add_widget(button)
    	self.add_widget(rv)

    def go_back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
