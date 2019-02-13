import os
import random


def jogar():
    imprime_mensagem_abertura()
    # COLEÇÕES
    # tuple('São Paulo','Rio de Janeiro') , tuple é uma coleção imutavel
    # ['Paulo', 'Bruna'] , list é uma coleção mutavel
    # {'Paulo':'Homem', 'Bruna': 'Mulher'} , dictionary é uma coleção mutavel e boa para atender o problema 
    # que a list não resolve quando tenta busca um item de uma lista dentro de outra lista,
    # exemplo lista = [('Paulo', 'Homem'), ('Bruna', 'Mulher')], não podemos realizar lista['Paulo'], portanto com
    # o dictionary conseguimos colecao = {'Paulo':'Homem', 'Bruna': 'Mulher'}, colecao['Paulo'] resultado: 'Homem'
    # Set, o set é utilizado quando temos uma coleção de dados que não pode se repetir, o set ignora a inserção
    # de registro ja existente, portanto um set não contem indece.

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    enforcou = False
    acertou = False
    erros = 0

    # enquanto não enforcou e não acertou
    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
    
    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def imprime_mensagem_abertura():
    print('*********************************')
    print('***BEM VINDO NO JOGO DE FORCA!***')
    print('*********************************')

def carrega_palavra_secreta():
    # com with o python vai gerenciar a abertura e o fechamento do arquivo
    with open(f'{os.getcwd()}/Python 3 parte 2: Avançando na linguagem/palavras.txt', 'r') as arquivo:
        #iniciar um array com os valores do arquivo e usar o strip para remover espaços e caracter como /n no inicio e no final
        palavras = [linha.strip() for linha in arquivo]

    # pegando um elemento da lista de acordo com um numero randomico de 0 até o tamanho da lista.
    return palavras[random.randrange(0, len(palavras))].upper()

def inicializa_letras_acertadas(palavra_secreta):
    # Criando uma lista
    return ['_' for letra in palavra_secreta]

def pede_chute():
     # o str.lower converter a palavra para minuscula e o strip remove os espaço da frente e do final de uma palavra
     return input('Qual letra? ').strip().upper()

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra.upper():
            letras_acertadas[index] = letra           
        index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if __name__ == '__main__':
    jogar()
