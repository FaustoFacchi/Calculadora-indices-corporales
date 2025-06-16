from calculadora_indices import Calcular_IMC
def ejecutar():
    print("CALCULADORA IMC")
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
    imc = Calcular_IMC(peso, altura)
    print ("la IMC es de:", imc)