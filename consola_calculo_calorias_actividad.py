import calculadora_indices as calc

niveles = {
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.72,
    5: 1.9
}

try:
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    edad = int(input("Edad: "))
    genero = int(input("Gnero: 1 masculino, 2 femenino: "))
    actividad = int(input("Nivel actividad (1 a 5): "))
    valor_genero = 5 if genero == 1 else -161
    valor_actividad = niveles.get(actividad, 1.2)
    calorias = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print("Calorias con actividad:", int(calorias))
except:
    print("Error al ingresar datos.")