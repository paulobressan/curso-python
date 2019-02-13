import os

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

    arquivo = open(f'{os.getcwd()}/Python 3 parte 2: Avançando na linguagem/palavras.txt', 'r')
    #iniciar um array com os valores do arquivo e usar o strip para remover espaços e caracter como /n no inicio e no final
    palavras = [linha.strip() for linha in arquivo]
    arquivo.close()
    print(palavras)

    palavra_secreta = 'banana'.upper()
    # Criando uma lista
    letras_acertadas = ['_' for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    # enquanto não enforcou e não acertou
    while not enforcou and not acertou:
        # o str.lower converter a palavra para minuscula e o strip remove os espaço da frente e do final de uma palavra
        chute = input('Qual letra? ').strip().upper()
        print(chute)
        index = 0
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra.upper():
                    letras_acertadas[index] = letra
                    
                index += 1
        else:
            erros += 1
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
    
    if acertou:
        print('Você ganhou')
    else:
        print('Você perdeu')
    print('FIM DE JOGO!')


if __name__ == '__main__':
    jogar()
