#clase personna tiene que comenzar con Mayuscula 



class Persona:
    def __init__(self,nombre,edad,rut):
        self.nombre = nombre
        self. edad = edad
        self.rut = rut

    def saludar(self):
        print(f"hola mi nombre es: {self.nombre} y tengo {self.edad}")

    def cumplir_anios(self):
        self.edad +=1

    def verificar_rut(selft):
        if selft.rut==0:
            print("sin rut")  
        else:
            print("rut listo")
                  


    
# intancia
juanito = Persona("juanito",34,123456)
carlos = Persona("claudia", 25,123456)
print(juanito)
print(juanito.saludar())
print(juanito.cumplir_anios())
print(juanito.saludar())