# 1- Classificador de Idade

idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12:
        print("Você é criança")
elif idade >12 and idade <= 17:
        print("Você é adolescente")
elif idade > 17 and idade <= 59:
        print("Você é adulto")
elif idade > 59:
        print("Você é idoso")
else:
        print("Idade inválida")

# 2- Calculadora de IMC (peso pela altura ao quadrado)
peso = float(input("\nDigite seu peso: "))
altura = float(input("Digite sua altura (sem casas decimais): "))
altura = altura / 100
imc = peso / (altura **2)
if imc < 18.5:
        print("Abaixo do peso")
elif imc < 25:
        print("Peso normal")
elif imc < 30:
        print("Sobrepeso")
elif imc > 29:
        print("Obeso")
else:
        print("Valor inválido")

#3- Conversor de Temperatura

temperatura = float(input("\nDigite a temperatura a ser convertida: "))
origem = input("De qual unidade é essa temperatura? (c, k, f) ")
origem = origem.lower() 
destino = input("Para qual unidade deseja converter? (c, k, f) ")
destino = destino.lower() 

if origem == "c" and destino == "f":
    resultado = (temperatura * 9/5) + 32
    print(f"A temperatura convertida é de: {resultado:.2f}°F") # Corrigido: usando f-string para formatar

elif origem == "c" and destino == "k":
    resultado = (temperatura + 273.15)
    print(f"A temperatura convertida é de: {resultado:.2f}K")

elif origem == "f" and destino == "c":
    resultado = (temperatura - 32) / 1.8
    print(f"A temperatura convertida é de: {resultado:.2f}°C")

elif origem == "f" and destino == "k":
    resultado = (temperatura - 32) * 5/9 + 273.15
    print(f"A temperatura convertida é de: {resultado:.2f}K")

elif origem == "k" and destino == "c":
    resultado = (temperatura - 273.15)
    print(f"A temperatura convertida é de: {resultado:.2f}°C")

elif origem == "k" and destino == "f":
    resultado = (temperatura - 273.15) * 9/5 + 32
    print(f"A temperatura convertida é de: {resultado:.2f}°F")

elif origem == destino: # Adicionado: caso a unidade de origem seja igual à de destino
    print(f"A temperatura já está na unidade desejada: {temperatura:.2f}{origem.upper()}") # Mostra a unidade original

else:
    print("Ocorreu um erro, verifique seus dados ou unidades!")


input("\nfinalizar?") #para travar a tela de prompt