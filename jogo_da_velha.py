def exibir_tabuleiro(tabuleiro):
    print()
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("---------")
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("---------")
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
    print()


def verificar_vitoria(tabuleiro, simbolo):
    if tabuleiro[0] == simbolo and tabuleiro[1] == simbolo and tabuleiro[2] == simbolo:
        return True
    if tabuleiro[3] == simbolo and tabuleiro[4] == simbolo and tabuleiro[5] == simbolo:
        return True
    if tabuleiro[6] == simbolo and tabuleiro[7] == simbolo and tabuleiro[8] == simbolo:
        return True
    if tabuleiro[0] == simbolo and tabuleiro[3] == simbolo and tabuleiro[6] == simbolo:
        return True
    if tabuleiro[1] == simbolo and tabuleiro[4] == simbolo and tabuleiro[7] == simbolo:
        return True
    if tabuleiro[2] == simbolo and tabuleiro[5] == simbolo and tabuleiro[8] == simbolo:
        return True
    if tabuleiro[0] == simbolo and tabuleiro[4] == simbolo and tabuleiro[8] == simbolo:
        return True
    if tabuleiro[2] == simbolo and tabuleiro[4] == simbolo and tabuleiro[6] == simbolo:
        return True

    return False


def tabuleiro_cheio(tabuleiro):
    for i in range(len(tabuleiro)):
        if tabuleiro[i] == " ":
            return False
    return True


def procurar_jogada(tabuleiro, simbolo):
    for i in range(len(tabuleiro)):
        if tabuleiro[i] == " ":
            tabuleiro[i] = simbolo

            if verificar_vitoria(tabuleiro, simbolo):
                tabuleiro[i] = " "
                return i

            tabuleiro[i] = " "

    return -1


def jogada_maquina(tabuleiro):
    posicao = procurar_jogada(tabuleiro, "O")
    if posicao != -1:
        return posicao

    posicao = procurar_jogada(tabuleiro, "X")
    if posicao != -1:
        return posicao

    if tabuleiro[4] == " ":
        return 4

    cantos = [0, 2, 6, 8]

    for i in range(len(cantos)):
        if tabuleiro[cantos[i]] == " ":
            return cantos[i]

    for i in range(len(tabuleiro)):
        if tabuleiro[i] == " ":
            return i


tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

while True:
    exibir_tabuleiro(tabuleiro)

    posicao = int(input("Digite uma posição de 1 a 9: ")) - 1

    while posicao < 0 or posicao > 8 or tabuleiro[posicao] != " ":
        posicao = int(input("Posição inválida. Digite outra: ")) - 1

    tabuleiro[posicao] = "X"

    if verificar_vitoria(tabuleiro, "X"):
        exibir_tabuleiro(tabuleiro)
        print("Você venceu!")
        break

    if tabuleiro_cheio(tabuleiro):
        exibir_tabuleiro(tabuleiro)
        print("Empate!")
        break

    posicao_maquina = jogada_maquina(tabuleiro)
    tabuleiro[posicao_maquina] = "O"

    if verificar_vitoria(tabuleiro, "O"):
        exibir_tabuleiro(tabuleiro)
        print("A máquina venceu!")
        break

    if tabuleiro_cheio(tabuleiro):
        exibir_tabuleiro(tabuleiro)
        print("Empate!")
        break
