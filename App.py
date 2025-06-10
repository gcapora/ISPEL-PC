
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from Programa.screens.conexion import conexionPlaca 
from Programa.screens.generador_pantalla import GeneradoresPantalla
from Programa.screens.informacion import InformacionGeneral

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("UNDAV - Software ISPL")
        self.geometry("1000x700")
        self.conexion = None

        style = ttk.Style()
        style.configure('TNotebook.Tab', font=('Helvetica', 12, 'bold'))  # Fuente grande en las pestañas

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        self.pantallaConexion  = conexionPlaca(self)
        self.pantallaGenerador = GeneradoresPantalla(self, self.pantallaConexion)
        self.informacionGeneral = InformacionGeneral(self)

        # Crear las pestañas principales
        self.pestanaConexionPlaca = ttk.Frame(self.notebook)
        self.pestanaGenerador = ttk.Frame(self.notebook)
        self.informacion = ttk.Frame(self.notebook)  # Pestaña adicional que puede mostrarse cuando se requiere

        # Agregar pestañas
        self.notebook.add(self.pantallaConexion, text='Conexion placa')
        self.notebook.add(self.pantallaGenerador, text='Generador')
        self.notebook.add(self.informacionGeneral, text='Informacion')

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