print('\033[1;36m-' * 30)
print(f'{'Loja ALIMCAPIM':^30}')
print('\033[1;36m-\033[m' * 30)
totalcompra = tot1000 = contbarato = menorpreco = barato = 0
while True:
    produto = str(input('\033[1;36mPRODUTO:\033[m '))
    preco = float(input('\033[1;36mPREÇO: R$\033[m '))
    totalcompra += preco
    contbarato += 1
    if preco > 1000:
        tot1000 += 1
    if contbarato == 1 or preco < menorpreco:
        menorpreco = preco
        barato = produto
    sair = ' '
    while sair not in 'SN':
        sair = str(input('\033[1;31mQuer continuar? [S/N]\033[m ')).strip().upper()[0]
    if sair in 'N':
        break
print('\033[1;36m-' * 30)
print(f'{'COMPRA FINALIZADA':^30}')
print('-' * 30)
print(f'TOTAL DA COMPRA: R$ {totalcompra:.2f}')
print(f'Ao todo, {tot1000} produto passou de R$ 1000.00')
print(f'\033[1;36mO produto mais barato foi o {barato}, que custa R$ {menorpreco:.2f}\033[m')