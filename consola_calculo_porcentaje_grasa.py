from calculadora_indices import Calcular_GC
from calculadora_indices import Calcular_IMC
def ejecutar():
    print("CALCULADORA PORCENTAJE GRASA CORPORAL\nGénero\nMasculino(1)\nFemenino(2)")
    while True:
        genero = input("Indique:")
        if genero == '1':
            valor_genero = 10.8
            break
        elif genero == '2':
            valor_genero = 0
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
    imc = Calcular_IMC(peso, altura)
    gc = Calcular_GC(imc, edad, valor_genero)
    print ("el porcentaje de grasa corporal es:", gc,"%")