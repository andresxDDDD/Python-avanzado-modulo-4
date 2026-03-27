

class Usuario: 
    def __init__(self,username,email,password,activo):
        self.username = username
        self.email = email
        self.password = password
        self.activo = activo

    def login(self,passw):
        if self.password != passw:
            print("password incorrecto")
        else:
            print("password correcta")    

        pass
    def leer(self):
        print(f"nombre:{self.username} email: {self.email} activo: {self.activvo}")


    def desactivar(self):
        self.activo = False
        pass    


usario1= Usuario("juanito","correo@corre.cl","1234",True)
usuario1.