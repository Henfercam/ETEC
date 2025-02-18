n1 = int(input('numero'))
n2 = int(input('numero'))
n3 = int(input('numero'))
n4 = int(input('numero'))
lista: list[int] = [n1 + n2 + n3 + n4]
d: float = lista/len(lista)
if d >= 6:
    print(f'parabens sua média é {d}')
else:
    print(f'burro, sua média é {d}, melhore')
