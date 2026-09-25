boletim = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    boletim.append([nome, [nota1, nota2]])

    sair = ' '
    while sair not in ('S', 'N'):
        sair = str(input('Quer continuar? [S/N] ')).strip().upper()[:1]
    if sair == 'N':
        break

print('-=' * 15)
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":>6}')
print('-=' * 15)

# Usamos o enumerate para pegar a posição e o aluno de uma vez
for pos, (nome, notas) in enumerate(boletim):
    media = sum(notas) / len(notas)
    print(f'{pos:<4}{nome:<15}{media:>6.2f}')

print('-=' * 15)

while True:
    aluno = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    if aluno == 999:
        print('<<< FINALIZANDO >>> Volte sempre!')
        break

    if aluno <= len(boletim) - 1:
        # Desempacotamos direto da lista do aluno escolhido
        nome, notas = boletim[aluno]
        print(f'Notas de {nome} são {notas}')
    else:
        print('Aluno inválido! Tente novamente.')
    print('-=' * 15)

