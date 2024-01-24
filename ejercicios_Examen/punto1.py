Voltaje1 = int(input("ingrese Voltaje 1: "))
Voltaje2 = int(input("ingrese Voltaje 2: "))
Voltaje3 = int(input("ingrese Voltaje 3: "))
Voltaje4 = int(input("ingrese Voltaje 4: "))
Voltaje5 = int(input("ingrese Voltaje 5: "))

promedio = (Voltaje1 + Voltaje2 + Voltaje3 + Voltaje4 + Voltaje5 / 5)

if promedio >= 220:
    print(promedio)
    print("ALTO VOLTAJE")
else:
    print(promedio)
    print("VOLTAJE CORRECTO")