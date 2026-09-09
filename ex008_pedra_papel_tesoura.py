from random import choice
from time import sleep
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opcoes = ('Pedra', 'Papel', 'Tesoura')
jogador_num = int(input('Qual é a sua jogada? '))
jogador = opcoes[jogador_num]
computador = choice(opcoes)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print(f'Computador jogou {computador}.')
print(f'Jogador jogou {jogador}.')
print('-=' * 11)
if computador == jogador:
    print('EMPATE!')
elif (computador == 'Pedra' and jogador == 'Papel') or \
     (computador == 'Papel' and jogador == 'Tesoura') or \
     (computador == 'Tesoura' and jogador == 'Pedra'):
    print('O jogador VENCEU!')
else:
    print('Computador VENCEU!')