class Transaccion:
    def __init__(self, monto,descripcion):
        self.__monto = monto
        self.descripcion = descripcion

    def get_monto(self):
        return self.__monto 

    def set_monto(self,monto):
        if monto > 0:
            self.__monto = monto
        else: 
            print("monto ingresado es 0 o menor de 0")


    def tipo(self):
        pass
    def mostrar(self):
        return f"{self.descripcion} - {self.get_monto} - {self.tipo()}"

class Ingreso(Transaccion): 
    #poliformismo del metodo tipo de la clase transaccion 
    def tipo(self):
        return("Trasaccion")
class Egreso(Transaccion):
    pass

pago1 = Transaccion(100,"pago banco")
print(pago1)



class GestorFinanzas:
    def __init__(self):
        self.transacciones=[]
        pass
    def agregar(self,transaccion):
        self.transacciones.append(transaccion)
    def calcular_balance(self):
        pass
    def guardar_en_archivo(self):
        pass
    def importar_en_archivo(self):
        pass
    def mostrar_todo(self):
        if not self.transacciones:
            print("lista vacia") 
        for transaccion  in self.transacciones:
            print(transaccion.mostrar())      
