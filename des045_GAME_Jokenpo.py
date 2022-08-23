''' Melhorando o programa, agora alem de jogar com você, o computador da as opções em numeros e jogo como se fosse outra pessoa pessoa joga "Jokenpô"'''
from time import sleep # faz o computador esperar em segundos
from termcolor import colored # para dar cor no seu
from random import randint

print(colored('-=-', 'yellow') * 15)
print('    Vamos jogar Jokenpô. Tente ganhar...')
print(colored('-=-', 'yellow') * 15)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÔES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print(colored('JO...', 'magenta'))
sleep(1)
print(colored('KEN...', 'magenta'))
sleep(1)
print(colored('PÔ!!!', 'magenta'))

print(colored('-=-', 'yellow') * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print(colored('-=-', 'yellow') * 11)

if computador == 0: #pedra
    if jogador == 0:
        print('EMPATOU!')
    elif jogador == 1:
        print(colored('PARABÉNS!!! JOGADOR VENCEU!', 'green'))
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print(colored('JOGADA INVALIDA!', 'red'))

elif computador ==1: #papel
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATOU!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print(colored('JOGADA INVALIDA!', 'red'))

elif computador ==2: #tesoura
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATOU!')
    else:
        print(colored('JOGADA INVALIDA!', 'red'))
