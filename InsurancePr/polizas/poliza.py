from kivy.uix.screenmanager import Screen, SlideTransition


class Polizas(Screen):
    def go_back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'