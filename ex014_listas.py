pilha = []

expr = str(input('Digite a expressão: '))

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if pilha: #verifica se a lista está vazia ou não
            pilha.pop()
        else:
            pilha.append(')')
            # Se digitar ')' logo no começo do programa,
            # ele adiciona ')' na lista e logo em seguida fecha o programa.
            break

if len(pilha) == 0:# se tiver vazia, vai ser válido, se não, vai ser invalido
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

