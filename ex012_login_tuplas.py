usuarios = (
    ('joao', '1234', 'admin'),
    ('maria', 'abcd', 'comum'),
    ('carlos', 'senha1', 'comum')
)

print('-'*30)
print(f"{'LOGIN':^30}")
print('-'*30)

login = str(input('Login: '))
senha = str(input('Senha: '))
encontrou = False

for pos in range(0, len(usuarios)):
    usuario = usuarios[pos]

    if login == usuario[0] and senha == usuario[1]:
        if usuario[2] == 'admin':
            print('Acesso total liberado para Administrador')
        else:
            print('Acesso restrito para Comum')

        encontrou = True
        break

if not encontrou:
    print('Acesso negado!')

