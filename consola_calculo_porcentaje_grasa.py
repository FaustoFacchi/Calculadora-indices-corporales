from calculadora_indices import Calcular_GC
from calculadora_indices import Calcular_IMC
def pedir_genero():
    while True:
        valor_genero = input("Género\nMasculino .1\nFemenino .2\nIndique: ")
        if valor_genero == '1':
            return 10.8
        elif valor_genero == '2':
            return 0
        else:
            print("Entrada inválida. Por favor ingrese 1 (Masculino) o 2 (Femenino).")
valor_genero = pedir_genero()
edad = input("Coloque su edad:")
peso = input("Coloque su peso en kg:")
altura = input("Coloque su altura en m:")
imc = Calcular_IMC(peso, altura)
gc = Calcular_GC(imc, edad, valor_genero)
print ("el porcentaje de grasa corporal es:", gc,"%")