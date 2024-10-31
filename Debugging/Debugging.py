def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def comparar_con_promedio(numeros, promedio):
    for num in numeros:
        if num > promedio:#Falta de ":"
            print(f"{num} es mayor que el promedio.")
        elif num < promedio:#Falta de ":"
            print(f"{num} es menor que el promedio.")
        else:#Falta de ":"
            print(f"{num} es igual al promedio.")

# Pedir al usuario tres números
numeros = []
while len(numeros) < 3: #Aseugurarse de obtener 3 valores para la lista
    num = input("Introduce un número: ")
    if num.isnumeric() == True: # Comprobar que sea numerico
        numeros.append(float(num))# Convertir a un valor numérico
    else:
        print("Eso no es un valor numérico")

# Calcular el promedio
promedio = calcular_promedio(numeros)

# Comparar cada número con el promedio
comparar_con_promedio(numeros, promedio)










