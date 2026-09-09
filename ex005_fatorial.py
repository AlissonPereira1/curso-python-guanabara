n = int(input('Quer saber o fatorial de qual número ? '))
c = n
r = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    r *= c
    c -= 1
print(f'{r}')