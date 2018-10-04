from kivy.uix.screenmanager import Screen, SlideTransition
from clientes.clientes import LoadDialog
from kivy.uix.popup import Popup

class DocumentosClientes(Screen):
    def go_back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'cliente'


    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()

	
