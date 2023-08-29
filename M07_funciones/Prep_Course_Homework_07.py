#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:

def es_primo(numero):
    if numero == 2 or numero == 3:
        return True
    if numero % 2 == 0:
        return False
    else:
        for i in range(3, int(numero ** 0.5) + 1, 2):
            if numero % i == 0:
                return False
    return True



# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:




# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:
def numero_mas_repetido(lista):
    reps = 0
    max_reps = 0
    max_rep_n = 0
    start = 1
    n = start
    for i in lista:
        while n < len(lista):
            if i == lista[n]:
                reps += 1
                if reps > max_reps:
                    max_reps = reps
                    max_rep_n = i
            n += 1
        reps = 0
        start += 1
        n = start
    return "El numero " + str(max_rep_n) + " se repitio mas veces: " + str(max_reps)




# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:
def cambiar_medicion_grados(temp, origen, cambio):
    if origen == cambio: 
        return temp
    if origen == "°C":
        if cambio == "°F":
            return temp * (9 / 5) + 32
        else:
            return temp + 273.15

    elif origen == "°F":
        if cambio == "°C":
            return (temp - 32) / (9 / 5)
        else:
            return (temp - 32) / (9 / 5) + 273.15

    else:
        if cambio == "°C":
            return temp - 273.15
        else:
            return (temp - 273.15) * (9 / 5) + 32

# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:




# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:

def factorial(n):
    if n < 1 or n != int(n):
        return "El numero ingresado no es un numero natural"
    contador = 1
    resultado = 1
    while contador < n:
        resultado = resultado * (contador + 1)
        contador+=1
    return resultado


