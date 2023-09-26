letra = input("Ingresa una letra del abecedario : ")
letra = letra.lower()
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"{letra} es una vocal.")
else:
    print(f"{letra} es una consonante.")
