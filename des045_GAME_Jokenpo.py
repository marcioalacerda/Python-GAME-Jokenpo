''' Programa que faz o computador jogar "Jokenpô" com você.'''
from random import choice
from time import sleep # faz o computador esperar em segundos
from termcolor import colored # para dar cor no seu
lista = ['PEDRA', 'PAPEL', 'TESOURA']

computador = choice(lista) # faz o computador "PENSAR"
#print(computador)
print(colored('-=-', 'yellow') * 20)
print('  Vamos jogar Jokenpô. Tente acertar...')
print(colored('-=-', 'yellow') * 20)
jogador = str(input('Escolha Pedra, Papel ou Tesoura: ')).upper() # jogador tenta adivinhar
#print(jogador)
print(colored('PROCESSANDO...', 'magenta'))
sleep(3)
if (jogador == 'PAPEL' and computador == 'PEDRA') or (jogador == 'PEDRA' and computador == 'TESOURA') or (jogador == 'TESOURA' and computador == 'PAPEL'):
    print(colored('PARABÉNS! Você conseguiu me vencer!', 'green'))
    print(colored('Você jogou {} e eu joguei {}', 'yellow').format(jogador, computador))
elif(computador == 'PAPEL' and jogador == 'PEDRA') or (computador == 'PEDRA' and jogador == 'TESOURA') or (computador == 'TESOURA' and jogador == 'PAPEL'):
    print(colored('GANHEI! Eu joguei {} e você jogou {}', 'red').format(computador, jogador))
