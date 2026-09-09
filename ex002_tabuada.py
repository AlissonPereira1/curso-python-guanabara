while True:
    print('\033[1;33m-' * 30)
    print(f'{'TABUADA':^30}')
    print('\033[1;33m-\033[m' * 30)
    t = int(input('Quer ver qual tabuada [Digite um número negativo para parar]: '))
    if t < 0:
        break
    print('\033[1;33m-'*30)
    for c in range(1, 11):
        resultado = t * c
        if resultado % 2 == 0:
            print(f'{t} x {c} = {resultado} (PAR)')
        else:
            print(f'{t} x {c} = {resultado} (ÍMPAR)')
print('\033[1;31mPROGRAMA TABUADA ENCERRADO. Volte sempre!\033[m')