import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

# Crear la ventana de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Gráfica de polinomios")

# Crear un cuadro de texto para ingresar la ecuación del polinomio
lbl_ecuacion = tk.Label(ventana, text="Ecuación: ")
lbl_ecuacion.pack(side=tk.LEFT)

txt_ecuacion = tk.Entry(ventana)
txt_ecuacion.pack(side=tk.LEFT)

# Crear un botón para graficar la ecuación
def graficar():
    # Obtener la ecuación del polinomio ingresada por el usuario
    ecuacion = txt_ecuacion.get()

    # Evaluar la ecuación del polinomio en un rango de valores de x
    x = np.linspace(-10, 10, 100)
    y = eval(ecuacion)

    # Graficar la ecuación del polinomio
    plt.plot(x, y)

    # Encontrar el punto de corte de la gráfica en el eje x
    raices = np.roots([float(coeficiente) for coeficiente in ecuacion.split("x^")])

    # Mostrar el punto de corte de la gráfica en el eje x
    plt.plot(raices, [0]*len(raices), 'ro')

    # Mostrar los ejes x y y
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    # Mostrar la gráfica en una ventana
    plt.show()

btn_graficar = tk.Button(ventana, text="Graficar", command=graficar)
btn_graficar.pack(side=tk.LEFT)

# Ejecutar la ventana de la interfaz gráfica
ventana.mainloop()