p = 'thallys'

index = 0
p2 = ''

while index < len(p):
    if index % 2:
        p2 += p[index]
    index = index + 1
print(f'As letras pares são:  {p2}')