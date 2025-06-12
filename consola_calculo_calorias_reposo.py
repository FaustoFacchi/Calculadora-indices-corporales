from calculadora_indices import Calcular_TMB
def pedir_genero():
    while True:
        valor_genero = input("Género\nMasculino .1\nFemenino .2\nIndique: ")
        if valor_genero == '1':
            return 5
        elif valor_genero == '2':
            return -161
        else:
            print("Entrada inválida. Por favor ingrese 1 (Masculino) o 2 (Femenino).")
valor_genero = pedir_genero()
edad = input("Coloque su edad:")
altura = input("Coloque su altura en m:")
peso = input("Coloque su peso en kg:")

tmbReposo = Calcular_TMB(peso, altura, edad, valor_genero)
print ("La tasa metablólica basal en reposo es de:", tmbReposo, "cal")