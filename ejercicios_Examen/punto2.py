base = int(input("Ingrese base del triangulo: "))
altura = int(input("Ingrese altura del triangulo: "))

area = (base * altura) / 2

if area < 1000:
    print(f"El area del triangulo es {area}")
else:
    print("DATOS NO VALIDOS")