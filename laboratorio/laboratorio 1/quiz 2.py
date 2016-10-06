diccionario={"agua":0, "fuego":0}
lista=[]
cd="true"
X=0

while cd=="true":
    lista.append(input("introduce una oracion: "))
    if "fuego" in diccionario:
        X=X+1
    elif "agua" in diccionario:
        X=X+1

    a=input("deseas salir del programa: ")
    if a=="si" or a=="Si":
        print("saliendo del programa.")
        break
    else:
        pass

print("fuego: " + str(X))
print("agua: " + str(X))
print(lista)