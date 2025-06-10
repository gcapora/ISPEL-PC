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
        self.estadoGenerador = 'encendido'
        self.tk = self.master.tk
                # Configuración del estilo visual
        self.configure(bg="#2C3E50", bd=2, relief='ridge')
        self.senalesOpciones = ["Senoidal", "Cuadrada", "Triangular"]
        self.xx = tk.IntVar()
        self.trianguloImg = tk.PhotoImage(file="imgs/triangular.png", width=100, height=100)
        self.cuadradaImg = tk.PhotoImage(file="imgs/cuadrada.png", width=100, height=100)
        self.senoidalImg = tk.PhotoImage(file="imgs/senoidal.png", width=100, height=100)

        self.trianguloImg =  ImageTk.PhotoImage((Image.open("imgs/triangular.png")).resize((50,50)))
        self.senoidalImg =  ImageTk.PhotoImage((Image.open("imgs/senoidal.png")).resize((60,60)))
        self.cuadradaImg =  ImageTk.PhotoImage((Image.open("imgs/cuadrada.png")).resize((50,50)))

        self.imgSenales = [self.senoidalImg,self.cuadradaImg,self.trianguloImg]
        self.respuesta_var = tk.StringVar()

        self.vcmd = (self.register(self.validar_numero), '%P')

        # Título
        label_titulo = tk.Label(self, text=titulo, font=("Arial", 22, "bold"), bg="#2C3E50", fg='white')
        label_titulo.pack(pady=15)


        self.tituloConfiguracionPlaca = tk.Label(self, text="Configuracion generador", font=('robot', 18), bg="#2C3E50", fg='white')
        self.tituloConfiguracionPlaca.pack(padx=10, pady=5)

        # Frame para radio buttons con iconos
        radio_frame = tk.Frame(self, bg="#2C3E50")
        radio_frame.pack(pady=10)

        # Crear radio buttons con iconos
        for index in range(len(self.senalesOpciones)):
            option_frame = tk.Frame(radio_frame, bg="#2C3E50")
            option_frame.pack(side='left', padx=10)

            rb = tk.Radiobutton(
                option_frame,
                text=self.senalesOpciones[index],
                variable=self.xx,
                value=index,
                bg="#2C3E50",
                fg='white',
                selectcolor="#16A085",
                font=("Arial", 12)
            )
            rb.pack(side='left')

            icon_label = tk.Label(option_frame, image=self.imgSenales[index], bg="#2C3E50")
            icon_label.pack(side='left', padx=5)

        self.vcmd = (self.register(self.validar_numero), '%P')
        self.vcmdNegativo = (self.register(self.validar_numero_negativo), '%P')

        label_fase = tk.Label(self, text="FASE (0° - 360°):", font=('Arial', 14), bg="#2C3E50", fg='orange')
        label_fase.pack(padx=10, pady=5)

        self.faseInput = tk.Entry(self, validate='key', validatecommand=self.vcmd, font=('Arial', 14))
        self.faseInput.pack(padx=20, pady=10)

      # Etiqueta y entrada para frecuencia con validación
        label_frec = tk.Label(self, text="Frecuencia (Hz):", font=('Arial', 14), bg="#2C3E50", fg='orange')
        label_frec.pack(padx=10, pady=5)


        # Validación para entrada numérica
        self.freqInput = tk.Entry(self, validate='key', validatecommand=self.vcmd, font=('Arial', 14))
        self.freqInput.pack(padx=20, pady=10)


              # Etiqueta y entrada para vmax con validación
        label_vmin = tk.Label(self, text="Vmin (V):", font=('Arial', 14), bg="#2C3E50", fg='orange')
        label_vmin.pack(padx=10, pady=5)

                # Validación para entrada numérica
        self.vminInput = tk.Entry(self, validate='key', validatecommand=self.vcmdNegativo, font=('Arial', 14))
        self.vminInput.pack(padx=20, pady=10)



      # Etiqueta y entrada para vmin con validación
        label_vmax = tk.Label(self, text="Vmax (V):", font=('Arial', 14), bg="#2C3E50", fg='orange')
        label_vmax.pack(padx=10, pady=5)

                        # Validación para entrada numérica
        self.vmaxInput = tk.Entry(self, validate='key', validatecommand=self.vcmdNegativo, font=('Arial', 14))
        self.vmaxInput.pack(padx=20, pady=10)



        # Frame para contener los botones
        boton_frame = tk.Frame(self, bg="#2C3E50")
        boton_frame.pack(pady=15)

        # Botón para Configurar
        self.boton_enviar = tk.Button(
            boton_frame,  # Usar el Frame como padre
            text="Configurar",
            bg='#2980B9',
            fg='white',
            font=('Arial', 14, 'bold'),
            command=self.cmdFreq
        )
        self.boton_enviar.pack(side=tk.LEFT, padx=10)

        # Botón para Información
        self.boton_informacion = tk.Button(
            boton_frame,  # Usar el Frame como padre
            text="Obtener estado",
            bg='#2980B9',
            fg='white',
            font=('Arial', 14, 'bold'),
            command=self.obtenerStatusGenerador
        )
        self.boton_informacion.pack(side=tk.LEFT, padx=10)

        # Botón para Información
        self.btn_on_off = tk.Button(
            boton_frame,  # Usar el Frame como padre
            text="Encender",
            bg="#19CD19",
            fg='white',
            font=('Arial', 14, 'bold'),
            command=self.habilitarGenerador
        )
        self.btn_on_off.pack(side=tk.LEFT, padx=10)

        self.repuestaGeneralesPlaca = tk.Label(self, text="", font=('robot', 18, 'bold'), bg="#2C3E50", fg='red')
        self.repuestaGeneralesPlaca.pack(padx=10, pady=5)


        separator = ttk.Separator(self, orient='horizontal')
        separator.pack(fill='x', padx=10, pady=10)

        self.tituloRespuestasPlaca = tk.Label(self, text="Respuesta de placa", font=('robot', 18), bg="#2C3E50", fg='white')
        self.tituloRespuestasPlaca.pack(padx=10, pady=5)

        # Etiqueta de respuesta desde placa - frecuencia
        self.freResponse = tk.Label(self, text="Frecuencia (Hz) en respuesta -- Hz", font=('Arial', 14), bg="#2C3E50", fg='yellow')
        self.freResponse.pack(padx=10, pady=5)

        # Etiqueta de respuesta desde placa - fase
        self.faseResponse = tk.Label(self, text="Fase (°) --°", font=('Arial', 14), bg="#2C3E50", fg='yellow')
        self.faseResponse.pack(padx=10, pady=5)


        # Etiqueta de respuesta desde placa - Tipo senal
        self.signalResponse = tk.Label(self, text="Tipo senal --", font=('Arial', 14), bg="#2C3E50", fg='yellow')
        self.signalResponse.pack(padx=10, pady=5)

        # Etiqueta de respuesta desde placa - Tipo senal
        self.vminResponse = tk.Label(self, text="Vmin (V) -- V", font=('Arial', 14), bg="#2C3E50", fg='yellow')
        self.vminResponse.pack(padx=10, pady=5)

        # Etiqueta de respuesta desde placa - Tipo senal
        self.vmaxResponse = tk.Label(self, text="Vmax (V) -- V", font=('Arial', 14), bg="#2C3E50", fg='yellow')
        self.vmaxResponse.pack(padx=10, pady=5)

    
    def validar_numero(self,P):
        # Solo permite ingresar dígitos
        return P.isdigit() or P == ""

    def validar_numero_negativo(self,P):
        if P == "" or P == "-":
            return True
        try:
            float(P)
            return True
        except ValueError:
            return False


    def cmdFreq(self):
        self.boton_enviar.config(text="Cargando....")
        tipoSenal = "senoidal"
        try:
            if(self.xx.get() == 0):
                tipoSenal = "senoidal"
            elif(self.xx.get() == 1):
                tipoSenal = "cuadrada"
            elif(self.xx.get() == 2) :
                tipoSenal = "triangular"
            value = self.freqInput.get()
            faseSeleccion = self.faseInput.get()
            mensaje = f"gen {self.generador} config frec={value} tipo={tipoSenal} FASE={faseSeleccion} VMAX={self.vmaxInput.get()} VMIN={self.vminInput.get()}"
            mensaje = mensaje + "\n"
            self.enviar_mensaje(mensaje)
            responseData = self.respuesta_var.get().split(" ")[6].split("=")[1]
            responseSignal = self.respuesta_var.get().split(" ")[4].split("=")[1]
            responseFase = self.respuesta_var.get().split(" ")[7].split("=")[1]
            responseVmin = self.respuesta_var.get().split(" ")[9].split("=")[1]
            responseVmax = self.respuesta_var.get().split(" ")[8].split("=")[1]
            
            self.freResponse.config(text=f"Frecuencia (Hz) en repuesta {responseData} Hz")
            self.signalResponse.config(text=f"Tipo senal {responseSignal}")
            self.faseResponse.config(text=f"Fase (°) {responseFase}°")
            self.vminResponse.config(text=f"Vmin (V) {responseVmin}V")
            self.vmaxResponse.config(text=f"Vmax (V) {responseVmax}V")
        except:
            self.freResponse.config(text=f"Placa desconectada")
            self.signalResponse.config(text=f"")
            self.faseResponse.config(text=f"")
            self.vminResponse.config(text=f"")
            self.vmaxResponse.config(text=f"")
        finally:
            self.boton_enviar.config(text="Configurar", state="active")


    def habilitarGenerador(self):
        # Determinar el mensaje según el estado actual
        if self.estadoGenerador == 'encendido':
            mensaje = f"gen {self.generador} apagar\n"
        elif self.estadoGenerador == 'apagado':
            mensaje = f"gen {self.generador} encender\n"

        print("mensaje: ", mensaje)
        self.enviar_mensaje(mensaje)

        # Analizar la respuesta y actualizar la interfaz
        respuesta = self.respuesta_var.get()
        print(f"RES: -{respuesta}-")

        estado = respuesta.split(" ")[3]  # Obtener el estado de la respuesta
        estadoLimpio = estado.split(".")[0]
        print(f"estado: ={estadoLimpio}=")
        if estadoLimpio == 'encendido':
            self.btn_on_off.config(text="Apagar",bg="#CD191F",)
            self.estadoGenerador = 'encendido'  # Corregir asignación
            self.repuestaGeneralesPlaca.config(text="")
        elif estadoLimpio == 'apagado':
            self.btn_on_off.config(text="Encender", bg="#19CD3D",)
            self.estadoGenerador = 'apagado'  # Corregir asignación
            self.repuestaGeneralesPlaca.config(text="")
        elif estadoLimpio == 'pudimos':
            self.repuestaGeneralesPlaca.config(text="Encienda placa primero")

        print("status: ", self.estadoGenerador)



    def obtenerStatusGenerador(self):
            mensaje = f"gen obtener"
            mensaje = mensaje + "\n"
            self.enviar_mensaje(mensaje)
            if self.generador == 's1':
               self.mostrarInformacionPlaca(0)
            elif self.generador == 's2':
                self.mostrarInformacionPlaca(11)


    def mostrarInformacionPlaca(self,generador):
        try:
            responseData = self.respuesta_var.get().split(" ")[6+ generador].split("=")[1]
            responseSignal = self.respuesta_var.get().split(" ")[4 + generador].split("=")[1]
            responseFase = self.respuesta_var.get().split(" ")[7 + generador].split("=")[1]
            responseVmin = self.respuesta_var.get().split(" ")[9 + generador].split("=")[1]
            responseVmax = self.respuesta_var.get().split(" ")[8 + generador].split("=")[1]
            
            self.freResponse.config(text=f"Frecuencia (Hz) en repuesta {responseData} Hz")
            self.signalResponse.config(text=f"Tipo senal {responseSignal}")
            self.faseResponse.config(text=f"Fase (°) {responseFase}°")
            self.vminResponse.config(text=f"Vmin (V) {responseVmin}V")
            self.vmaxResponse.config(text=f"Vmax (V) {responseVmax}V")
        except:
            self.freResponse.config(text=f"Placa desconectada")
            self.signalResponse.config(text=f"")
            self.faseResponse.config(text=f"")
            self.vminResponse.config(text=f"")
            self.vmaxResponse.config(text=f"")


    def enviar_mensaje(self,mensaje):
        print(mensaje)
        ser = self.instancia.estadoConexion()
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
            else:
                self.respuesta_var.set("No se recibió respuesta")
        else:
            self.respuesta_var.set("Puerto no disponible")
