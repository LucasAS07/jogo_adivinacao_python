def jogar_forca():
    print('********************************')
    print('BEM VINDO AO JOGO DE FORCA')
    print('********************************')

    palavra_secreta = 'banana'
    enforcou = False
    acertou = False
    while(not enforcou and not acertou):
        chute = input('Digite uma letra: ')
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(f'Encontrei a {letra} na posição {index}!')
            index = index + 1
        print('...')

    print('Fim de Jogo!')


if(__name__ == '__main__'):
    jogar_forca()
