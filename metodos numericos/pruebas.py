import tkinter as tk
import random
import sympy

class RootFinder:
    def __init__(self, master):
        self.master = master
        self.master.title("Encontrar la raíz de una ecuación")
        self.master.geometry("400x200")
        
        # Crear el label para la ecuación
        self.label_equation = tk.Label(self.master, text="Ecuación: ")
        self.label_equation.pack()
        
        # Crear la entrada de texto para la ecuación
        self.entry_equation = tk.Entry(self.master)
        self.entry_equation.pack()
        
        # Crear el botón para generar el número aleatorio
        self.button_generate = tk.Button(self.master, text="Generar número aleatorio", command=self.generate_number)
        self.button_generate.pack()
        
        # Crear el botón para encontrar la raíz
        self.button_find_root = tk.Button(self.master, text="Encontrar raíz", command=self.find_root)
        self.button_find_root.pack()
        
        # Crear el label para mostrar el número aleatorio
        self.label_number = tk.Label(self.master, text="")
        self.label_number.pack()
        
        # Crear el label para mostrar el resultado
        self.label_result = tk.Label(self.master, text="")
        self.label_result.pack()
        
        # Variables de clase
        self.equation = None
        self.number = None
        
    def generate_number(self):
        self.number = random.randint(0, 10)
        self.label_number.config(text="Número generado: " + str(self.number))
        
    def find_root(self):
        if self.number is None:
            self.label_result.config(text="Primero debe generar un número aleatorio.")
            return
        
        # Obtener la ecuación y evaluarla en el número aleatorio
        self.equation = sympy.sympify(self.entry_equation.get())
        guess = self.number
        iterations = 0
        while True:
            iterations += 1
            f = self.equation.subs('x', guess)
            if abs(f) < 0.01:
                break
            guess = guess - f
        self.label_result.config(text="La raíz es: " + str(guess) + " (en " + str(iterations) + " iteraciones)")

# Crear la ventana principal
root = tk.Tk()

# Crear la instancia de RootFinder
app = RootFinder(root)

# Iniciar el bucle de la aplicación
root.mainloop()