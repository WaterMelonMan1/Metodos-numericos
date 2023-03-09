from tkinter import *
from PIL import Image,ImageTk
import tkinter.font as font
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class App():
    def __init__(self):
        ventana = Tk()
        ventana.title("Metodos numericos Parcial 1")
        ventana.geometry("1280x720")
        imagen = Image.open("imagen/fondo.jpg")
        fondo = ImageTk.PhotoImage(imagen)
        label_fondo = Label(ventana, image=fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        #widgets
        Fuente = font.Font(size=20)
        Fuente2 = font.Font(size=14)

        #Mensajes
        #label indicacion 1
        self.labelIndicacion = Label(ventana,text="Ingresa el polinomio",font=Fuente,bg="white")
        self.labelIndicacion.place(x=100,y=50)
        #label metodo
        self.labelMetodo = Label(ventana,text="Seleccionar metodo",font=Fuente,bg="white")
        self.labelMetodo.place(x=100,y=260)
        #label reusultadoRaiz
        self.labelRaiz = Label(ventana, text="Raiz", font=Fuente, bg="white")
        self.labelRaiz.place(x=240,y=590)
        #contadorTanteo
        self.labelContadorTanteo = Label(ventana, text="contador tanteo", font=Fuente2, bg="white")
        self.labelContadorTanteo.place(x=100,y=380)
        #ContadorBiseccion
        self.labelContadorBiseccion = Label(ventana,text="contador bis",font=Fuente2, bg="white")
        self.labelContadorBiseccion.place(x=250,y=380)
        #ContadorRegla
        self.labelContadorRegla = Label(ventana,text="contador regla",font=Fuente2,bg="white")
        self.labelContadorRegla.place(x=430,y=380)

        #ENtrada de polinomio
        self.Ecuacion = None
        #Numero random
        self.numero = None
        self.numero2 = None
        #Texto por teclado
        self.polinomio = Entry(ventana,bg='white',font=Fuente)
        self.polinomio.place(x=100,y=100)

        #Botones
        #checkbox
        self.Tanteo = IntVar()
        self.Biseccion = IntVar()
        self.Regla = IntVar()
        #Tanteo
        self.seleccionTanteo = Checkbutton(ventana,text="Tanteo",font=Fuente,bg="white",variable=self.Tanteo)
        
        #checkBox
        #biseccion
        self.seleccionBiseccion = Checkbutton(ventana,text="Biseccion",font=Fuente,bg="white", variable=self.Biseccion)
        
        #regla falsa
        self.seleccionRegla = Checkbutton(ventana,text="Regla Falsa",font=Fuente,bg="white", variable=self.Regla)
        

        self.checkboxes = [self.seleccionTanteo, self.seleccionBiseccion, self.seleccionRegla]
        for checkbox in self.checkboxes:
            checkbox.pack()
            
            # Configura la función "command" de cada checkbox
            checkbox.config(command=lambda c=checkbox: self.deselect_all(c))
        self.seleccionTanteo.place(x=100,y=320)
        self.seleccionBiseccion.place(x=250,y=320)
        self.seleccionRegla.place(x=430,y=320)

        #Boton pulsar
        #resultado
        self.botonResultado = Button(ventana,text="Calcular",width=30,height=3,font=Fuente2,bg="white",command=self.Calcular)
        self.botonResultado.place(x=100, y=450)

        #mostrargrafica
        #grafica
        image = Image.open("imagen/foto.jpg")
        foto = ImageTk.PhotoImage(image)
        self.imagen = Label(ventana, image=foto,width=500,height=500)
        self.imagen.place(x=700,y=50)

    

        ventana.mainloop()

    #Funciones
    #Unica opcion de checkbox
    def deselect_all(self, current_checkbox):
        # Desmarca todos los checkboxes, excepto el que se acaba de marcar
        for checkbox in self.checkboxes:
            if checkbox is not current_checkbox:
                checkbox.deselect()

    def Calcular(self):
        if (self.Tanteo.get()==1):
            x = random.randint(-5,5)
            self.labelContadorTanteo.config(text=x)
            ecu = self.polinomio.get()
            f = eval(ecu.format(x))
            self.labelRaiz.config(text=f)



            
            

#interfaz principal
ventanaPrincipal=App()