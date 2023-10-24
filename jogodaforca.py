import random

#Início das variáveis
palavra = ['futebol', 'girafa', 'brasil']
palavra = random.choice(palavra)
tentativas = 0
chances = 5
letras_escolhidas = []
estado_atual = ['_'] * len(palavra)
#Fim das variáveis

#Tela de Início
print('\nSeja bem vindo ao Jogo da Forca!')
print('Aqui você terá que acertar a palavra secreta!')
print(f'É necessário acertar uma letra por vez. Você tem {chances} tentativas.')
print('Que o jogo comece...Boa sorte!\n')
#Fim da tela de início

#Início do jogo
while tentativas < chances and ''.join(estado_atual) != palavra:
    letra = str(input('\nQual letra você quer tentar? ',))
    
    while letra in letras_escolhidas:
        print('\nVocê já escolheu esta letra, escolha outra.\n')
        letra = str(input('\nEscolha outra letra '))

    if letra in palavra: 
        print('\nParabéns, você acertou a letra!\n')
        for i in range(len(palavra)):
            if letra == palavra[i]:
                estado_atual [i] = letra
    else:
        tentativas +=1
        print('\nVocê errou :(')
        print(f'\nNúmero de tentativas restantes: {chances - tentativas}\n')
    
    print('Esse é o estado atual da palavra:')
    print(estado_atual)

    letras_escolhidas.append(letra)
    
    for i in letras_escolhidas:
        print(f'\nLetras tentadas: {i}')

#Fim do Jogo
if tentativas == chances:
    print('\nVocê foi enforcado!')
    print(f'\nA palavra era {palavra}.')
else:
    print('Parabéns, você descobriu a palavra e se salvou de ser enforcado!')


        

