from time import sleep
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
op = 0
while op != 5:
    print ('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    op = int(input('Escolha: '))
    if op == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma} ')
    elif op == 2:
        multi = n1 * n2
        print(f'O resultado de {n1} x {n2} é {multi} ')
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif op == 4:
        print('Informe os números novamente:')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif op == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção invalida. Tente novamente.')
    print('-' * 30)
    sleep(1)
print('Fim do programa!')
