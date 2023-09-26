# taller-numero-1.
![Imagen de WhatsApp 2023-09-26 a las 00 02 46](https://github.com/marjovall/taller-numero-1./assets/146041418/685a45b7-eedd-4275-8593-4f78f40df467)

GRUPO  I LOVE MORAT 

Taller hecho por maria jose vallejo rodriguez para la materia de programacion de computadores 
1. Quiz con resultado de 85% de aciertos
   ![Imagen de WhatsApp 2023-09-25 a las 23 19 57](https://github.com/marjovall/taller-numero-1./assets/146041418/dadf08c0-56d3-4b29-931a-e62bee1b78c8)
2. Realice un programa que lea tres números reales y determine cuál es el mayor.
```python
# Pedir tres numeros al usuario
n1 = float(input("Introduce el primer numero: "))
n2 = float(input("Introduce el segundo numero: "))
n3 = float(input("Introduce el tercer numero: "))

# Comparar los tres numeros para determinar el mayor
if n1 >= n2 and n1 >= n3:
    print("El numero " + str(n1) + " es el mayor")
elif n2 >= n1 and n2 >= n3:
    print("El numero " + str(n2) + " es el mayor")
else:
    print("El numero " + str(n3) + " es el mayor")
print
```
En este ejercicio lo que se busca es que el usuario pueda introducir los numero que el quiera y mediante este codigo determine cual es el mayor,
para ello, se insertan tres variales en las cuales el usuario pueda introducir esos tres numeros, seguido a ello entra a comparar los numeros mediante la palabra reservada "if" si se cumple en un primer caso, si no se recurre a la palabra "elif", la cual se puede repetir las veces necesarias, pero si no se cumple en esas veces necesarias el programa se vera forzadoa utilizar el ultimo que "else", el cual se le asigna un mensaje en el caso en el que no se cumpla ningun caso.
3.Realice un programa que lea un número enteros y determine si es par o impar.
```python
numero = int(input("Ingresa un número entero: "))
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")
```
En el siguiente caso lo que se hace es pedirle al usuario tres numeros enteros los cuales se forzaran a ser asi con la palabra reservada int, seguido a ello, se entra a comparar a cada uno con la palabra reservada "if", seguido a ello se pone el nombre de la variable donde esta contenida el numero y se somete a una de las funciones la cual es el modulo % en el cual se condiciona con un comparador "==" para dar la condicional, que en este caso es si es 0, entonces es par, pero en el caso de que no lo sea, se da directamente con la palabra reservada "else" seguido a un mensaje declarando es es impar.
4.Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
 ```python
numero1 = float(input("Ingresa el primer número real: "))
numero2 = float(input("Ingresa el segundo número real: "))
if numero2 != 0 and numero2 % numero1 == 0:
    print(f"{numero1} es múltiplo de {numero2}.")
else:
    print(f"{numero1} no es múltiplo de {numero2}.")
```
En el siguiente punto se le pide al usuario dos numeros reales y para forzar esa condicion se impone la palabra "float" para declarar que esa variable será una variable con número real, despues se comprar si el número el cual se llama "alpha" es multiplo de "beta" y para ello se multiplica por 2 y seguido a ello se compara con "beta" para saber si el primer caso se cumple, en el caso de que si se deja un mensaje confirmando que es multiplo, en el caso contrario se deja otro mensaje declarando que no es multiplo

5.Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.
 ```python
numero1 = float(input("Ingresa el primer número real: "))
numero2 = float(input("Ingresa el segundo número real: "))
numero3 = float(input("Ingresa el tercer número real: "))
suma = numero1 + numero2

if suma > numero3:
    print(f"La suma  de  {numero1} y {numero2} es  igual a {suma}  y es mayor que  el tercer numero {numero3}.")
elif suma < numero3:
    print(f"La suma de  {numero1} y {numero2} es  igual a {suma} y  es menor que el tercer numero {numero3}.")
else:
    print(f"La suma de  {numero1} y {numero2} es  igual a {suma}  y es igual al tercer numero {numero3}.")
```
En este punto se le pide al usuario tres numeros, los cuales seran sumados "numero1" y "numero2", y dependiendo de su resultado cumpliran las condicionales dadas y dependiendo de cual cumpla o si no cumple ninguna, mostrará alguno de los tres mensajes confirmando si la suma de los numeros ingresados en las variables "numero1" y "numero2" son mayor, menor o igual al numero ingresado en la variable "numero3"
6. Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.
 ```python
letra = input("Ingresa una letra del abecedario : ")
letra = letra.lower()
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"{letra} es una vocal.")
else:
    print(f"{letra} es una consonante.")
```
diagrama de flujo 
![diagramadeflujo](https://github.com/marjovall/taller-numero-1./assets/146041418/ec71660d-8e6b-49a9-99e0-262a0ce0a848)
En este ejercicio, simplemete se busca una comparacion, donde se deja las vocales en un primer caso donde si se cumple, será una vocal y si no, entonces seria una consonante.
7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:

 7.1El promedio
 
 7.2La mediana
 
 7.3El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)

 7.4 Ordenar los números de forma ascendente
 
 7.5Ordenar los números de forma descendente
 
 7.6 La potencia del mayor número elevado al menor número
 
  7.7 La raíz cúbica del menor número
 ```python
  n1 = float(input(f"Ingresa el número : "))
 n2 = float(input(f"Ingresa el número : "))
 n3 = float(input(f"Ingresa el número : "))
 n4 = float(input(f"Ingresa el número : "))
 n5 = float(input(f"Ingresa el número : "))

# Calcula el promedio
promedio = (n1 + n2 + n3 + n4 + n5) / 5

# encuentra el numero minimo
minimo = n1
if n2 < minimo:
    minimo = n2
if n3 < minimo:
    minimo = n3
if n4 < minimo:
    minimo = n4
if n5 < minimo:
    minimo = n5
# Encuentra el número máximo
maximo = n1
if n2 > maximo:
    maximo = n2
if n3 > maximo:
    maximo = n3
if n4 > maximo:
    maximo = n4
if n5 > maximo:
    maximo = n5
# Calcula la mediana
mediana = n3
# Calcula el promedio multiplicativo
producto_multiplicativo= (n1 * n2 * n3 * n4 * n5)**(1/5)
# Ordena los números de forma descendente y ascendente 
if n1 > n2:
    n1, n2 = n2, n1
if n2 > n3:
    n2, n3 = n3, n2
if n3 > n4:
    n3, n4 = n4, n3
if n4 > n5:
    n4, n5 = n5, n4
if n1 > n2:
    n1, n2 = n2, n1
if n2 > n3:
    n2, n3 = n3, n2
if n3 > n4:
    n3, n4 = n4, n3
if n1 > n2:
    n1, nu2 = n2, n1
if n2 > n3:
    n2, n3 = n3, n2
if n1 > n2:
    n1, n2 = n2, n1

# Calcula la potencia del mayor número elevado al menor número
potencia = maximo** minimo
# Calcula la raíz cúbica del menor número
raiz_cubica_menor = minimo ** (1 / 3)

# Muestra los resultados
print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")
print(f"Promedio multiplicativo: {producto_multiplicativo}")
print(f"Números en orden ascendente: {n1},{n2},{n3},{n4},{n5}")
print(f"Números en orden descendente:  {n5},{n4},{n3},{n2},{n1}")
print(f"Potencia del mayor al menor: {potencia}")
print(f"Raíz cúbica del menor número: {raiz_cubica_menor}")
```
8.Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.
 ```python
frecuencia = float(input("Ingresa la frecuencia en Hz: "))
# Compara la frecuencia con los rangos típicos del espectro electromagnético
if 3 * 10**9 <= frecuencia <= 3 * 10**12:
    print("La frecuencia se encuentra en la región de las microondas.")
elif 3 * 10**12 < frecuencia <= 3 * 10**14:
    print("La frecuencia se encuentra en la región de las terahertz.")
elif 3 * 10**14 < frecuencia <= 3 * 10**17:
    print("La frecuencia se encuentra en la región de los infrarrojos.")
elif 3 * 10**17 < frecuencia <= 4.3 * 10**14:
    print("La frecuencia se encuentra en la región de la luz visible.")
elif 4.3 * 10**14 < frecuencia <= 7.5 * 10**14:
    print("La frecuencia se encuentra en la región de los ultravioleta.")
elif 7.5 * 10**14 < frecuencia <= 3 * 10**17:
    print("La frecuencia se encuentra en la región de los rayos X.")
elif frecuencia > 3 * 10**17:
    print("La frecuencia se encuentra en la región de los rayos gamma.")
else:
    print("La frecuencia no está en ninguna región conocida del espectro electro
 ```
En este punto se le pide al usuario una frecuencia en hertz (Hz) la cual esta alojada en una variable llamada "frecuencia" y esta será comparada con los valores de frecuencia que son visibles al ojo humano, donde si la frecuencia ingresada esta dentro del intervalo de frecuencias del espectro visible, se delara que el valor esta en el rango visible, si esta es menor al intervalo se declara que esta en un rango de infrarojos y si esta es muy alta (superando el intervalo) entonces esta esta en el rango de los ultravioleta.

9)Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.
 ```python
pais = input("escriba el nombre de un pais en minusculas: ")
if pais == "canada":
    print("La capital es toronto")
elif pais == "estados unidos":
    print("la capital es washington")
elif pais == "mexico":
    print("la capital es mexico d.f.")
elif pais == "belice":
    print("La capital es belmopan")
elif pais == "costa rica":
    print("La capital es san jose")
elif pais == "el salvador":
    print("La capital es san salvador")
elif pais == "guatemala":
    print("La capital es ciudad de guatemala")
elif pais == "honduras":
    print("Las capitales son tegucigalpa y comayagüela")
elif pais == "nicaragua":
    print("La capital es managua")
elif pais == "panama":
    print("La capital es ciudad de panama")
elif pais == "colombia":
    print("La capital es bogota")
elif pais == "venezuela":
    print("La capital es caracas")
elif pais == "peru":
    print("La capital es lima")
elif pais == "bolivia":
    print("La capital es la paz")
elif pais == "argentina":
    print("La capital es buenos aires")
elif pais == "chile":
    print("La capital es santiago de chile")
elif pais == "ecuador":
    print("La capital es quito")
elif pais == "guyana":
    print("La capital es georgetown")
elif pais == "paraguay":
    print("La capital es asuncion")
elif pais == "surinam":
    print("La capital es paramaribo")
elif pais == "trinidad y tobago":
    print("La capital es puerto españa")
elif pais == "uruguay":
    print("La capital es montevideo")
elif pais == "brasil":
    print("La capital es brasilia")
elif pais == "guyana francesa":
    print("La capital es cayena")
elif pais == "antigua y barbuda":
    print("La capital es saint john")
elif pais == "bahamas":
    print("La capital es nasau")
elif pais == "barbados":
    print("La capital es bridgetown")
elif pais == "cuba":
    print("La capital es la habana")
elif pais == "dominica":
    print("La capital es roseau")
elif pais == "granada":
    print("La capital es saint george")
elif pais == "haiti":
    print("La capital es puerto principe")
elif pais == "jamaica":
    print("La capital es kingston")
elif pais == "republica dominicana":
    print("La capital es santo domingo")
elif pais == "san cristobal y nieves":
    print("La capital es basseterre")
elif pais == "san vicente y las granbadinas":
    print("La capital es kingstown")
elif pais == "santa lucia":
    print("La capital es castries")
elif pais == "puerto rico":
    print("La capital es san juan")
else:
    print("pais no identificado")
 ```
En este punto se da con condicionales, en la cual se le pide al usuario el nombre de un pais de america en minusculas, ya que se tiene que tener en cuenta que si una letra es mayuscula, Python la interpreta como otro valor u otra variable, por ende, se le especifica al usuario escribirlo en minusculas, y si cumple con alguna condicional, se imprimira la capital o las capitales de ese pais, si no, simplemente mostrará el mensaje "pais no identificado"

10.Escriba un programa que dada una distancia calcule: 

10.1El tiempo que le tomaría a la luz recorrer la distancia.

10.2El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.

10.3El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.

10.4El tiempo que le tomaría a Bolt recorrer la distancia.
  ```python
 velocidad_luz = 299792458  # Velocidad de la luz en el vacío
velocidad_sonido = 343  # Velocidad del sonido en el aire a 20°C
velocidad_vehiculo_comercial = 90  # Velocidad en km/h convertida a m/s
velocidad_bolt = 12.42  # Velocidad promedio de Usain Bolt en m/s

# Solicita al usuario ingresar la distancia en metros
distancia = float(input("Ingresa la distancia en metros: "))

# Calcula el tiempo que tomaría a la luz recorrer la distancia
tiempo_luz = distancia / velocidad_luz

# Calcula el tiempo que tomaría al sonido (en el aire) recorrer la distancia
tiempo_sonido = distancia / velocidad_sonido

# Calcula el tiempo que tomaría al vehículo comercial más veloz recorrer la distancia
tiempo_vehiculo_comercial = distancia / velocidad_vehiculo_comercial

# Calcula el tiempo que tomaría a Bolt recorrer la distancia
tiempo_bolt = distancia / velocidad_bolt

# Muestra los resultados
print(f"Tiempo que tomaría a la luz recorrer la distancia: {tiempo_luz} segundos")
print(f"Tiempo que tomaría al sonido recorrer la distancia: {tiempo_sonido} segundos")
print(f"Tiempo que tomaría al vehículo comercial más veloz recorrer la distancia: {tiempo_vehiculo_comercial} segundos")
print(f"Tiempo que tomaría a Bolt recorrer la distancia: {tiempo_bolt} segundos")
 ```
En este ultimo programa se le pide una distancia en metros al usuario, ya que las velocidades que se trabajan son en metros/segundo, despues de eso, el valor que ingreso el usuario será sometido a las formulas de velocidad, distancia y tiempo, donde su resultado se da para el tiempo en segundos y por ultimo se imprime el mensaje despues de cada formula mostrando el resultado.

