import random
#diccionario
var={'letra':'a',
     'numero':100}
#set o conjunto
var1={1,2,3}
print(type(var1))
#tupla
var2=('a',567,"asa")
#listas - similares a los arreglos de java
#O a los arraylist o linkedlist de java
lista=[1,"udec",3.8]
lista.append("estructuras")
print(lista)
for i in range(len(lista)):
    print(lista[i])

for elemento in lista:
    print(elemento)
    
cantidad=random.randint(5, 15)
print(f'cantidad={cantidad}')
vector=[]
for i in range(cantidad):
    vector.append(random.randint(1, 100))    
print(vector)
