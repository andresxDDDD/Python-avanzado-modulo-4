

#read lectura
""" 
archivo = open("prueba.txt","r")
contenido = archivo.read()
print(contenido)
archivo.close """


#leer linea a linea
""" 
f = open("archivo.txt","r")
for linea in f:
    print(linea)
f.close()    

# escritura

archivo = open("archivo.txt","w")
archivo.write("hola")"""

# append
#no borra solo agrega

""" f = open("archivo.txt","a")
f.write("como estas\n")
f.close() """


with open ("archivo.txt","a") as f:
    f.write("pepito\n")
