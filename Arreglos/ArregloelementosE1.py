import random 
import statistics

cantidadnumero=int(input("ingresa la cantidad de numeros que tiene el arreglo  "))
lista = [random.randint(1, 11) for i in range(0, cantidadnumero)]
print (lista)

def sumar (suma):
    suma=sum(lista)
    return suma 

def promedio (sumar):
    count=0
    for i in range(len(lista)):
        count+=1
        promedio=sumar(sumar)/count
        print(f"el promedio es {promedio}")
    return promedio 

def numeromaximo (maximo):
    maximo = max(lista)
    return maximo

def numerominimo (minimo):
    minimo = min(lista)
    return minimo 

def ordenarace (lista):
    lista.sort()
    return lista 

def ordenardece (lista):
    lista.reverse()
    return lista 

def moda (moda):
    moda = statistics.mode(lista)
    return moda

def mediana (mediana):
    mediana = statistics.median(lista)
    return mediana

def buscar ():
    
    insertar = int(input("ingrese un numero a buscar en la lista: "))
    for i in range(len(lista)):
        if lista[i]==insertar:
            print(f"el numero {insertar} se encuentra en la posicion {i}")
        else:
            print(f"el numero {insertar} no se encuentra en la lista")
    return insertar

match int(input("""ingrese la operacion que desea realizar:
1. Sumar los elementos del arreglo
2. Promedio de los elementos del arreglo
3. Numero mayor del arreglo
4. Numero menor del arreglo
5. Ordenar el arreglo de forma ascendente
6. Ordenar el arreglo de forma descendente
7. Moda del arreglo
8. Mediana del arreglo
9. Buscar un numero en el arreglo
""")):
    
    case 1:
        print(f"la suma de los elementos es {sumar(sumar)}")
    case 2:
        print(f"el promedio es {promedio(sumar)}")
    case 3:
        print(f"el numero mayor es {numeromaximo(maximo=True)}")
    case 4:
        print(f"el numero menor es {numerominimo(minimo=True)}")
    case 5:
        print(f"la lista ordenada es {ordenarace(lista)}")
    case 6:
        print(f"la lista en orden inverso es {ordenardece(lista)}")
    case 7:
        print(f"la moda es {moda(moda)}")
    case 8:
        print(f"la mediana es {mediana(mediana)}")
    case 9:
        buscar()
    case _:
        print("opcion no valida")