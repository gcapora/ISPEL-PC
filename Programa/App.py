
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import serial
import time
import serial.tools.list_ports
from PIL import Image, ImageTk

from screens.conexion import conexionPlaca 
from screens.generadores import generadoresSenal

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("UNDAV - Software ISPL")
        self.geometry("600x700")
        self.bgColor = "#747474"
        self.conexion = None

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        self.pantallaConexion  = conexionPlaca(self)
        self.pantallaGenerador = generadoresSenal(self, self.pantallaConexion, "Generador 1", "s1")
        self.pantallaGenerador2 = generadoresSenal(self, self.pantallaConexion, "Generador 2" , "s2")

        # Crear las pestañas principales
        self.pestanaConexionPlaca = ttk.Frame(self.notebook)
        self.pestanaGenerador = ttk.Frame(self.notebook)
        self.pestana_extra = ttk.Frame(self.notebook)  # Pestaña adicional que puede mostrarse cuando se requiere

        # Agregar pestañas
        self.notebook.add(self.pantallaConexion, text='Conexion placa')
        self.notebook.add(self.pantallaGenerador, text='Generador 1')
        self.notebook.add(self.pantallaGenerador2, text='Generador 2')

        self.revisarConexion()

    def revisarConexion(self):
        self.conexion = self.pantallaConexion.estadoConexion()
        if(self.conexion and self.conexion.open):
            self.notebook.tab(self.pantallaConexion, text="Conexion placa [ONLINE]")
        else:
            self.notebook.tab(self.pantallaConexion, text="Conexion placa [OFFLINE]")

        self.after(1000, self.revisarConexion)

if __name__ == "__main__":
    app = App()
    app.mainloop()