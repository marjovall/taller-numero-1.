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
