# 1- Escreva um código que exiba a mensagem na tela.

print("\nOlá Mundo!")

# 2- Calculadora de Soma

n1 = 4
n2 = 6
soma = n1 + n2
print("\nO resultados da soma é :", soma)

# 3-Calculadora de Volume

comprimento = 3
largura = 4
altura = 4
volume = comprimento * largura * altura
print("\nO volume do retângulangulo é: ", volume, "cm³")

# 4- Calculadora de Preço Total

nome_produto = "Feijão Caldo Bom 1kg"
preco_unitario = 6.20
quantidade = 3
total = preco_unitario * quantidade
print("\n=== NOTA FISCAL ===")
print("*", nome_produto)
print(f"* Preço com o clube: R$ {preco_unitario:.2f}")
print("* Quantidade", quantidade)
print(f"* Preço Total: R$ {total:.2f}")
print("=" *19)

input("\nfinalizar?") #para travar a tela de prompt
