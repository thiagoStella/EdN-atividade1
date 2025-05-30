'''https://www.google.com/search?q=qual+o+valor+medio+de+uma+gorjeta&rlz=1C1GCEA_enRO1052BR1101&oq=qual+o+valor+medio+de+uma+gorjeta&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRifBTIHCAUQIRifBTIHCAYQIRifBTIHCAcQIRifBTIHCAgQIRifBTIHCAkQIRifBdIBCDU2NTVqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8'''

PROCENTAGEM_FIXA = 0.13

def gorjetinha(PROCENTAGEM_FIXA, valor_conta):
    gorjeta = valor_conta * PROCENTAGEM_FIXA
    return gorjeta

valor_conta = float(input("Informe o valor da conta para calcular o gorjeta: "))
valor_gorjeta = gorjetinha(PROCENTAGEM_FIXA, valor_conta)

print("====== BAR DO TIÃO ======")
print(f"\nServices: R$ {valor_conta}")
print(f"\nTax:      {PROCENTAGEM_FIXA * 100}%")
print(f"\nTip:      R$ {valor_gorjeta}")
print(f"\nTotal:    R$ {valor_conta + valor_gorjeta}")

input("\n\nVai a saideira?")