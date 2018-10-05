from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.core.image import Image as CoreImage
from clientes.clientes import LoadDialog
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.label import Label
from bson.json_util import dumps
from random import randint
import os
import pymongo
import base64
import json
import io

class DocumentosClientes(Screen):
    varlbldom = ObjectProperty()
    fileInsert = ObjectProperty()
    def go_back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'cliente'


    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        print('documentsclients')
        with open(os.path.join(path, filename[0]), "rb") as stream:
            self.fileInsert = base64.b64encode(stream.read())
            self.varlbldom.text = filename[0]
            picture = Picture(source=filename[0], rotation=randint(-30, 30))
            self.add_widget(picture)

        self.dismiss_popup()

    def retrieveImage(self):
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        mydb = myclient['mydocuments']
        data = mydb["Polizas"].find()
        data1 = json.loads(dumps(data))
        img = data1[0]
        img1 = img['file']
        print(img1['$binary'])
        decode=base64.b64decode(img1['$binary'])
        imageBinary = io.BytesIO(img1['$binary'])
        im = CoreImage(imageBinary, ext="png") 
        image1 = Image(texture=im.texture)
        self.add_widget(image1)

    def dismiss_popup(self):
        self._popup.dismiss()

    def submit_documents(self):
        popupCD = Popup(title='Documento Cliente',
                content=Label(text='Registro exitoso'),
                size_hint=(None, None), size=(250, 200))
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        mydb = myclient['mydocuments']
        mycol = mydb["Polizas"]
        mydict = { "name": "John", "file": self.fileInsert }
        x = mycol.insert_one(mydict)
        print(x)
        popupCD.open()
        #self.retrieveImage()



class Picture(Scatter):

    source = StringProperty(None)
	

