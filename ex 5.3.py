import datetime

def idade_em_dias(ano_atual, ano_nascimento):
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

ano_atual = datetime.datetime.now().year
ano_nascimento = int(input("informe o ano de nascimento com 4 digitos: "))


dias = idade_em_dias(ano_atual, ano_nascimento)

print(f"Vo^ce nasceu em {ano_nascimento}, e estamos em {ano_atual}")
print(f"Você está vivo a {dias} dias")

input("Deseja encerrar?")