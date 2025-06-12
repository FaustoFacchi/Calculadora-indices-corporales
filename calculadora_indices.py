def Calcular_IMC(peso, altura):
    altura = float(altura)
    altura = altura
    peso = int(peso)
    imc = peso / (altura * altura)
    return imc

def Calcular_GC(imc, edad, valor_genero):
    edad = int(edad)
    gc = 1.2 * imc + 0.23 * edad - 5.4 - valor_genero
    return round(gc, 2)

def Calcular_TMB(peso, altura, edad, valor_genero):
    peso = int(peso)
    altura = float(altura)
    altura = altura * 100
    edad = int(edad)
    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return round(tmb, 2)

def Calcular_CDA(tmb):
    calorias_max = tmb - (tmb * 15) / 100
    calorias_min = tmb - (tmb * 20) / 100
    calorias_max = round(calorias_max, 2)
    calorias_min = round(calorias_min, 2)
    return calorias_min, calorias_max
