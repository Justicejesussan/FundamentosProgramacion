"""
programa 2
   crear un programa
   de un rectangulo
Entradas:
   base: integer
   altura: integr
salidas:
   area: integer
   perimetro: integer
"""
base = input('Ingresa la base: ')

base = int(base)

altura = input('Ingresa la altura: ')

altura = int(altura)

area = base * altura

perimetro = (base + altura) * 2

print("El area del restangulo es", area)

print("El perimetro del rectangulo es", perimetro)