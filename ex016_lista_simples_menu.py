from time import sleep
cliente = list()
while True:
    print('\n\033[1;33m=== SISTEMA DE ATENDIMENTO BANCÁRIO ===')

    print("""[ 1 ] Adicionar cliente à fila
[ 2 ] Chamar próximo cliente
[ 3 ] Mostrar fila atual
[ 4 ] Sair do programa""")

    print('\033[1;33m-\033[m'*40)
    op = str(input('\033[1mEscolha uma opção: '))

    if op == '1':
        fila = str(input('Digite o nome do cliente: '))
        cliente.append(fila)
        print(f"> '{fila}' entrou na fila com sucesso!")

    elif op == '2':
        print(f'> Chamando para atendimento: {cliente[0]}! (Removido(a) da fila)')
        cliente.pop(0)

    elif op == '3':
        print(f'Fila atual: {" -> ".join(f"[{pos+1}º] {lista}" for pos, lista in enumerate(cliente))}')

    elif op == '4':
        print('> Encerrando o sistema. Até logo!')
        break

    else:
        print('Opção invalida! Tente novamente.')
        sleep(1)
