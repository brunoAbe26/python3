from random import randrange

def jogar():
	print('*********************************')
	print('Bem vindo ao Jogo de Adivinhação!')
	print('*********************************')

	nome = input("Digite seu nome: ")
	print('{}, escolha o nível de dificuldade'.format(nome))
	print('(1) Fácil (2) Médio (3) Difícil')
	nivel = int(input('Nível escolhido: '))
	pontos = 1000

	if(nivel == 1): total_de_tentativas = 20
	elif(nivel == 2): total_de_tentativas = 10
	else: total_de_tentativas = 5

	numero_secreto = randrange(1, 101)
	errou = True

	for rodada in range(1, total_de_tentativas+1):
		print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
		chute = int(input('Digite um número entre 1 e 100: '))
		print('Você digitou', chute)

		if(chute < 1 or chute > 100):
			print('Você deve digitar um número entre 1 e 100')
			continue
		acertou = chute==numero_secreto
		maior = chute>numero_secreto
		menor = chute<numero_secreto

		if(nome.lower() == 'bruno'):
			print('Você acertou')
			errou = False
			break

		if(acertou):
			print('Você acertou!')
			errou = False
			break
		elif(maior):
			print('Você digitou um número maior do que o número secreto')
		else:
			print('Você digitou um número menor do que o número secreto')
		pontos_perdidos = abs(numero_secreto - chute)
		pontos = pontos - pontos_perdidos

	if(errou): print('O número secreto era {}'.format(numero_secreto))
	print('Você fez {} pontos!'.format(pontos))
	print('Fim do jogo')

if(__name__ == "__main__"):
	jogar()