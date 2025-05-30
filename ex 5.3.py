import datetime

def idade_em_dias(ano_atual, ano_nascimento):
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias
try:
    ano_atual = datetime.datetime.now().year
    ano_nascimento = input("informe o ano de nascimento com 4 digitos: ")
    if len(ano_nascimento) != 4:
        print("Ano invalido! Informe o ano com 4 digitos (ex: 1997)")
        input("Encerrando a aplicação!")
        exit()
    else:
        ano_nascimento = int(ano_nascimento)
    if ano_nascimento < 1900 or ano_nascimento > ano_atual:
        print(f"Ano inválido! O ano de nascimento deve ser entre 1900 e {ano_atual}.")
        input("Encerrando a aplicação!")
        exit()    
    dias = idade_em_dias(ano_atual, ano_nascimento)
    print(f"\nVocê nasceu em {ano_nascimento}, e estamos em {ano_atual}")
    print(f"\nVocê está vivo a {dias} dias")
    
except ValueError:
    print("Ano invalido! Informe o ano com 4 digitos (ex: 1997)")
    input("Encerrando a aplicação!")

except Exception as e:
    print("APENAS NUMEROS! Erro: {e}")
    input("Encerrando a aplicação")
finally:
    input("\nDeseja encerrar?")