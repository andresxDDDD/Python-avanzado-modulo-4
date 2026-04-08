

class Motor:
    def __init__(self,tipo):
        self.tipo = tipo



class Auto:
    def __init__(self,patente, motor):
        self.patente = patente
        self.motor = motor #composicion

class Cliente: 
    def __init__(self,nombre):
        self.nombre = nombre   
        self.autos= []
    def agregar_autos (self,auto):  
         self.autos.append(auto)  
    def __str__(self):
        return f"cliente 1: {self.nombre}"  

class Mecanico: 
    def __init__(self,nombre):
        self.nombre = nombre

    def reparar_auto(selft,auto):
        return f"Reparando auto"   
    
class Reparacion:
    def __init__(self,auto,mecanico):
        self.auto = auto
        self.mecanico = mecanico
    def __str__(self):
        return f"El auto patente: {self.auto.patente} esta siendo arreglado por el mecanico: {self.mecanico.nombre}"
pepito = Cliente("Pepito") 
print(pepito)  

motor= Motor("v8")

auto1= Auto("xx-69",motor)
print(auto1)

mecanico1= Mecanico("Federico")
print(mecanico1)

reparacion1= Reparacion(auto1,mecanico1)
print(reparacion1)