#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

num = 2
if (num<0): print("El numero es menor a 0") 
elif(0<num): print("El numero es mayor a 0") 
else: print("El numero es igual a 0")



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

a = 2
b=2
if (type(a) == type(b)): print("Lo son")



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

i = 0
while i != 20:
    i += 1
    if i % 2 == 0:
        print(str(i) + " es par")
    else:
        print(str(i) + " es impar")




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for n in range(0, 5):
    print(n ** 3)



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

ciclo = 2
for n in range(0, ciclo):
    print (n)



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

n = 23

div = 2
if n <= 0 or str(type(n)) != "<class 'int'>":
    print("numero invalido")
else:
    while n != 1:
        if n % div == 0:
            n /= div
            print(div)
            div = 2
        else:
            div += 1




# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

while True:
    for n in range(10,0,-1):
        print(n)
    break



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

for n in range(10, 0, -1):
    while True:
        print(n)
        n += 1
        if n == 10:
            break



# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

primo = 1
while (primo <30):
    primo += 1
    if primo == 2 or primo == 3: print(primo)
    if primo%2==0 or primo%3==0 or primo%5==0: {}
    else:
        print(primo)


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

primo = 1
while (primo <30):
    primo += 1
    if primo == 2 or primo == 3:
        print(primo)
        continue
    if primo%2==0 or primo%3==0 or primo%5==0: continue
    else:
        print(primo)



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

#se saltea las comparaciones innecesarias, haciendo al codigo mas ligero


# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

div12 = 99
while (div12 <300):
    div12 += 1
    if div12 % 12 == 0:
        print(div12)
        continue



# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:


n_input = int(input("ingresa un numero y se dara el primo mayor mas cercano: "))
if n_input < 2:
    print(2)
elif n_input < 3:
    print(3)

while n_input > 3:
    saltar = False
    n_input += 1
    if n_input % 2 == 0: continue
    for i in range(3, int(n_input ** 0.5) + 1, 2):
        if n_input % i == 0:
            saltar = True
            continue

    if saltar: continue
    print(n_input)
    if input("encontrar el siguiente? (y/n): ") == "y": continue
    break

# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

mult_div = 99
while (mult_div <300):
    mult_div+=1
    if mult_div % 6 == 0:
        print(mult_div)
        break

