import calculadora_indices as calc

try:
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    edad = int(input("Edad: "))
    genero = int(input("Genero: 1 masculino, 2 femenino: "))
    valor_genero = 5 if genero == 1 else -161
    calorias = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print("Calorias en reposo:", int(calorias))
except:
    print("Error ingresa bien los datos.")