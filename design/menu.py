from logic.formula import hi

def design():
    print("Bienvenido a el mejor sistema del mundo")
    print("     0.Atras")
    print("     1.Deseas que nuestra maquina salude")
    opc=int(input("Elija una de las opciones disponibles"))
    if(opc == 1):
        name = input ("Ingrese su nombre: ")
        result = hi(name)
        print(result)
    return opc