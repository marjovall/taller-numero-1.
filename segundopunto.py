numero1 = float(input("Ingresa el primer número real: "))
numero2 = float(input("Ingresa el segundo número real: "))
numero3 = float(input("Ingresa el tercer número real: "))

if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3

print("El número mayor es:"+ str(mayor))




