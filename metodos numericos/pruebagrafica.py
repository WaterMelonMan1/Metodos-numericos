import tkinter as tk
import numpy as np

ventana = tk.Tk()
ventana.geometry('400x400')

canvas = tk.Canvas(ventana, width=300, height=300, bg='white')
canvas.pack()

x = np.arange(0, 10, 0.1)
y = np.sqrt(x)

for i in range(len(x) - 1):
    canvas.create_line(x[i]*20, 300-y[i]*20, x[i+1]*20, 300-y[i+1]*20)

ventana.mainloop()