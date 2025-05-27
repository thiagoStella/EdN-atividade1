# Calculadora
resultado = 0
while True:
    primeiro = input("Digite o valor da primeira operação: ")
    if primeiro.isdigit():
        primeiro = int(primeiro)
    else:
        print("Somente numeros na operação!")
    
    operacao = input("Qual operação a ser realizada?")

    segundo = input("Digite o valor da segunda operação: ")
    if segundo.isdigit():
        segundo = int(segundo)
    else:
        print("Somente numeros na operação!")
        

    if operacao == "+":
        resultado = primeiro + segundo

    elif operacao == "-":
        resultado = primeiro - segundo

    elif operacao == "*":
        resultado = primeiro * segundo

    elif operacao == "/":
        if segundo == 0:
            print("Não é possivel realizar divisao por zero")
        else:
            resultado = primeiro / segundo

    else:
        print("Operação não encontrada!!")
        

    print(resultado)
# 2 Crie um programa para o professor registrar as notas da turma.

soma = 0
i = 0
print("Digite as notas (de 0 a 10, apenas inteiros positivos) ou 'fim' para calcular a média e sair.")

while True:
    num = input("Digite a nota: ")
    if num == "fim":
        break
    if num.isdigit():
        nota = int(num)
        if 0 <= nota <= 10:
            soma += nota
            i += 1
        else:
            print("Valor inválido! A nota deve estar entre 0 e 10.")
    else:
        print("Entrada inválida! Por favor, digite um número inteiro positivo ou 'fim'.")

if i > 0:
    media = soma / i
    print("\n--- Resultado Final ---")
    print(f"Total de notas registradas: {i}")
    print(f"A média das notas informadas é: {media:.2f}")
else:
    print("\nNenhuma nota válida foi registrada para calcular a média.")

print("Programa encerrado.")

input("Encerrar?")