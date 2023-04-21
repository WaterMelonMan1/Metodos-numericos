from random import randint

def pol(x):
  return 2*x**2 + 4*x -6

resultados = set()  # conjunto para almacenar los resultados únicos

for i in range(100):  # ejecutar el código 5 veces
  Xa = randint(-20, 20)
  #print('Xa = ', Xa)
  cont = 0
  Xc = Xa
  while True:
    cont += 1
    if cont > 100000:  # si se han hecho más de 1000 iteraciones, salir del ciclo
      #print("Se han hecho más de 1000 iteraciones. Generando nueva Xa...")
      break
    if abs(pol(Xc)) <= 0.0001:
      break
    else:
      Xc = Xa - ((pol(Xa)**2) / (pol(Xa+pol(Xa)) - pol(Xa)))
    Xa = Xc
  if cont > 1000:  # si se han hecho más de 1000 iteraciones, saltar a la siguiente iteración
    continue
  if all(abs(Xc - r) > 0.001 for r in resultados):  # agregar el resultado solo si es lo suficientemente diferente
    resultados.add(Xc)

print('Las raices del polinomio son:', resultados)