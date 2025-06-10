import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import serial
import serial.tools.list_ports
from PIL import Image, ImageTk

class conexionPlaca(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.puerto_var = tk.StringVar()
        self.ser = None


        self.logoUndavImg = tk.PhotoImage(file="imgs/undavLogo.png", width=100, height=100)
        self.logoUndavImg = ImageTk.PhotoImage((Image.open("imgs/undavLogo.png")).resize((400,200)))
        icon_label = tk.Label(self, image=self.logoUndavImg, bg="#2C3E50")
        icon_label.pack(padx=5, pady=10)



        # Parte mejorada
        self.config(bg="#2C3E50")  # Fondo general



        # etiqueta descriptiva
        label = tk.Label(
            self, 
            text='Seleccione el puerto donde se encuentra la placa conectada',
            bg="#2C3E50",
            fg='white',
            font=("Helvetica Neue", 16, "bold")
        )
        label.pack(pady=20)
        
        self.puerto_var = tk.StringVar()

        self.menu_puertos = tk.OptionMenu(
            self, 
            self.puerto_var, 
            "",
        )
        self.menu_puertos.pack(padx=10, pady=10, fill='x')


                # Botón con estilo moderno
        self.btn_actualiarPuertos = ctk.CTkButton(
            self,
            text="Actualizar",
            width=140,
            height=40,
            command=self.listar_puertos,
            corner_radius=8,
            fg_color="#37E6AF",      # Verde moderno
            hover_color="#1facc1",
            font=("Helvetica Neue", 14, "bold")
        )
        self.btn_actualiarPuertos.pack(padx=10, pady=10)





        # Botón con estilo moderno
        self.btn_conectar = ctk.CTkButton(
            self,
            text="Conectar",
            width=140,
            height=40,
            command=self.conectar,
            corner_radius=8,
            fg_color="#4CAF50",      # Verde moderno
            hover_color="#45a049",
            font=("Helvetica Neue", 14, "bold")
        )
        self.btn_conectar.pack(padx=10, pady=10)

        # Estado
        self.status_label = tk.Label(
            self,
            text="Estado",
            bg="#7F8C8D",
            fg='white',
            font=('Helvetica Neue', 12, "bold"),
            relief='raised',
            bd=1
        )
        self.status_label.pack(padx=10, pady=10, fill='x')


        self.listar_puertos()


    def listar_puertos(self):
        puertos = serial.tools.list_ports.comports()
        opciones_display = []
        for p in puertos:
            info = f"{p.device} - {p.description}"
            opciones_display.append(info)
        # Actualiza el OptionMenu
        self.menu_puertos['menu'].delete(0, 'end')
        for o in opciones_display:
            p_device = o.split(' - ')[0]
            self.menu_puertos['menu'].add_command(
                label=o,
                command=lambda p=p_device: self.puerto_var.set(p))
        # Selecciona la primera opción si hay
        if opciones_display:
            self.puerto_var.set(opciones_display[0].split(' - ')[0])
        return [o.split(' - ')[0] for o in opciones_display]

    def conectar(self):
        seleccion = self.puerto_var.get()
        try:
            self.ser = serial.Serial(seleccion, 115200, timeout=1)
            self.status_label.config(text=f"Conectado a {seleccion}", bg='green')
            self.btn_conectar.configure(
            text="Desconectar",
            fg_color="red",
            hover_color="darkred"
        )
        except Exception as e:
            self.ser = None
            self.status_label.config(text=f"Error: {e}", bg='red')
            self.btn_conectar.configure(
            text="Conectar",
            fg_color="green",
            hover_color="darkred")

    def estadoConexion(self):
        return self.ser