print('*********************************')
print('BEM VINDO NO JOGO DE ADIVINHAÇÃO!')
print('*********************************')
print('Escolha numeros de 1 a 100')

numero_secreto = 42
total_de_tentativas = 3

# for, vamos iniciar a rodada com 1 e ir incrementando de 1 a 1 até 3. Porem o for
# utiliza o operador < então de 1 a 3 vamos ter somente 2 rodadas e para isso vamos ir de 1 a 4,
# por isso vamos somar 1 no total_de_tentativas
for rodada in range(1, total_de_tentativas + 1):
    # f-string, abreviação de format
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    # String interpolation sem abreviação
    # a, b = 1, 2
    # print('{} teste {}'.format(a,b))
    chute_str = input('Digite o seu numero: ')
    print('Você digiotu ', chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print('Você deve digitar entre o numero 1 e 100')
        # continue quebra somente esse laço e continua, por exemplo,
        # estamo no index 1 e damos continue o for vai para a proxima rodada
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Você acertou!')
        # Se o usuário acertou, vamos sair do laço for
        break
    else:
        if maior:
            print('Você errou! O seu chute foi maior do que o numero secreto.')
        elif menor:
            print('Você errou! O seu chute foi menor do que o numero secreto.')

    rodada += 1

print('Fim de jogo')
