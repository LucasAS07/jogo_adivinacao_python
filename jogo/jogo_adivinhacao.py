import random

print('********************************')
print('BEM VINDO AO JOGO DE ADIVINHAÇÃO')
print('********************************')

numero_secreto = random.randrange(1, 101)
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
        print('Você acertou!')
        break
    else:
        if(chute > numero_secreto):
            print('Você errou chutou para cima do numero!')
        elif(chute < numero_secreto):
            print('Você errou chutou para baixo do numero! ')
    numero_tentativas = numero_tentativas - 1

print('Fim de Jogo!')
