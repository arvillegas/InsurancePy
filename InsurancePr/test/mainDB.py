import sqlite3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup
import pymysql.cursors
import os

class ConnectionMySql():
    def getConnection():
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='toor',                             
                                     db='aseguradoradb',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        return connection

class TextInputPopup(Popup):
    obj = ObjectProperty(None)
    obj_text = StringProperty("")

    def __init__(self, obj, **kwargs):
        super(TextInputPopup, self).__init__(**kwargs)
        self.obj = obj
        self.obj_text = obj.text


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected

    def on_press(self):
        popup = TextInputPopup(self)
        popup.open()

    def update_changes(self, txt):
        self.text = txt


class RV(BoxLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):
        path = r"C:\Users\Avillegas\Documents\sqlDir"
        rows = ObjectProperty()
        #connection = sqlite3.connect(os.path.join(path, u"test.db"))
        connection = ConnectionMySql.getConnection()
        print(connection)
        self.data_items.clear()

        with connection.cursor() as cursor:
            cursor.execute("SELECT idCliente, Nombre, Apellido, Edad FROM cliente")
            rows = cursor.fetchall()
            for row in rows:
                self.data_items.append(row['idCliente'])
                self.data_items.append(row['Nombre'])
                self.data_items.append(row['Apellido'])
                self.data_items.append(row['Edad'])
                self.data_items.append('...')

        #cursor = connection.cursor()

        #cursor.execute("SELECT * FROM Usuarios")
        #rows = cursor.fetchall()

        # create data_items


class RVAgentes(BoxLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(RVAgentes, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):
        path = r"C:\Users\Avillegas\Documents\sqlDir"
        connection = sqlite3.connect(os.path.join(path, u"test.db"))
        print(connection)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Usuarios")
        rows = cursor.fetchall()
        # create data_items
        for row in rows:
            for col in row:
                self.data_items.append(col)

class RVPolizas(BoxLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(RVPolizas, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):
        path = r"C:\Users\Avillegas\Documents\sqlDir"
        rows = ObjectProperty()
        #connection = sqlite3.connect(os.path.join(path, u"test.db"))
        connection = ConnectionMySql.getConnection()
        print(connection)
        self.data_items.clear()
        with connection.cursor() as cursor:
            cursor.execute("SELECT idPoliza, NombreBenef, ApellidoBenef, EdiadBenef FROM poliza")
            rows = cursor.fetchall()
            for row in rows:
                self.data_items.append(row['idPoliza'])
                self.data_items.append(row['NombreBenef'])
                self.data_items.append(row['ApellidoBenef'])
                self.data_items.append(row['EdiadBenef'])
                self.data_items.append('...')


class TestApp(App):
    title = "Kivy RecycleView & SQLite3 Demo"

    def build(self):
        return RV()


if __name__ == "__main__":
    TestApp().run()