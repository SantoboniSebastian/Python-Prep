#!/usr/bin/env python
# coding: utf-8

# ## Manejo de errores

# 1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

# In[1]:

import sys
print(sys.path)
sys.path.append(r'C:\Users\Merth\Python-Prep\M08_clasesyOOP')
from funciones import Funciones_Matematicas as F
#sys.path.pop(-1)
#


####F("string")


# 2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

# In[5]:

####from funciones import Funciones_Matematicas as F
####F([1,2,3]).conversion_grados(21,"te", "st")



# 3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
# Creacion del objeto incorrecta<br>
# Creacion correcta del objeto<br>
# Metodo valor_modal()<br>
# 
# Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.

# In[9]:



import unittest



class Funciones_Matematicas_test(unittest.TestCase):
    
    def test_creacion_correcta(self):
        arg_1 = [1,2,3,4]
        f1 = F(arg_1)
        print(arg_1)
        print(f1.lista)
        self.assertEqual(f1.lista, arg_1)
        

    def test_valor_modal(self):
        
        arg_1 = [4,2,3,4]
        self.assertEqual(F(arg_1).valor_modal(), [4,1])

    def test_creacion_incorrecta(self):
        arg_1 = [10,4]
        arg_2 = [2,1]
        
        with self.assertRaises(ValueError):
            F(arg_1, arg_2)


# 4) Probar una creación incorrecta y visualizar la salida del "raise"

# In[13]:




# 6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo

# In[14]:

class TestStringMethods(unittest.TestCase):
    #Funciones_Matematicas_test
    def test_creacion_correcta(self):
        arg_1 = [1,2,3,4]
        f1 = F(arg_1)
        print(arg_1)
        print(f1.lista)
        self.assertEqual(f1.lista, arg_1)
        

    def test_valor_modal(self):
        
        arg_1 = [4,2,3,4]
        self.assertEqual(F(arg_1).valor_modal(), [4,1])

    def test_creacion_incorrecta(self):
        arg_1 = [10,4]
        arg_2 = [2,1]
        
        with self.assertRaises(ValueError):
            F(arg_1, arg_2)

unittest.main(argv=[''], verbosity=2, exit=False)


# 7) Agregar casos de pruebas para el método conversion_grados()

# In[17]:




# 8) Agregar casos de pruebas para el método factorial()

# In[20]:




