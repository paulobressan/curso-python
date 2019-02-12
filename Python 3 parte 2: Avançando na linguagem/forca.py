def jogar():
    print('*********************************')
    print('***BEM VINDO NO JOGO DE FORCA!***')
    print('*********************************')

    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    enforcou = False
    acertou = False

    # enquanto não enforcou e não acertou
    while not enforcou and not acertou:
        # o str.lower converter a palavra para minuscula e o strip remove os espaço da frente e do final de uma palavra
        chute = input('Qual letra? ').strip().lower()
        print(chute)
        index = 0
        for letra in palavra_secreta:
            if chute == letra.lower():
                letras_acertadas[index] = letra
                print(f'Encontrei a letra {chute} na posição {index}')
            index += 1
        print(letras_acertadas)
    print('FIM DE JOGO!')


if __name__ == '__main__':
    jogar()
