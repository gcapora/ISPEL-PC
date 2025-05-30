import tkinter as tk
import customtkinter as ctk
import serial
import serial.tools.list_ports

class conexionPlaca(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="#747474")
        self.baud_rates =  ['9600', '115200', '57600', '38400', '19200', '2400', '4800', '300']
        self.puerto_var = tk.StringVar()
        self.ser = None

        label = tk.Label(self, text='Seleccione el puerto donde se encuentra la placa conectada',bg="#747474", 
                 fg='black',             
                 font=("Arial", 16, "bold"))
        label.pack(pady=20)

        # hacer que sea un atributo de la clase
        self.menu_puertos = tk.OptionMenu(self, self.puerto_var, "")
        self.menu_puertos.pack(padx=10, pady=10, fill='x')

        self.combo_baud = ctk.CTkComboBox(
            self,
            values=self.baud_rates,
            width=120,
            height=30,
           
)
        self.combo_baud.pack(padx=20, pady=20)

        # Botón para conectar
        self.btn_conectar = ctk.CTkButton(
            self,
            text="Conectar",
            width=120,        # Ancho en píxeles
            height=40,        # Alto en píxeles
            command=self.conectar,
            corner_radius=8,  # Esquinas un poco redondeadas (valor en píxeles)
            fg_color="#4CAF50",  # Color del fondo (verde en este ejemplo)
            hover_color="#45a049" # Color al pasar el cursor
        )
        self.btn_conectar.pack(padx=10, pady=10)


        # Estado
        self.status_label = tk.Label(self, text="Estado", bg='gray', fg='white', font=('Arial', 12))
        self.status_label.pack(padx=10, pady=10, fill='x')

        # Llenar los puertos disponibles en el OptionMenu
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
        seleccionBauds = int(self.combo_baud.get())
        try:
            self.ser = serial.Serial(seleccion, seleccionBauds, timeout=1)
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