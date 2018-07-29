print('*********************************')
print('Bem vindo ao Jogo de Adivinhação!')
print('*********************************')

numero_secreto = 42
total_de_tentativas = 3

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

	if(acertou):
		print('Você acertou!')
		break
	elif(maior):
		print('Você digitou um número maior do que o número secreto')
	else:
		print('Você digitou um número menor do que o número secreto')

print('Fim do jogo')