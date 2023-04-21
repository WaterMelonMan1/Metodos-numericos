from tkinter import *
from PIL import Image,ImageTk, ImageDraw
import tkinter.font as font
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np
import sympy

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
        self.fig, self.ax = plt.subplots()

        #Mensajes
        #label indicacion 1
        self.labelIndicacion = Label(ventana,text="Ingresa el polinomio",font=Fuente,bg="white")
        self.labelIndicacion.place(x=100,y=50)
        #label metodo
        self.labelMetodo = Label(ventana,text="Seleccionar metodo",font=Fuente,bg="white")
        self.labelMetodo.place(x=100,y=160)
        #label reusultadoRaiz
        self.labelRaiz = Label(ventana, text="Raiz", font=Fuente, bg="white")
        self.labelRaiz.place(x=240,y=665)
        #contadorTanteo
        self.labelContadorTanteo = Label(ventana, text="contador tanteo", font=Fuente2, bg="white")
        self.labelContadorTanteo.place(x=100,y=280)
        #ContadorBiseccion
        self.labelContadorBiseccion = Label(ventana,text="contador bis",font=Fuente2, bg="white")
        self.labelContadorBiseccion.place(x=250,y=280)
        #ContadorRegla
        self.labelContadorRegla = Label(ventana,text="contador regla",font=Fuente2,bg="white")
        self.labelContadorRegla.place(x=430,y=280)
        #contadorNewton
        self.labelContadorNewton = Label(ventana, text="contador Newton", font=Fuente2, bg="white")
        self.labelContadorNewton.place(x=100,y=410)
        #ContadorSecante
        self.labelContadorSecante = Label(ventana,text="contador Seca",font=Fuente2, bg="white")
        self.labelContadorSecante.place(x=260,y=410)
        #Contadorsteffensen
        self.labelContadorSteffensen = Label(ventana,text="contador Stef",font=Fuente2, bg="white")
        self.labelContadorSteffensen.place(x=430,y=410)

        #Texto por teclado
        self.polinomio = Entry(ventana,bg='white',font=Fuente)
        self.polinomio.place(x=100,y=100)


        #Botones
        #checkbox
        self.Tanteo = IntVar()
        self.Biseccion = IntVar()
        self.Regla = IntVar()
        self.Newton = IntVar()
        self.Secante = IntVar()
        self.steffensen = IntVar()
        #Tanteo
        self.seleccionTanteo = Checkbutton(ventana,text="Tanteo",font=Fuente,bg="white",variable=self.Tanteo)
        
        #biseccion
        self.seleccionBiseccion = Checkbutton(ventana,text="Biseccion",font=Fuente,bg="white", variable=self.Biseccion)
        
        #regla falsa
        self.seleccionRegla = Checkbutton(ventana,text="Regla Falsa",font=Fuente,bg="white", variable=self.Regla)

        #newton
        self.seleccionNewton = Checkbutton(ventana,text="Newton",font=Fuente,bg="white", variable=self.Newton)
        
        #secante
        self.seleccionSecante = Checkbutton(ventana,text="Secante",font=Fuente,bg="white", variable=self.Secante)
        
        #Steffensen
        self.seleccionSteffensen = Checkbutton(ventana,text="Steffensen",font=Fuente,bg="white", variable=self.steffensen)
        #comprobar solo una casilla
        self.checkboxes = [self.seleccionTanteo, self.seleccionBiseccion, self.seleccionRegla,self.seleccionNewton,self.seleccionSecante,self.seleccionSteffensen]
        for checkbox in self.checkboxes:
            checkbox.pack()
            
            # Configura la función "command" de cada checkbox
            checkbox.config(command=lambda c=checkbox: self.deselect_all(c))
        self.seleccionTanteo.place(x=100,y=220)
        self.seleccionBiseccion.place(x=250,y=220)
        self.seleccionRegla.place(x=430,y=220)
        self.seleccionNewton.place(x=100,y=350)
        self.seleccionSecante.place(x=260,y=350)
        self.seleccionSteffensen.place(x=430,y=350)
        #Boton pulsar
        #resultado
        self.botonResultado = Button(ventana,text="Calcular",width=25,height=3,font=Fuente2,bg="white",command=self.Calcular)
        self.botonResultado.place(x=400, y=550)

        self.botonGraficar = Button(ventana,text="Graficar",width=25,height=3,font=Fuente2,bg="white",command=self.Graficar)
        self.botonGraficar.place(x=100, y=550)

        self.limpio = Button(ventana,text="Limpiar",width=15,height=3,font=Fuente2,bg="white",command=self.limpiar)
        self.limpio.place(x=850, y=600)
        #mostrargrafica
        #grafica
        self.image = Image.open("imagen/foto.jpg")
        self.foto = ImageTk.PhotoImage(self.image)
        self.imagen = Label(ventana, image=self.foto,width=500,height=500)
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
            ecu = self.polinomio.get()
            iterador = 0
            x = random.randint(-10,10)
            while True:
               fx = eval(ecu.format(x))
               if abs(fx) == 0:  # La precisión se puede ajustar a la necesidad
                   iterador = iterador + 1 
                   self.labelRaiz.config(text=x)
                   self.labelContadorTanteo.config(text=iterador)
                   break
               elif fx > 0:
                   x -= 1
                   iterador = iterador + 1
               else:
                   x += 1
                   iterador = iterador + 1
            

        if (self.Biseccion.get()==1):
            ecu = self.polinomio.get()
            a = random.randint(-20, 20)
            b = random.randint(-20, 20)
            iterador_max = 1000000
            iterador = 0
            tolerancia = 0.00001
            c = 0

            while True:
                if eval(ecu.format(a)) * eval(ecu.format(b)) < 0:
                    iterador = 0
                    while True:
                        c = (a + b) / 2
                        if abs(eval(ecu.format(a)) * eval(ecu.format(c))) <= tolerancia:
                            iterador = iterador + 1
                            self.labelContadorBiseccion.config(text=iterador)
                            self.labelRaiz.config(text=c)
                            break
                        elif eval(ecu.format(a)) * eval(ecu.format(c)) < 0:
                            b = c
                            iterador = iterador + 1
                        else:
                            a = c
                            iterador = iterador + 1
                        if iterador >= iterador_max or abs(b - a) <= tolerancia:
                            break
                    break
                else:
                 a = random.randint(-20, 20)
                 b = random.randint(-20, 20)

        if (self.Regla.get()==1):
            ecu = self.polinomio.get()
            ecu = ecu.replace("x", "{}")
            a = random.randint(-20, 20)
            b = random.randint(-20, 20)
            iterador_max = 1000
            iterador = 0
            tolerancia = 0.01
            c = 0

            while True:
               if eval(ecu.format(a)) * eval(ecu.format(b)) < 0:
                    iterador = 0
                    while True:
                         c = a- ((eval(ecu.format(a)))*(b-a))/((eval(ecu.format(b)))-(eval(ecu.format(a))))
                         if abs(eval(ecu.format(a)) * eval(ecu.format(c))) <= tolerancia:
                             iterador = iterador + 1
                             self.labelContadorRegla.config(text=iterador)
                             self.labelRaiz.config(text=c)
                             break
                         elif eval(ecu.format(a)) * eval(ecu.format(c)) < 0:
                             b = c
                             iterador = iterador + 1
                         else:
                             a = c
                             iterador = iterador + 1
                         if iterador >= iterador_max or abs(b - a) <= tolerancia:
                             break
                    break
               else:
                   a = random.randint(-20, 20)
                   b = random.randint(-20, 20)

        if (self.Newton.get()==1):
            ecu = self.polinomio.get()
            x0 = random.uniform(-20, 20) # Elegimos un valor aleatorio para empezar
            iterador_max = 1000000
            iterador = 0
            tolerancia = 0.01
            delta = 0.0001

            while True:
                fx0 = eval(ecu.replace('x', f'({x0})'))
                dfx0 = (eval(ecu.replace('x', f'({x0 + delta})')) - fx0) / delta
                x1 = x0 - fx0/dfx0
                if abs(x1 - x0) < tolerancia:
                    break
                x0 = x1
                iterador += 1
                if iterador >= iterador_max:
                    break

            self.labelContadorNewton.config(text=iterador)
            self.labelRaiz.config(text=x1)
        
        if (self.Secante.get()==1):
            ecu = self.polinomio.get()
            ecu = ecu.replace("x", "{}")
            c = 0
            Soluciones=[]
            Max_Seeds=100
            i=0
            acc =0.001
            cont=0
            while i <= Max_Seeds:
                a = random.randint(-20,20)
                b = random.randint(-20,20)
                if eval(ecu.format(a,a,a)) * eval(ecu.format(b, b, b)) < 0:
                    while True:
                        #Xc= Xa - ((f(Xa)*(Xa-Xb))/(f(Xa)- f(Xb)))
                        c= a -(eval(ecu.format(a,a,a))*(a-b))/(eval(ecu.format(a,a,a))-eval(ecu.format(b,b,b)))
                        if abs(eval(ecu.format(c,c,c))) < acc:
                            cont= cont+1
                            break
                        elif (eval(ecu.format(a,a,a))*eval(ecu.format(c,c,c))) < 0:
                            b=c
                            cont= cont+1
                        else:
                            a=c
                            cont = cont + 1
                    i+=1
                    c= round(c, 2)
                    if c not in Soluciones:
                        Soluciones.append(c)
                
            cadena_lista = ", ".join(str(x) for x in Soluciones)
            self.labelContadorSecante.config(text=cont)
            self.labelRaiz.config(text=cadena_lista)


    def Graficar(self):
        ecuacion = self.polinomio.get()
        raiz = float(self.labelRaiz.cget("text"))
        if (self.Regla.get()==1 or self.Biseccion.get()==1):
            ecuacion = ecuacion.replace("{}", "x")
        
        x = np.linspace(-10, 10, 1000)

        y = eval(ecuacion)

        fig, ax = plt.subplots()
        ax.cla()
        ax.plot(x,y)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Gráfica de la ecuación: ' + ecuacion)

        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        ax.plot(raiz, 0, 'ro')

        canvas = FigureCanvasTkAgg(fig, master=self.imagen)
        canvas.draw()
        canvas.get_tk_widget().pack() 

    def limpiar(self):
        canvas = self.imagen.winfo_children()[0]
        canvas.destroy()

     
                    

#interfaz principal
ventanaPrincipal=App()