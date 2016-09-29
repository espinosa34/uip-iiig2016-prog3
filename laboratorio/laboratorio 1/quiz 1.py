print("Juan, el callado")

a="True"

while a=="True":
    pregunta = input("su pregunta: ")

    if pregunta.endswith("?"):
        print("ofi")
    elif pregunta.isupper():
        print("chillea")
    elif not pregunta:
        print("Mmmm")
    else:
        print("me da igual")

    a=input("desea volver a preguntar")
    print(a)

print("dialogo terminado")