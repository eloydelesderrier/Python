a = input().split()
v1 = float(a[0])
v2 = float(a[1])
v3 = float(a[2])
pi = 3.14159

TRIANGULO = (v1 * v3) / 2
CIRCULO = pi * (v3 ** 2)
TRAPEZIO = ((v1 + v2) * v3) / 2
QUADRADO = v2 * v2
RETANGULO = v1 * v2

print('TRIANGULO: {:.3f}'.format(TRIANGULO))
print('CIRCULO: {:.3f}' .format(CIRCULO))
print('TRAPEZIO: {:.3f}'.format(TRAPEZIO))
print('QUADRADO: {:.3f}'.format(QUADRADO))
print('RETANGULO: {:.3f}' .format(RETANGULO))