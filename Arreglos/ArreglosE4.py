import random

n = int(input("Ingrese la cantidad de elementos del arreglo: "))
arreglo = []
while len(arreglo) < n:
    num = random.randint(1, 100)
    if num not in arreglo:
        arreglo.append(num)
    else:
        print(f"El número {num} ya está en el arreglo.")
print("El arreglo final es:", arreglo)
