from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton	
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import pymysql.cursors  

class Clientes(Screen):

    def __init__(self, **kwargs):
        super(Clientes, self).__init__(**kwargs)

    def go_back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'

    def go_documents(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'documentsC'

    def open_drop_down(self, widget):
        self.dropdown = EstadoDropDown(self)           
        self.dropdown.open(widget)

    def open_drop_down_municipio(self, widget):
        self.dropdown = MunicipioDropDown(self)           
        self.dropdown.open(widget)

    # Function return a connection.
    def getConnection(self):
     
    # You can change the connection arguments.
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='toor',                             
                                     db='aseguradoradb',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection

    def submit_client(self):
        connection = self.getConnection()
        print('connection')
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `cliente` ( Nombre, Apellido, Edad) VALUES (%s, %s, %s)"
                print('sql')
                cursor.execute(sql, (self.first_name_text_input.text, self.last_name_text_input.text,self.age_text_input.text))
                print('execute')

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        except RuntimeError:
            print("Oops!  Error Runtime.")
        finally:
            # Close connection.
            connection.close()

    loadfile = ObjectProperty(None)

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


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class EstadoDropDown(DropDown):
    def __init__(self, screen_manager, **kwargs):
        super(EstadoDropDown, self).__init__(**kwargs)
        self.sm = screen_manager

    def on_select(self, data):
        self.sm.ids.state_select.text = data

class MunicipioDropDown(DropDown):
    def __init__(self, screen_manager, **kwargs):
        super(MunicipioDropDown, self).__init__(**kwargs)
        self.sm = screen_manager

    def on_select(self, data):
        self.sm.ids.city_select.text = data
 
 
