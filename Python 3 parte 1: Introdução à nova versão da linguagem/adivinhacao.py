print('*********************************')
print('BEM VINDO NO JOGO DE ADIVINHAÇÃO!')
print('*********************************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas:
    #f-string, abreviação de format
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    #String interpolation sem abreviação
    # a, b = 1, 2
    # print('{} teste {}'.format(a,b))
    chute_str = input('Digite o seu numero: ')

    print('Você digiotu ', chute_str)

    chute = int(chute_str)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Você acertou!')
    else:
        if maior:
            print('Você errou! O seu chute foi maior do que o numero secreto.')
        elif menor:
            print('Você errou! O seu chute foi menor do que o numero secreto.')

    rodada += 1

print('Fim de jogo')
