from random import shuffle
x = 55
x1 = 55
x2 = 55
n1 = 0
jogador1 = input('Digite o nome do primeiro jogador: ')
jogador2 = input('Digite o nome do segundo jogador: ')
jogadores = [jogador1, jogador2]
shuffle(jogadores)
n = 0
while x != 0 or x1 != 0 or x2 != 0:
    o = 4
    p = 56
    m = jogadores[n]
    if n1 == 0:
        print('O jogador que começa é {}'.format(m))
        n1 = 1
    else:
        print('O próximo a jogar é {}'.format(m))
    print('{}, escolha a pilha e o número de peças a serem tiradas'.format(m))
    while o > 3 or p > 55:
        o = int(input('Pilha: '))
        p = int(input('Nº de peças: '))
        if o > 3 or p > 55:
            print('Número inválido! Digite um valor correto')
            print('')
    if o == 1:
        x = x - p
    if o == 2:
        x1 = x1 - p
    if o == 3:
        x2 = x2 - p
    print('{} escolheu a pilha {} e tirou {} peças'.format(m, o, p))
    print('Restam {} peças na pilha 1, {} peças na pilha 2 e {} na pilha 3'.format(x, x1, x2))
    print('')
    if x <= 0 and x1 <= 0 and x2 <= 0:
        print('Parabéns {}! Você ganhou o jogo'.format(m))
    if n == 0:
        n = 1
    else:
        n = 0
