Voltaje1 = int(input("ingrese Voltaje 1: "))
Voltaje2 = int(input("ingrese Voltaje 2: "))
Voltaje3 = int(input("ingrese Voltaje 3: "))

promedio = int(Voltaje1 + Voltaje2 + Voltaje3 / 3)

if promedio <= 115:
    print(promedio)
    print("Voltaje correcto")
elif promedio > 115 and promedio < 220:
    print(promedio)
    print("ALTO VOLTAJE")
elif promedio >= 220:
    print(promedio)
    print("PELIGRO")
