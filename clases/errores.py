

""" numero = int(input("ingrese un numero:"))
print(numero) """




try:
    numero = int(input("ingrese un numero:"))
    print(numero)
except ValueError:
    print("no es numero valido porfavoe solo numeros")  
