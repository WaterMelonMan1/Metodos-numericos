from tkinter import *
from PIL import Image, ImageTk

# Crear la ventana principal de Tkinter
ventana = Tk()
ventana.geometry("1500x720")

# Cargar la imagen que deseas utilizar como fondo
imagen = Image.open("imagen/foto.jpg")

# Convertir la imagen en un objeto PhotoImage de Tkinter
fondo = ImageTk.PhotoImage(imagen)

# Crear un widget Label que contenga la imagen de fondo y establecer sus dimensiones
label_fondo = Label(ventana, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Continuar con el diseño de la interfaz gráfica
# ...

# Iniciar el bucle principal de la aplicación
ventana.mainloop()