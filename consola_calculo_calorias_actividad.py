from calculadora_indices import Calcular_TMB
def ejecutar():
    print("CALCULADORA TMB(actividad)\nGénero\nMasculino(1)\nFemenino(2)")
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

    print ("1.2: poco o ningún ejercicio\n1.375: ejercicio ligero (1 a 3 días a la semana)" \
    "\n1.55: ejercicio moderado (3 a 5 días a la semana)\n1.72: deportista (6 -7 días a la semana)" \
    "\n1.9: atleta (entrenamientos mañana y tarde.")
    actividad = float(input("Ingrese actividad fisica segun la tabla:"))
    tmbReposo = Calcular_TMB(peso, altura, edad, valor_genero)
    tmbactividad = tmbReposo * actividad
    tmbactividad = round(tmbactividad, 2)
    print ("La tasa metablólica basal en actividad es de:",tmbactividad , "cal")