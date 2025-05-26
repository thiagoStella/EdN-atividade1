# 1- Conversor de Moeda

valor = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15
dolar = valor * taxa_dolar
euro = valor * taxa_euro
print(f"O valor de R$: {valor:.2f}, corresponde a: US$ {dolar:.2f} e € {euro:.2f}")

# 2- Calculadora de Desconto

nome_produto = "Camiseta"
preco = 50
desconto = 0.2
novo_preco = preco - (preco * desconto)
print("\n=== DETALHES ===")
print(f"{nome_produto} com valor original: R$ {preco:.2f}")
print(f"{nome_produto} com desconto: R$ {novo_preco:.2f}")
print("="*16)

# 3- Calculadora de Média Escolar

n1 = 7.5
n2 = 8.0
n3 = 6.5
media = (n1 + n2 + n3) / 3
print("\nAs notas do aluno foram:")
print("Primeiro trimestre: ", n1)
print("Segundo trimestre: ", n2)
print("Terceiro trimestre: ", n3)
print(f"A média do aluno é de: {media:.2f}")


# 4- Calculadora de Consumo de Combustível

distancia = 300
litros = 25
km_litro = distancia / litros
km_litro = int(km_litro)
print(f"\nA distancia percorrida entre o ponto A e o ponto B foi de {distancia} km, e foram gastos {litros} litros de combustivel, então a média de consumo é de {km_litro} kilometros por litro")



input("\nfinalizar?") #para travar a tela de prompt