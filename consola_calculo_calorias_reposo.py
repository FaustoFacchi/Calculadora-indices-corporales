from calculadora_indices import Calcular_TMB
def ejecutar():
    print("CALCULADORA TMB\nGénero\nMasculino(1)\nFemenino(2)")
    while True:
        genero = input("Indique:")
        if genero == '1':
            valor_genero = 5
            break
        elif genero == '2':
            valor_genero = -161
            break
        else:
            print("Entrada inválida. Por favor ingrese 1 (Masculino) o 2 (Femenino).")

    while True:
        edad = int(input("Coloque su edad:"))
        if edad > 0:
            break
        else:
                print("Peso invalido, ingrese un valor mayor a 0")   

    while True:
        peso = float(input("Coloque su peso en kg:"))
        if peso > 0:
            break
        else:
            print("Peso invalido, ingrese un valor mayor a 0")

    while True:
        altura = float(input("Coloque su altura en m:"))
        if altura > 0:
            break
        else:
            print("Altura invalida, ingrese un valor mayor a 0")

    tmbReposo = Calcular_TMB(peso, altura, edad, valor_genero)
    print ("La tasa metablólica basal en reposo es de:", tmbReposo, "cal")