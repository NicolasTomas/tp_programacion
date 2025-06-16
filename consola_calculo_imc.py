import calculadora_indices as calc

def categoria_imc(imc):
    if imc < 16:
        return "Delgadez Severa"
    elif imc < 17:
        return "Delgadez Moderada"
    elif imc < 18.5:
        return "Delgadez Aceptable"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad Tipo 1"
    elif imc < 40:
        return "Obesidad Tipo 2 "
    elif imc < 50:
        return "Obesidad Tipo 3"
    else:
        return "Obesidad Tipo 4 "

try:
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresad tu altura en metros:"))
    imc = calc.calcular_IMC(peso, altura)
    categoria = categoria_imc(imc)
    print("Tu IMC es:", round(imc, 2))
    print("Categoria:", categoria)
except:
    print("Error, ingresa numeros validos")
