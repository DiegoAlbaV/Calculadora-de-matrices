from algoritmo import gaussJ
from fractions import Fraction

a = [[Fraction('0'), Fraction('0'), Fraction('0')], 
     [Fraction('0'), Fraction('0'), Fraction('0')], 
     [Fraction('0'), Fraction('0'), Fraction('1')]]
arreglo =[Fraction('0'), Fraction('1'), Fraction('2')]
m = 3
n = 3
g, ares = gaussJ(a, m, n, arreglo)

for y in ares:
    print(y )

for i in range(m):
    for j in range(n):
        print(g[i][j], end=" ")
    print(end="\n")