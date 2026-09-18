# ==============================================================================
# PROJETO: Lista Ordenada de Valores Únicos (Sem repetição e em tempo real)
# DESCRICAO: Script que gerencia uma lista numérica garantindo valores únicos
#            e mantendo os elementos ordenados em ordem crescente a cada inserção.
# ==============================================================================

num = list()

while True:
    # 1. Entrada de dados do usuário convertida para inteiro
    valor = int(input('Digite um valor: '))

    # 2. Controle de duplicidade: barra imediatamente números que já existem na lista
    if valor not in num:
        # 3. Lógica de inserção ordenada em tempo real (sem usar .sort() ao final)
        # enumerate(num) percorre a lista capturando índice (pos) e valor (n)
        for pos, n in enumerate(num):
            if valor <= n:
                num.insert(pos, valor)
                print(f'Número adicionado na posição {pos} da lista...!')
                break
        else:
            # O for-else roda se o loop terminar sem dar break (número é o maior de todos)
            num.append(valor)
            # len(num) - 1 calcula dinamicamente a posição exata do último elemento (índice 0-based)
            print(f'Número adicionado no final da lista (posição {len(num) - 1})...')
    else:
        print('Número duplicado, não será adicionado!')

    # 4. Validação blindada de continuação (evita erros com strings vazias ou letras erradas)
    sair = ' '
    while sair not in ('S', 'N'):
        sair = str(input('Quer continuar? [S/N] ')).strip().upper()[:1]

    if sair == 'N':
        break

# 5. Apresentação final estilizada
# \033[1;34m aplica formatação ANSI (azul brilhante e negrito) no terminal
print('\033[1;34m-' * 30)
# .join() une os elementos da lista formatados como string de forma limpa e profissional
print(f'Números digitados: {", ".join(str(v) for v in num)}')