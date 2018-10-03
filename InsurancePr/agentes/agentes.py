from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton	
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

class Agentes(Screen):
    def go_back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'

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


