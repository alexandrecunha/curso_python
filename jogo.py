jogador1=input("Qual e o seu nome? ")
jogador2=input("Qual e o seu nome? ")
jogador=""
resultado="N"
print ()
print ()
print ("{} vai jogar com X " .format(jogador1))
print ("{} vai jogar com 0 " .format(jogador2))
coord = list(range(1,10))

def imprime_tela():
    print ()
    print (" {} | {} | {}" .format(coord[0],coord[1],coord[2]))
    print ("----------")
    print (" {} | {} | {}" .format(coord[3],coord[4],coord[5]))
    print ("----------")
    print (" {} | {} | {}" .format(coord[6],coord[7],coord[8]))
    print ()

def verifica_jogadas():
    global resultado
    if coord[0] == coord[1] == coord[2]:
        print ("{} ganhou o jogo".format(jogador))
        resultado = "G"
    elif coord[3] == coord[4] == coord[5]:
        print ("{} ganhou o jogo".format(jogador))
        resultado = "G"
    elif coord[6] == coord[7] == coord[8]:
        print ("{} ganhou o jogo".format(jogador))
        resultado = "G"
    elif coord[0] == coord[3] == coord[6]:
        print ("{} ganhou o jogo".format(jogador))
        resultado = "G"
    elif coord[1] == coord[4] == coord[7]:
        print ("{} ganhou o jogo".format(jogador))
        resultado = "G"
    elif coord[2] == coord[5] == coord[8]:
        print ("{} ganhou o jogo".format(jogador))
        resultado = "G"
    elif coord[0] == coord[4] == coord[8]:
        print ("{} ganhou o jogo".format(jogador))
        resultado = "G"
    elif coord[2] == coord[4] == coord[6]:
        print ("{} ganhou o jogo".format(jogador))
        resultado = "G"

imprime_tela()

num_jogadas = 9
jogador = jogador1
varjog = "X"
while num_jogadas >= 1:
        coordjog=int(input("Sua vez {}. Informe a posicao a ser jogada = ".format(jogador)))
        coord[coordjog - 1] = varjog
        num_jogadas = num_jogadas - 1
        imprime_tela()
        verifica_jogadas()
        if jogador == jogador1:
            jogador = jogador2
            varjog = "0"
        elif jogador == jogador2:
            jogador = jogador1
            varjog = "X"
        if resultado == "G":
            break
        else:
            continue
if num_jogadas == 0:
    print ("")
    print("*" * 9)
    print ("DEU VELHA")
    print("*" * 9)
