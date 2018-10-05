from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton	
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from clientes.clientes import LoadDialog
from kivy.uix.popup import Popup
from test.mainDB import ConnectionMySql
from kivy.uix.label import Label
import pymysql.cursors
import os

class Agentes(Screen):
    def go_back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'


    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        #with open(os.path.join(path, filename[0])) as stream:
            #for i in range(0,15):
                #print(str(i) + str(self.ids.layoutCliente.children[i].text))

        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()


    def submit_agente(self):
        connection = ConnectionMySql.getConnection()
        print('connection')

        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `agente` ( NoAgente, Nombre, Apellido, Edad, Correo, Telefono, Password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                print('sql')
                cursor.execute(sql, (self.num_agent_text_input.text, self.first_name_text_input.text,self.last_name_text_input.text
                                    ,self.age_agent_text_input.text,self.email_agent_text_input.text,self.phoneagent_text_input.text
                                    ,self.password_agent_input.text))
                print('execute')

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            popupC = Popup(title='Agente',
                content=Label(text='Registro exitoso'),
                size_hint=(None, None), size=(250, 200))
            popupC.open()
            self.manager.transition = SlideTransition(direction="right")
            self.manager.current = 'login'

        except RuntimeError:
            print("Oops!  Error en la base de datos.")
        finally:
            # Close connection.
            connection.close()

class StudentListButton(ListItemButton):
    pass

class CustomDropDown(DropDown):
    pass

dropdown = CustomDropDown()
mainbutton = Button(text='Hello', size_hint=(None, None))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
 
 
class StudentDB(BoxLayout):

     # Connects the value in the TextInput widget to these
    # fields
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    age_text_input = ObjectProperty()
    picture_file_input = ObjectProperty()
    state_select = ObjectProperty()
    student_list = ObjectProperty()

    def submit_student(self):
 
        # Get the student name from the TextInputs
        student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
 
        # Add the student to the ListView
        self.student_list.adapter.data.extend([student_name])
 
        # Reset the ListView
        self.student_list._trigger_reset_populate()
 
    def delete_student(self, *args):
 
        # If a list item is selected
        if self.student_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text
 
            # Remove the matching item
            self.student_list.adapter.data.remove(selection)
 
            # Reset the ListView
            self.student_list._trigger_reset_populate()
 
    def replace_student(self, *args):
 
        # If a list item is selected
        if self.student_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text
 
            # Remove the matching item
            self.student_list.adapter.data.remove(selection)
 
            # Get the student name from the TextInputs
            student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
 
            # Add the updated data to the list
            self.student_list.adapter.data.extend([student_name])
 
            # Reset the ListView
            self.student_list._trigger_reset_populate()


