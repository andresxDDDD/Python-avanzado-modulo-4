

""" numero = int(input("ingrese un numero:"))
print(numero) """




""" try:
    numero = int(input("ingrese un numero:"))
    print(numero)
except ValueError:
    print("no es numero valido por favor solo numeros")
 """


#try y el except

# raise, else finally
# regla: que la edad sea superior o igaul a 0

edad =-5

if edad < 0:
    raise ValueError("la edad no puede ser menor a 0")
