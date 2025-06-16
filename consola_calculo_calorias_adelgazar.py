import calculadora_indices as calc

try:
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    edad = int(input("Edad: "))
    genero = int(input("Genero: 1 masculino, 2 femenino: "))
    valor_genero = 5 if genero == 1 else -161
    mensaje = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print(mensaje)
except:
    print("Datos invalidos, usa numeros.")
