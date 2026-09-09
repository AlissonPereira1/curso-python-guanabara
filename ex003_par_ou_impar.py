print('\033[1;35m=-'*15)
print(f'{'JOGO PAR OU ÍMPAR':^30}')
print('\033[1;35m=-\033[m'*15)
from random import randint
vitorias = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Escolha um número de 0 a 10: '))
    soma = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU ÍMPAR ? [P/I] ')).strip().upper()[0]
    print('\033[1;35m-\033[m'*30)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    print('\033[1;35m-\033[m'*30)

    if tipo == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print('\033[1;35m=-\033[m'*30)
print(f'Jogo encerrado! Você teve {vitorias} vitorias consecutivas!')
