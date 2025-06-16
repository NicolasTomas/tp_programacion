import calculadora_indices as calc

def grasa_recomendada(edad, genero):
    if genero == 1:
        if edad < 30:
            return "11% - 20%"
        elif edad < 40:
            return "12% - 21%"
        elif edad < 50:
            return "14% - 23%"
        else:
            return "15% - 24%"
    else:
        if edad < 30:
            return "16% - 28%"
        elif edad < 40:
            return "17% - 29%"
        elif edad < 50:
            return "18% - 30%"
        else:
            return "19% - 31%"

try:
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    edad = int(input("Edad: "))
    genero = int(input("Género: 1 para masculino, 2 para femenino: "))
    valor_genero = 10.8 if genero == 1 else 0
    grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print("Grasa corporal:", round(grasa, 2), "%")
    print("Rango recomendado:", grasa_recomendada(edad, genero))
except:
    print("Error en los datos. Ingresá números.")


