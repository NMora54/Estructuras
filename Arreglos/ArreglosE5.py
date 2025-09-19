import random

n = int(input("Ingrese la cantidad de elementos del arreglo: "))
arreglo = []
while len(arreglo) < n:
    if len(arreglo) == 0:
        num = random.randint(1, 10)
        arreglo.append(num)
    else:
        next_decade = ((arreglo[-1] // 10) + 1) * 10
        if next_decade > 100:
            break
        num = random.randint(arreglo[-1] + 1, next_decade)
        arreglo.append(num)
print("El arreglo final es:", arreglo)
