print('\033[1;35m-'*30)
print(f'{' LOJA ALIMCAPIM ':-^30}')
print('\033[1;35m-\033[m'*30)
totgasto = totmil = cont = 0
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    cont += 1
    totgasto += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menorpreco:
        menorpreco = preco
        maisbarato = produto
    encerrar = ' '
    while encerrar not in 'SN':
        encerrar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if encerrar == 'N':
        break
print(f'\033[1;35m{' FIM DO PROGRAMA ':-^30}\033[m')
print(f'O total gasto na compra foi R$ {totgasto:.2f}')
print(f'Ao todo {totmil} produtos custam mais de R$1000.00')
print(f'O produto mais barato foi {maisbarato} que custa R$ {menorpreco:.2f}')