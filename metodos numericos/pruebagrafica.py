n1=int(input('Ingrese el primer número de la ecucación: '))
sig=int(input('Ingrese el signo de la ecuación si es + ingrese 1, si es - ingrese 0: '))
n2=int(input('Ingrese el segundo número de la ecucación: '))
import random as rnd
x = rnd.randint(-20,20)
print('el valor aleatorio de x es:',x)
if(sig ==0):
  print('la ecuación es: ',n1,'X -',n2)
  if abs((n1 * x) - n2) == 0:
    print("La respuesta es: " , x)
  else:
    cont = 0
    while True:
      if ((n1 * x) - n2) < 0:
        x1 = x + 1
        x = x1
        cont = cont + 1
      else:
        x1 = x - 1
        x = x1
        cont = cont + 1
      if abs((n1 * x) - n2) <= 0:
        print("felicidades la respuesta es: " , x)
        print("Tardó " , cont, " intentos")
        break
else:
 if(sig ==1):
   print('la ecuación es: ',n1,'X +',n2)
   if abs((n1 * x) + n2) == 0:
     print("La respuesta es: " , x)
   else:
     cont = 0
     while True:
       if ((n1 * x) + n2) < 0:
         x1 = x + 1
         x = x1
         cont = cont + 1
       else:
         x1 = x - 1
         x = x1
         cont = cont + 1
       if abs((n1 * x) + n2) <= 0:
         print("felicidades la respuesta es: " , x)
         print("Tardó " , cont, " intentos")
         break