def gaussJ(a, m, n):
    j = 0 
    i = 0
    z = 0
    p = [0, 0, 0]
    while j < n:
        i=0
        while i < m:
            if a[i][j] != 0 :
                for q in range(n):
                    p[q] = a[i][q]
                    a[i][q] = a[z][q]
                    a[z][q] = p[q]
                for q in range(n):
                    a[z][q] /= a[z][j]
                if i != m-1 :
                    for h in range(i+1, m):
                        for r in range(n):
                            a[h][r] = a[h][r] + (a[z][r] * -a[h][j])
                if z != 0 :
                    for t in range(z):
                        for w in range(n):
                            a[t][w] = a[t][w] + (a[z][w] * -a[t][j])
                z += 1
                i = z-1
                j = j+1
            i += 1
        j += 1
    return a