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
    print("La frecuencia no está en ninguna región conocida del espectro electromagnético.")
