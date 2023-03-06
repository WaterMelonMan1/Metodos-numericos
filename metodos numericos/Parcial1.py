from tkinter import *
from PIL import Image,ImageTk
import tkinter.font as font
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
        #Texto por teclado
        self.polinomio = Entry(ventana,bg='white',font=Fuente)
        self.polinomio.place(x=100,y=100)

        #Botones
        #Tanteo
        self.seleccionTanteo = Checkbutton(ventana,text="Tanteo",font=Fuente,bg="white")
        self.seleccionTanteo.place(x=100,y=320)
        #biseccion
        self.seleccionBiseccion = Checkbutton(ventana,text="Biseccion",font=Fuente,bg="white")
        self.seleccionBiseccion.place(x=250,y=320)
        #regla falsa
        self.seleccionRegla = Checkbutton(ventana,text="Regla Falsa",font=Fuente,bg="white")
        self.seleccionRegla.place(x=430,y=320)
        #resultado
        #resultado
        self.botonResultado = Button(ventana,text="Calcular",width=30,height=3,font=Fuente2,bg="white",command="")
        self.botonResultado.place(x=100, y=500)

        #mostrargrafica
        #grafica
        image = Image.open("imagen/foto.jpg")
        foto = ImageTk.PhotoImage(image)
        self.imagen = Label(ventana, image=foto,width=500,height=500)
        self.imagen.place(x=700,y=50)

    

        ventana.mainloop()


#interfaz principal
ventanaPrincipal=App()