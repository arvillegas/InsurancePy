from kivy.uix.screenmanager import Screen, SlideTransition
from test.mainDB import ConnectionMySql
from kivy.properties import ObjectProperty
from clientes.clientes import LoadDialog
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
import pymysql.cursors  

class Polizas(Screen):
    num_poliza_text_input= ObjectProperty()
    name_benef_text_input= ObjectProperty()
    last_name_benfe_text_input =ObjectProperty()
    age_benef_text_input = ObjectProperty()
    phone_benef_text_input = ObjectProperty()

    def open_dd_cliente(self, widget):
        self.dropdown = ClienteDropDown(self)           
        self.dropdown.open(widget)

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

    def go_back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'

    def submit_poliza(self):
        connection = ConnectionMySql.getConnection()
        print('connection')
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `poliza` ( NumeroPoliza, NombreBenef, ApellidoBenef, EdiadBenef, TelefonoBenef) VALUES (%s, %s, %s, %s, %s)"
                print('sql')
                cursor.execute(sql, (self.num_poliza_text_input.text, 
                					 self.name_benef_text_input.text,
                					 self.last_name_benfe_text_input.text,
                					 self.age_benef_text_input.text,
                					 self.phone_benef_text_input.text))
                print('execute')

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        except RuntimeError:
            print("Oops!  Error Runtime.")
        finally:
            # Close connection.
            connection.close()


class ClienteDropDown(DropDown):
    def __init__(self, screen_manager, **kwargs):
        super(ClienteDropDown, self).__init__(**kwargs)
        self.sm = screen_manager

    def on_select(self, data):
        self.sm.ids.cliente_select.text = data

class TipoSeguroDropDown(DropDown):
    def __init__(self, screen_manager, **kwargs):
        super(TipoSeguroDropDown, self).__init__(**kwargs)
        self.sm = screen_manager

    def on_select(self, data):
        self.sm.ids.tipo_select.text = data


class PlanDropDown(DropDown):
    def __init__(self, screen_manager, **kwargs):
        super(PlanDropDown, self).__init__(**kwargs)
        self.sm = screen_manager

    def on_select(self, data):
        self.sm.ids.plan_select.text = data