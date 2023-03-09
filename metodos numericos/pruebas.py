ecuacion = "2*x - 12"   
x = 0
while True:
            fx = eval(ecuacion.replace("x", str(x)))
            if abs(fx) < 0.001:  # La precisión se puede ajustar a la necesidad
                self.resultado_text.insert(tk.END, str(x))
                break
            elif fx > 0:
                x -= 0.001
            else:
                x += 0.001