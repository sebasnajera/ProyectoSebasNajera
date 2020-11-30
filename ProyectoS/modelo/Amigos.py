from tkinter import StringVar #Para asociar los campos de texto con el compomente texto
from tkinter import IntVar #Para asociar los campos de numero con el compomente radio

class Amigos:

    def __init__(self):
        self.nivel_de_amistad = StringVar()
        self.amigos = StringVar()
        self.fk_cedulaOrigen = StringVar()
        self.fk_cedulaDestino = StringVar()
        self.lastUser = ""
        self.lastModificacion = StringVar()
        

    def limpiar(self):
        self.nivel_de_amistad.set("")
        self.amigos.set("")
        self.fk_cedulaOrigen.set("")
        self.fk_cedulaDestino.set("")


    def printInfo(self):
        print(f"Nivel de Amistad:{self.nivel_de_amistad.get()}")
        print(f"Amigos:{self.amigos.get()}")
        print(f"Cedula Origen:{self.fk_cedulaOrigen.get()}")
        print(f"CedulaDestino:{self.fk_cedulaDestino.get()}")