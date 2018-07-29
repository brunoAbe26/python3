print('*********************************')
print('Bem vindo ao Jogo de Adivinhação!')
print('*********************************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
	print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
	chute = int(input('Digite seu número: '))
	print('Você digitou', chute)
	acertou = chute==numero_secreto
	maior = chute>numero_secreto
	menor = chute<numero_secreto

	if(acertou):
		print('Você acertou!')
	elif(maior):
		print('Você digitou um número maior do que o número secreto')
	else:
		print('Você digitou um número menor do que o número secreto')

	rodada += 1

print('Fim do jogo')