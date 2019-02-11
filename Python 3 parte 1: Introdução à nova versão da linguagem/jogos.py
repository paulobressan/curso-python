import adivinhacao
import forca

print('*********************************')
print('*******ESCOLHA O SEU JOGO********')
print('*********************************')

print('(1) Forca (2) Adivinhação')
jogo = int(input('Qual jogo?'))
if jogo == 1:
    print('jogar forca')
    forca.jogar()
elif jogo == 2:
    print('jogar adivinhação')
    adivinhacao.jogar()