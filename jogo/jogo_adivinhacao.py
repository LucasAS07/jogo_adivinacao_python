import random


def jogar_adivinhacao():

    print('********************************')
    print('BEM VINDO AO JOGO DE ADIVINHAÇÃO')
    print('********************************')

    numero_secreto = random.randrange(1, 101)
    numero_tentativas = 5
    pontos = 1000

    print('Qual nivel de dificudade? ')
    print('1- Facil 2- Medio 3- Dificil ')

    nivel = int(input('Defina o nivel: '))

    if(nivel == 1):
        numero_tentativas = 20
    elif(nivel == 2):
        numero_tentativas = 10
    else:
        numero_tentativas = 5

    for rodada in range(1, numero_tentativas + 1):
        print(f'Tentativa {numero_tentativas} de 5!')
        chute_str = input("Digite o seu numero entre 1 e 100: ")
        print('Você digitou: ', chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print('Você digitou um numero invalido!')
            continue

        if(numero_secreto == chute):
            print(f'Você acertou! e fez {pontos} pontos!')
            break
        else:
            if(chute > numero_secreto):
                print('Você errou chutou para cima do numero!')
            elif(chute < numero_secreto):
                print('Você errou chutou para baixo do numero! ')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        numero_tentativas = numero_tentativas - 1

    print('Fim de Jogo!')


if(__name__ == '__main__'):
    jogar_adivinhacao()
