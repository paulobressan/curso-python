def jogar():
    print('*********************************')
    print('***BEM VINDO NO JOGO DE FORCA!***')
    print('*********************************')

    # COLEÇÕES
    # tuple('São Paulo','Rio de Janeiro') , tuple é uma coleção imutavel
    # ['Paulo', 'Bruna'] , list é uma coleção mutavel
    # {'Paulo':'Homem', 'Bruna': 'Mulher'} , dictionary é uma coleção mutavel e boa para atender o problema 
    # que a list não resolve quando tenta busca um item de uma lista dentro de outra lista,
    # exemplo lista = [('Paulo', 'Homem'), ('Bruna', 'Mulher')], não podemos realizar lista['Paulo'], portanto com
    # o dictionary conseguimos colecao = {'Paulo':'Homem', 'Bruna': 'Mulher'}, colecao['Paulo'] resultado: 'Homem'
    # Set, o set é utilizado quando temos uma coleção de dados que não pode se repetir, o set ignora a inserção
    # de registro ja existente, portanto um set não contem indece.

    palavra_secreta = 'banana'
    # Criando uma lista
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
