# taller-numero-1.
Taller hecho por maria jose vallejo rodriguez para la materia de programacion de computadores 
1. Quiz con resultado de 85% de aciertos
   ![Imagen de WhatsApp 2023-09-25 a las 23 19 57](https://github.com/marjovall/taller-numero-1./assets/146041418/dadf08c0-56d3-4b29-931a-e62bee1b78c8)
2. Realice un programa que lea tres números reales y determine cuál es el mayor.
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




