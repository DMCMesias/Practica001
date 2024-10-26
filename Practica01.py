#REALIZADO POR DAVID MARAVER CEBALLOS
#PARTE 1
s=input("Dime tu nombre: ")
print(f"Hola  {s}")


#PARTE 2
print(f"Hola {s.upper()}")
print(f"{len(s)}")


#PARTE 3
numeropar=int(input("Dime un numero: "))
for numero in range(2,numeropar):
    if int(numero)%2==0:
        print(f"El numero encontrado es el {numero}")
        

#PARTE 4
import math
peso = float(input("Escriba su peso: "))
altura = float(input("Escriba su altura: "))

imc = round(peso/math.pow(altura,2),1)

print("Su IMC es de "+str(imc))


#PARTE 5
import random
num1  = random.randrange(2,11)
num2  = random.randrange(2,11)

resultado=int(num1*num2)
pregunta =int(input("Escribe un numero: "))
if resultado==pregunta:
    print("Enorabuena acertaste")
else:
    print(f"NO, lo siento era {resultado}")