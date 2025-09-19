

import random

lista=[random.randint(1,100) for i in range(10)]
lista1 = [random.randint(1,100) for i in range(10)]

print("Lista 1: ", lista)
print("Lista 2: ", lista1)

def suma_mas_alta(lista, lista1):
    suma1 = sum(lista)
    suma2 = sum(lista1)
    if suma1 > suma2:
        return "La lista 1 tiene la suma más alta: " + str(suma1)
    elif suma2 > suma1:
        return "La lista 2 tiene la suma más alta: " + str(suma2)
    else:
        return "Ambas listas tienen la misma suma: " + str(suma1)
def numero_mayor(lista, lista1):
    mayor1 = max(lista)
    mayor2 = max(lista1)
    if mayor1 > mayor2:
        return "La lista 1 tiene el número mayor: " + str(mayor1)
    elif mayor2 > mayor1:
        return "La lista 2 tiene el número mayor: " + str(mayor2)
    else:
        return "Ambas listas tienen el mismo número mayor: " + str(mayor1)
def numero_menor(lista, lista1):
    menor1 = min(lista)
    menor2 = min(lista1)
    if menor1 < menor2:
        return "La lista 1 tiene el número menor: " + str(menor1)
    elif menor2 < menor1:
        return "La lista 2 tiene el número menor: " + str(menor2)
    else:
        return "Ambas listas tienen el mismo número menor: " + str(menor1)
def promedio_conjunto(lista, lista1):
    conjunto = lista + lista1
    promedio = sum(conjunto) / len(conjunto)
    return "El promedio conjunto es: " + str(promedio)
def promedio_individual(lista, lista1):
    promedio1 = sum(lista) / len(lista)
    promedio2 = sum(lista1) / len(lista1)
    conjunto = lista + lista1
    promedio_conjunto = sum(conjunto) / len(conjunto)
    resultado = ""
    if promedio1 > promedio_conjunto:
        resultado += "El promedio de la lista 1 está por encima del promedio conjunto: " + str(promedio1) + "\n"
    else:
        resultado += "El promedio de la lista 1 está por debajo del promedio conjunto: " + str(promedio1) + "\n"
    if promedio2 > promedio_conjunto:
        resultado += "El promedio de la lista 2 está por encima del promedio conjunto: " + str(promedio2) + "\n"
    else:
        resultado += "El promedio de la lista 2 está por debajo del promedio conjunto: " + str(promedio2) + "\n"
    return resultado
def cantidad_pares(lista, lista1):
    pares1 = len([x for x in lista if x % 2 == 0])
    pares2 = len([x for x in lista1 if x % 2 == 0])
    if pares1 > pares2:
        return "La lista 1 tiene mayor cantidad de pares: " + str(pares1)
    elif pares2 > pares1:
        return "La lista 2 tiene mayor cantidad de pares: " + str(pares2)
    else:
        return "Ambas listas tienen la misma cantidad de pares: " + str(pares1)
def cantidad_impares(lista, lista1):
    impares1 = len([x for x in lista if x % 2 != 0])
    impares2 = len([x for x in lista1 if x % 2 != 0])
    if impares1 > impares2:
        return "La lista 1 tiene mayor cantidad de impares: " + str(impares1)
    elif impares2 > impares1:
        return "La lista 2 tiene mayor cantidad de impares: " + str(impares2)
    else:
        return "Ambas listas tienen la misma cantidad de impares: " + str(impares1)
oppcion=int(input("Ingrese el numero de la opcion que desea ejecutar:\n1. Suma mas alta\n2. Numero mayor\n3. Numero menor\n4. Promedio conjunto\n5. Promedio individual\n6. Cantidad de pares\n7. Cantidad de impares\n"))

match oppcion:
    case 1: print(f"suma_mas_alta: {suma_mas_alta(lista, lista1)}")
    case 2: print(f"numero_mayor: {numero_mayor(lista, lista1)}")
    case 3: print(f"numero_menor: {numero_menor(lista, lista1)}")
    case 4: print(f"promedio_conjunto: {promedio_conjunto(lista, lista1)}")
    case 5: print(f"promedio_individual: {promedio_individual(lista, lista1)}")
    case 6: print(f"cantidad_pares: {cantidad_pares(lista, lista1)}")
    case 7: print(f"cantidad_impares: {cantidad_impares(lista, lista1)}")
    case _: print("Opcion no valida")
       

