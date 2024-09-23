# verificar o IMC (peso/altura)
PESO = int(input("digite o peso: "))
ALTURA = float(input("digite a altura: "))

# Calculo do imc
IMC = PESO / ALTURA ** 2

# Exibição dos resultados
if IMC < 18:
    print
