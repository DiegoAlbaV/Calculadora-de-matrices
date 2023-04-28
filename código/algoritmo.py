def gaussJ(a, m, n, arreglo):
    j = 0 
    i = 0
    z = 0
    p = [0 for x in range(n)]
    while j < n:
        i=0
        while i < m:
            if a[i][j] != 0 :
                for q in range(n):
                    p[q] = a[i][q]
                    a[i][q] = a[z][q]
                    a[z][q] = p[q]
                d = a[z][j]
                for q in range(n):
                    a[z][q] /= d
                if i != m-1 :
                    for h in range(i+1, m):
                        g = a[h][j];
                        for r in range(n):
                            a[h][r] = a[h][r] - (a[z][r] * g)
                if z != 0 :
                    for t in range(z):
                        s = a[t][j];
                        for w in range(n):
                            a[t][w] = a[t][w] - (a[z][w] * s)
                z += 1
                i = z-1
                j = j+1
            i += 1
        j += 1
    return a, arreglo