from random import choice

def jogar():
	print('***********************************')
	print('****Bem-vindo ao jogo da Forca!****')
	print('***********************************')

	palavras = []

	with open('palavras.txt') as arquivo:
		for linha in arquivo:
			palavras.append(linha.strip())

	palavra_secreta = choice(palavras)
	letras_acertadas = ["_" for letra in palavra_secreta]
	acertou = False
	enforcou = False
	erros = 0
	print('Palavra: ' + ' '.join(letras_acertadas))

	while(not acertou and not enforcou):
		chute = input('Qual letra? ');
		chute = chute.strip();

		if chute in palavra_secreta:
			index = 0
			for letra in palavra_secreta:
				if(chute.upper() == letra.upper()):
					letras_acertadas[index] = letra
				index = index + 1
		else:
			erros += 1
		print('Palavra: ' + ''.join(letras_acertadas))

		enforcou = erros == 6
		acertou = '_' not in letras_acertadas
	if acertou:
		print('Você ganhou!!!!')
	else:
		print('Você perdeu!!!!')
		

	print('Fim do jogo')


if(__name__ == '__main__'):
	jogar()
