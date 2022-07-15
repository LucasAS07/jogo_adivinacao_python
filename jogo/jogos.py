import jogo_forca as forca
import jogo_adivinhacao as adivinha


def escolha_jogo():
    print('******************************')
    print('****** ESCOLHA SEU JOGO ********')
    print('********************************')

    print('(1) FORCA (2) ADIVINHAÇÃO')

    jogo = int(input('Qual jogo? '))

    if(jogo == 1):
        print('Jogo Forca')
        forca.jogar_forca()
    elif(jogo == 2):
        print('Jogo de Adivinhação')
        adivinha.jogar_adivinhacao()


if(__name__ == '__main__'):
    escolha_jogo()
