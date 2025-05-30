palavra = input("Digite a palavra a ser verificada: ")
palavra = palavra.lower()
palavra = palavra.replace(" ", "")
palavra = palavra.replace(",", "")
palavra = palavra.replace(".", "")
palavra = palavra.replace("!", "")
palavra = palavra.replace("?", "")
palavra = palavra.replace("@", "")
palavra = palavra.replace("ã", "a")
palavra = palavra.replace("á", "a")
palavra = palavra.replace("â", "a")
palavra = palavra.replace("ê", "e")
palavra = palavra.replace("é", "e")
palavra = palavra.replace("í", "i")
palavra = palavra.replace("ó", "o")
palavra = palavra.replace("õ", "o")
invertida = palavra[::-1]

if invertida == palavra:
    print("\n\tSim\n")
else:
    print("\n\tNão\n")

input("encerrar execução?")