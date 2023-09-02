class Funciones_Matematicas:
    def __init__(self,lista):
        assert type(lista) == list,"Se debe ingresar una lista de numeros"
        self.lista = lista

    def verificar_primo_lista(self):
        nuevalista = []
        for i in self.lista:
            #if (self.verificar_primo(i)):
            #    print(i, 'es primo')
            #else:
            #    print(i, 'no es primo')
            nuevalista.append(self.verificar_primo(i))
        return nuevalista

    def conversion_grados_lista(self, origen, destino):
        nuevalista = []
        for i in self.lista:
            nuevalista.append(self.conversion_grados(i, origen, destino))
        return nuevalista

    def factorial_lista(self):
        nuevalista = []
        for i in self.lista:
            nuevalista.append(self.factorial(i))
        return nuevalista

    def verificar_primo(self ,numero):
        if numero == 2 or numero == 3:
            return True
        if numero % 2 == 0:
            return False
        else:
            for i in range(3, int(numero ** 0.5) + 1, 2):
                if numero % i == 0:
                    return False
        return True
    
    def factorial(self, n):
        if n < 1 or n != int(n):
            return "El numero ingresado no es un numero natural"
        contador = 1
        resultado = 1
        while contador < n:
            resultado = resultado * (contador + 1)
            contador+=1
        return resultado

    def valor_modal(self):
        reps = 0
        max_reps = 0
        max_rep_n = 0
        start = 1
        
        n = start
        for i in self.lista:
            while n < len(self.lista):
                if i == self.lista[n]:
                    reps += 1
                    if reps > max_reps:
                        max_reps = reps
                        max_rep_n = i
                n += 1
            reps = 0
            start += 1
            n = start
        return [max_rep_n , max_reps]
    
    def conversion_grados(self, temp, origen, cambio):
        """ strings °C, °F Y °K"""
        assert origen == "°C" or origen == "°F" or origen == "°K","Se deben ingresar las siglas de temperatura °C, °F o °K"
        assert cambio == "°C" or cambio == "°F" or cambio == "°K","Se deben ingresar las siglas de temperatura °C, °F o °K"
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


