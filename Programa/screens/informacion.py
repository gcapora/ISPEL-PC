import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class InformacionGeneral(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#34495E")


        self.logoUndavImg = tk.PhotoImage(file="imgs/undavLogo.png", width=100, height=100)
        self.logoUndavImg = ImageTk.PhotoImage((Image.open("imgs/undavLogo.png")).resize((400,200)))
        icon_label = tk.Label(self, image=self.logoUndavImg, bg="#34495E")
        icon_label.pack(padx=5, pady=10)

        # Título
        titulo_label = tk.Label(self, text="Interfaz ISPEL", font=("Helvetica", 18, "bold"), bg="#34495E", fg='white')
        titulo_label.pack(pady=10)

        # Subtítulo
        subtitulo_label = tk.Label(self, text="Información Detallada del Proyecto", font=("Helvetica", 14), bg="#34495E", fg='#ECF0F1')
        subtitulo_label.pack(pady=5)

        # Resumen detallado
        resumen_text = """
        Este proyecto presenta el desarrollo de la Interfaz de Señales para Prácticas Educativas de Laboratorio (ISPEL),
        un equipo diseñado para ofrecer una solución económica y de código abierto para prácticas de laboratorio
        en los primeros años de carreras de ingeniería y afines. ISPEL busca innovar construyendo un equipo
        accesible y aprovechable en instituciones educativas, especialmente en la Universidad Nacional de Avellaneda (UNDAV).
        El equipo consta de dos generadores de señales analógicas y dos capturadoras de señales, conectándose a una PC
        vía USB para su operación.

        El diseño de ISPEL parte de una sistematización de las prácticas de laboratorio en Ingeniería en Informática,
        y se inscribe en los programas PRIICA de UNDAV y el Programa de Laboratorios de Acceso Remoto de la Secretaría
        de Políticas Universitarias. Actualmente, el equipo está en fase de pruebas de hardware y software del sistema.

        El desarrollo sigue un enfoque STEM/STEAM, priorizando la experiencia práctica, la resolución de problemas,
        y la adaptación a entornos de aprendizaje remotos y presenciales. ISPEL reemplaza funciones de generadores de señal
        y osciloscopios, aunque con menores prestaciones. Las especificaciones incluyen frecuencias de hasta 100 kHz,
        salida de señales configurables, y protecciones para su correcta utilización.

        El desarrollo de hardware y software se realiza bajo licencias libres. En el equipo se ha seleccionado la
        placa NUCLEO-F429ZI de STMicroelectronics y se utiliza FreeRTOS como sistema operativo.

        """
        resumen_label = tk.Label(self, text=resumen_text, justify=tk.LEFT, font=("Helvetica", 12), bg="#34495E", fg="#ECF0F1")
        resumen_label.pack(padx=10, pady=5)
