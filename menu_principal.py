from consola_calculo_imc import ejecutar as imc
from consola_calculo_porcentaje_grasa import ejecutar as grasa
from consola_calculo_calorias_adelgazar import ejecutar as adelgazar
from consola_calculo_calorias_reposo import ejecutar as reposo
from consola_calculo_calorias_actividad import ejecutar as actividad
def mostrar_menu():
    print("MENU DE CALCULOS CORPORALES")
    print("1. Calcular IMC")
    print("2. Calcular Porcentaje de Grasa Corporal")
    print("3. Calcular Calorias para Adelgazar")
    print("4. Calcular Calorias por Reposo")
    print("5. Calcular Calorias por Actividad")
    print("0. Salir")

while True:
    mostrar_menu()
    opcion = input("Elegi una opcion: ")

    if opcion == "1":
        imc()
    elif opcion == "2":
        grasa()
    elif opcion == "3":
        adelgazar()
    elif opcion == "4":
        reposo()
    elif opcion == "5":
        actividad()
    elif opcion == "0":
        print("¡Nos vemos!")
        break
    else:
        print("Opcion invalida.Por favor, intenta de nuevo.")