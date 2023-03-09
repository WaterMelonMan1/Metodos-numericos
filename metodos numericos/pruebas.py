import random as rnd
Xa = rnd.randint(-20,20)
Xb = rnd.randint(-20,20)
Xr = 0
acc =1
cont=0
while True:
  if(2*Xa - 8)*(2*Xb - 8) < 0:
    while True:
      Xr=(Xa+Xb)/2
      if abs((2*Xa - 8)*(2*Xr - 8))<=acc:
        print("El valor Xr: ",Xr, "Se aproxima al resultado")
        print("la cantidad de repeticiones fue: ",cont)
        break
      elif (2*Xa - 8)*(2*Xr - 8) < 0:
        Xb=Xr
        cont=cont+1
      else:
        Xa=Xr
        cont=cont+1
    break
  else:
    Xa = rnd.randint(-20,20)
    Xb = rnd.randint(-20,20)