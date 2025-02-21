a = int(input('A'))
b = int(input('B'))
c = int(input('C'))
delta = b ** 2 - 4 * a * c
rdelta = float(delta ** 0.5)
x1 = (-b - rdelta) / 2 * a
x2 = (-b + rdelta) / 2 * a
print(f'x1 é {x1} e x2 é {x2}')
