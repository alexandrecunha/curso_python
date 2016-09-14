jogador1=input("Qual e o seu nome? ")
jogador2=input("Qual e o seu nome? ")
varx="X"
var0="0"
print ("{} vai jogar com X " .format(jogador1))
print ("{} vai jogar com 0 " .format(jogador2))
coord = list(range(1,10))
print (" {} | {} | {}" .format(coord[0],coord[1],coord[2]))
print ("----------")
print (" {} | {} | {}" .format(coord[3],coord[4],coord[5]))
print ("----------")
print (" {} | {} | {}" .format(coord[6],coord[7],coord[8]))
print ("{} escolha uma posicao para jogar" .format(jogador1))
jogadas = 9
while jogadas >= 1:
       	jogadas = jogadas - 1
       	coordjog1=int(input("Sua vez {}. Informe a posicao a ser jogada = ".format(jogador1)))
        coord[coordjog1 - 1] = varx
     #   	if coordjog1 == 1:
     #   		coord[0]=varx
     #   	elif coordjog1 == 2:
     #   		coord[1]=varx
     #   	elif coordjog1 == 3:
     #   		coord[2]=varx
     #   	elif coordjog1 == 4:
     #   		coord[3]=varx
     #   	elif coordjog1 == 5:
     #   		coord[4]=varx
     #   	elif coordjog1 == 6:
     #   		coord[5]=varx
     #   	elif coordjog1 == 7:
     #   		coord[6]=varx
     #   	elif coordjog1 == 8:
     #   		coord[7]=varx
     #   	elif coordjog1 == 9:
     #   		coord[8]=varx
       	print (" {} | {} | {}" .format(coord[0],coord[1],coord[2]))
       	print ("----------")
       	print (" {} | {} | {}" .format(coord[3],coord[4],coord[5]))
       	print ("----------")
       	print (" {} | {} | {}" .format(coord[6],coord[7],coord[8]))
       	if coord[0] == coord[1] == coord[2]:
       		print ("{} ganhou o jogo".format(jogador1))
       		break
       	elif coord[3] == coord[4] == coord[5]:
                print ("{} ganhou o jogo".format(jogador1))
                break
       	elif coord[6] == coord[7] == coord[8]:
                print ("{} ganhou o jogo".format(jogador1))
                break
       	elif coord[0] == coord[3] == coord[6]:
                print ("{} ganhou o jogo".format(jogador1))
                break
       	elif coord[1] == coord[4] == coord[7]:
                print ("{} ganhou o jogo".format(jogador1))
                break
       	elif coord[2] == coord[5] == coord[8]:
                print ("{} ganhou o jogo".format(jogador1))
                break
       	elif coord[0] == coord[4] == coord[8]:
                print ("{} ganhou o jogo".format(jogador1))
                break
       	elif coord[2] == coord[4] == coord[6]:
                print ("{} ganhou o jogo".format(jogador1))
                break
       	jogadas = jogadas - 1
       	coordjog2=float(input("Sua vez {}. Informe a posicao a ser jogada = ".format(jogador2)))
       	if coordjog2 == 1:
                coord[0]=var0
       	elif coordjog2 == 2:
                coord[1]=var0
       	elif coordjog2 == 3:
       		coord[2]=var0
       	elif coordjog2 == 4:
                coord[3]=var0
       	elif coordjog2 == 5:
       		coord[4]=var0
       	elif coordjog2 == 6:
       		coord[5]=var0
       	elif coordjog2 == 7:
       		coord[6]=var0
       	elif coordjog2 == 8:
       		coord[7]=var0
       	elif coordjog2 == 9:
       		coord[8]=var0
       	print (" {} | {} | {}" .format(coord[0],coord[1],coord[2]))
       	print ("----------")
       	print (" {} | {} | {}" .format(coord[3],coord[4],coord[5]))
       	print ("----------")
       	print (" {} | {} | {}" .format(coord[6],coord[7],coord[8]))
       	if coord[0] == coord[1] == coord[2]:
       		print ("{} ganhou o jogo".format(jogador2))
       		break
       	elif coord[3] == coord[4] == coord[5]:
       		print ("{} ganhou o jogo".format(jogador2))
       		break
       	elif coord[6] == coord[7] == coord[8]:
       		print ("{} ganhou o jogo".format(jogador2))
       		break
       	elif coord[0] == coord[3] == coord[6]:
       		print ("{} ganhou o jogo".format(jogador2))
       		break
       	elif coord[1] == coord[4] == coord[7]:
       		print ("{} ganhou o jogo".format(jogador2))
       		break
       	elif coord[2] == coord[5] == coord[8]:
       		print ("{} ganhou o jogo".format(jogador2))
       		break
       	elif coord[0] == coord[4] == coord[8]:
       		print ("{} ganhou o jogo".format(jogador2))
       		break
       	elif coord[2] == coord[4] == coord[6]:
       		print ("{} ganhou o jogo".format(jogador2))
       		break
