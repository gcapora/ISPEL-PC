import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import time

class generadoresSenal(tk.Frame):
    def __init__(self, maestro, instancia, titulo, generador):
        super().__init__(maestro)
        self.maestro = maestro
        self.instancia = instancia
        self.titulo = titulo
        self.generador = generador
        self.tk = self.master.tk
        self.bgColor = "#747474"
        self.configure(bg="#747474")
        self.senalesOpciones = ["Senoidal", "Cuadrada", "Triangular"]
        self.xx = tk.IntVar()
        self.trianguloImg = tk.PhotoImage(file="imgs/triangular.png", width=100, height=100)
        self.cuadradaImg = tk.PhotoImage(file="imgs/cuadrada.png", width=100, height=100)
        self.senoidalImg = tk.PhotoImage(file="imgs/senoidal.png", width=100, height=100)

        self.trianguloImg =  ImageTk.PhotoImage((Image.open("imgs/triangular.png")).resize((15,15)))
        self.senoidalImg =  ImageTk.PhotoImage((Image.open("imgs/senoidal.png")).resize((15,15)))
        self.cuadradaImg =  ImageTk.PhotoImage((Image.open("imgs/cuadrada.png")).resize((15,15)))

        self.imgSenales = [self.senoidalImg,self.cuadradaImg,self.trianguloImg]
        self.respuesta_var = tk.StringVar()

        self.vcmd = (self.register(self.validar_numero), '%P')

        label = tk.Label(self, 
                 text= self.titulo, 
                 bg=self.bgColor, 
                 fg='black',             
                 font=("Arial", 20, "bold"))
        label.pack(pady=20)


        for index in range(len(self.senalesOpciones)):
            radioButtonsSenoidales = tk.Radiobutton(self, text=self.senalesOpciones[index], variable= self.xx, value=index,
                                                    compound='left', padx=20, pady=20, image=self.imgSenales[index], bg=self.bgColor)
            radioButtonsSenoidales.pack()



        label_frec = tk.Label(self, text="Frecuencia (Hz):", font=('Arial', 14), bg='#747474', fg='red')
        label_frec.pack(padx=10, pady=5)

        self.freqInput = tk.Entry(self, validate='key', validatecommand=self.vcmd, font=('Arial', 20))
        self.freqInput.pack(padx=20, pady=20)

        self.freResponse = tk.Label(self, text=f"Frecuencia (Hz) en repuesta -- Hz", font=('Arial', 14), bg='#747474', fg='yellow')
        self.freResponse.pack(padx=10, pady=5)

        # Botón para empezar envío manual
        boton_enviar = tk.Button(self, text="Cambiar frecuencia", command=self.cmdFreq)
        boton_enviar.pack(padx=20, pady=10)
            

    
    def validar_numero(self,P):
        # Solo permite ingresar dígitos
        return P.isdigit() or P == ""


    def cmdFreq(self):
        tipoSenal = "senoidal"
        try:
            if(self.xx.get() == 0):
                tipoSenal = "senoidal"
            elif(self.xx.get() == 1):
                tipoSenal = "cuadrada"
            elif(self.xx.get() == 2) :
                tipoSenal = "triangular"
            value = self.freqInput.get()
            mensaje = f"gen {self.generador} config frec={value} tipo={tipoSenal}"  # Puedes cambiar el mensaje
            mensaje = mensaje + "\n"
            self.enviar_mensaje(mensaje)
            responseData = self.respuesta_var.get().split(" ")[6].split("=")[1]
            self.freResponse.config(text=f"Frecuencia (Hz) en repuesta {responseData} Hz")
        except:
            self.freResponse.config(text=f"Placa desconectada")

    def enviar_mensaje(self,mensaje):
        print(mensaje)
        ser = self.instancia.estadoConexion()
        print("SER: ",ser)
        if ser and ser.is_open:
            bytes_a_enviar = [b for b in mensaje.encode()]
            # Enviamos todos los bytes en un ciclo simple (bloqueante)
            for b in bytes_a_enviar:
                ser.write(bytes([b]))
                time.sleep(0.001)  # esperar 1 ms entre bytes
            # Leer respuesta
            time.sleep(0.05)  # pequeña pausa para que llegue
            datos = ser.read(1024)
            if datos:
                respuesta = datos.decode('utf-8', errors='ignore')
                self.respuesta_var.set(respuesta)
                print("Respuesta:", respuesta)
            else:
                self.respuesta_var.set("No se recibió respuesta")
        else:
            self.respuesta_var.set("Puerto no disponible")
