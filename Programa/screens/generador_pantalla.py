import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from Programa.screens.generadores import generadoresSenal


class GeneradoresPantalla(tk.Frame):
    def __init__(self,master, instanciaConexion):
        super().__init__(master)
        self.conexionSerial = instanciaConexion
        self.layout =  ImageTk.PhotoImage((Image.open("imgs/generadorFrente.png")).resize((300,500)))


        self.pantallaGenerador = generadoresSenal(self, self.conexionSerial, "Salida 1", "s1")
        self.pantallaGenerador2 = generadoresSenal(self, self.conexionSerial, "Salida 2" , "s2")

        self.layoutImg = tk.Label(self, image=self.layout, bg="#2C3E50")



        self.pantallaGenerador.grid(row=0, column=0, padx=10, sticky='nsew')
        self.pantallaGenerador2.grid(row=0, column=2, padx=10, sticky='nsew')

        self.layoutImg.grid(row=0, column=1, padx=10 , sticky='nsew')

        # Configurar la fila para que también pueda expandirse
        self.grid_rowconfigure(0, weight=1)
        