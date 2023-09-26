
numero1 = float(input("Ingresa el primer número real: "))
numero2 = float(input("Ingresa el segundo número real: "))
if numero2 != 0 and numero2 % numero1 == 0:
    print(f"{numero1} es múltiplo de {numero2}.")
else:
    print(f"{numero1} no es múltiplo de {numero2}.")
