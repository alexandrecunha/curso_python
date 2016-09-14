import os

def limpar_tela():
    try:
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 130
    print("\n" * lines)

def imprime_tela(coord):
    print ("\n")
    print ("  {} ┃ {} ┃ {} ".format(coord[0],coord[1],coord[2]))
    print (" ━━━╋━━━╋━━━ ")
    print ("  {} ┃ {} ┃ {} ".format(coord[3],coord[4],coord[5]))
    print (" ━━━╋━━━╋━━━ ")
    print ("  {} ┃ {} ┃ {} ".format(coord[6],coord[7],coord[8]))
    print ("\n")

def verifica_jogadas(coord, resultado, jogador):
    if coord[0] == coord[1] == coord[2]:
        print ("{} ganhou o jogo 🎉".format(jogador))
        resultado = "G"
    elif coord[3] == coord[4] == coord[5]:
        print ("{} ganhou o jogo 🎉".format(jogador))
        resultado = "G"
    elif coord[6] == coord[7] == coord[8]:
        print ("{} ganhou o jogo 🎉".format(jogador))
        resultado = "G"
    elif coord[0] == coord[3] == coord[6]:
        print ("{} ganhou o jogo 🎉".format(jogador))
        resultado = "G"
    elif coord[1] == coord[4] == coord[7]:
        print ("{} ganhou o jogo 🎉".format(jogador))
        resultado = "G"
    elif coord[2] == coord[5] == coord[8]:
        print ("{} ganhou o jogo 🎉".format(jogador))
        resultado = "G"
    elif coord[0] == coord[4] == coord[8]:
        print ("{} ganhou o jogo 🎉".format(jogador))
        resultado = "G"
    elif coord[2] == coord[4] == coord[6]:
        print ("{} ganhou o jogo 🎉".format(jogador))
        resultado = "G"

def informa_jogadores():
    jogador1=input("Qual e o seu nome? ")
    jogador2=input("Qual e o seu nome? ")
    limpar_tela()
    return jogador1, jogador2

def informa_x_o(jogador1, jogador2):
    print ("╔═══════════════╗")
    print ("║ JOGO DA VELHA ║")
    print ("╚═══════════════╝")
    print ("{} vai jogar com ❌ " .format(jogador1))
    print ("{} vai jogar com ⭕️ " .format(jogador2))

def recebe_jogada(jogador1, jogador2, coord, resultado):
    num_jogadas = 9
    jogador = jogador1
    varjog = "❌"
    while num_jogadas >= 1:
            coordjog=int(input("Sua vez {}. Informe a posicao a ser jogada = ".format(jogador)))
            coord[coordjog - 1] = varjog
            num_jogadas = num_jogadas - 1
            limpar_tela()
            informa_x_o(jogador1, jogador2)
            imprime_tela(coord)
            #verifica_jogadas()
            if jogador == jogador1:
                jogador = jogador2
                varjog = "⭕️"
            elif jogador == jogador2:
                jogador = jogador1
                varjog = "❌"
                if resultado == "G":
                    break
                else:
                    continue
            if num_jogadas == 0:
                print ("")
                print ("DEU VELHA")

def jogar():
    #resultado ="N"
    #jogador =""
    coord = tabuleiro()
    resultado, jogador = variaveis()
    limpar_tela()
    jogador1, jogador2 = informa_jogadores()
    informa_x_o(jogador1, jogador2)
    imprime_tela(coord)
    recebe_jogada(jogador1, jogador2, coord, resultado)
    imprime_tela(coord)
    verifica_jogadas(coord, resultado, jogador)


def tabuleiro():
    coord = list(range(1,10))
    return coord

def variaveis():
    resultado ="N"
    jogador =""
    return resultado, jogador

jogar()
