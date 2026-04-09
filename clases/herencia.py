

class Animal:
    def __init__(self,nombre):
        self.nombre = nombre

    def respirar(self):
        print("respirando")

        


class Perro(Animal):
    def ladrar(self):
        print("guau guau")

firulais = Perro("firulais")
firulais.respirar() #metodo de animal que fue heredado
firulais.ladrar() #metodo de la propia clase perro 
    

#Poliformismo


class Ave:
    def volar(self): #metodo sin implementacion 
        pass

ave = Ave()
ave.volar()     

class Aguila(Ave):
    def volar(self): # se sobreescribe el metodo
        print("ando volando soy un aguila")

pichon = Aguila()
pichon.volar()




#isimstance]()

class Pago:
    def __init__(self,monto):
       self.monto = monto

class Efectivo(Pago):
    pass

class Tarjeta(Pago):
    pass

class Cheque(Pago):
    pass



def verificar_pago(obj):   
    if  not isinstance(obj,Pago):
        print("Este objeto no es un pago valido")
    if isinstance(obj,Efectivo):
        print("abriendo caja manual") 
    if isinstance(obj,Tarjeta):
        print("procesando pago")   

pagare = Pago(100)
cheque1 = Cheque(100)
tarjeta1 = Tarjeta(100)
efectivo = Efectivo(100)

verificar_pago(pagare)
    