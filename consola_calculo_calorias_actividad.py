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
peso = input("Coloque su peso en kg:")
altura = input("Coloque su altura en m:")
print ("1.2: poco o ningún ejercicio\n1.375: ejercicio ligero (1 a 3 días a la semana)" \
"\n1.55: ejercicio moderado (3 a 5 días a la semana)\n1.72: deportista (6 -7 días a la semana)" \
"\n1.9: atleta (entrenamientos mañana y tarde.")
actividad = float(input("Ingrese actividad fisica segun la tabla:"))
tmbReposo = Calcular_TMB(peso, altura, edad, valor_genero)
tmbactividad = tmbReposo * actividad
tmbactividad = round(tmbactividad, 2)
print ("La tasa metablólica basal en actividad es de:",tmbactividad , "cal")