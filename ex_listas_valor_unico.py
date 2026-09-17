lista = list()

while True:
    numero = int(input('Digite um numero: '))

    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')

    sair = ' '
    while sair not in ('S','N'):
        sair = str(input('Quer continuar? [S/N] ')).strip().upper()[:1]
    if sair == 'N':
        break

lista.sort()
print('-' * 30)
print(f'Você digitou os valores: {", ".join(str(v) for v in lista)}')