prova = ('João', (8.5, 7.0), 'Maria', (9.0, 9.5),
         'Alisson', (9.0, 8.0), 'José', (10, 10),
         'Davi', (7.0, 9.9), 'Carlos', (9.0, 8.7))
print('--- BOLETIM DA TURMA ---')
for pos in range(0, len(prova), 2):
    aluno = prova[pos] #
    notas = prova[pos + 1]
    media = (notas[0] + notas[1]) / 2

    if media >= 9.0:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'

    print(f'Aluno: {aluno} | Notas: {notas} | Média: {media:.1f} | Status: {situacao}')
