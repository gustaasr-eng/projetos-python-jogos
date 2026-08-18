def mostrar_palavra(palavra, letras_acertadas):
    retorno = ""

    for i in range(len(palavra)):
        if palavra[i] in letras_acertadas:
            retorno += palavra[i] + " "
        else:
            retorno += "_ "

    return retorno

def venceu(palavra, letras_acertadas):
    for i in range(len(palavra)):
        if palavra[i] not in letras_acertadas:
            return False

    return True

palavra = "python"
letras_acertadas = []
tentativas = 6

while tentativas > 0 and not venceu(palavra, letras_acertadas):

    print()
    print("Palavra:", mostrar_palavra(palavra, letras_acertadas))
    print("Tentativas restantes:", tentativas)

    letra = input("Digite uma letra: ")

    if letra in letras_acertadas:
        print("Você já digitou essa letra.")
    else:
        letras_acertadas.append(letra)

        if letra not in palavra:
            tentativas -= 1
            print("Letra incorreta.")

if venceu(palavra, letras_acertadas):
    print()
    print("Parabéns! Você acertou a palavra:", palavra)
else:
    print()
    print("Você perdeu!")
    print("A palavra era:", palavra)
