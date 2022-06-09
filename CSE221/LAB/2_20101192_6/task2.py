def LCS(X, Y, Z):
    f2 = open("output2.txt", "w")
    m = len(X) + 1
    n = len(Y) + 1
    o = len(Z) + 1

    c = [0] * m
    for i in range(0, len(c)):
        c[i] = [0] * n
        for j in range(0, len(c[i])):
            c[i][j] = [0] * o

    d = [None] * m
    for i in range(0, len(d)):
        d[i] = [None] * n
        for j in range(0, len(d[i])):
            d[i][j] = [None] * o

    for i in range(1, m):
        for j in range(1, n):
            for k in range(1, o):
                if X[i - 1] == Y[j - 1] and X[i - 1] == Z[k - 1]:
                    c[i][j][k] = 1 + c[i - 1][j - 1][k - 1]
                    d[i][j][k] = "diagonal"
                elif c[i - 1][j][k] >= c[i][j - 1][k]:
                    max = c[i - 1][j][k]
                    if max >= c[i][j][k - 1]:
                        c[i][j][k] = max
                        d[i][j][k] = "up-up-left"
                    else:
                        max = c[i][j][k - 1]
                        c[i][j][k] = max
                        d[i][j][k] = "left-up-up"
                else:
                    max = c[i][j - 1][k]
                    if max >= c[i][j][k - 1]:
                        c[i][j][k] = max
                        d[i][j][k] = "up-left-up"
                    else:
                        max = c[i][j][k - 1]
                        c[i][j][k] = max
                        d[i][j][k] = "left-up-up"
    f2.write(str(c[m - 1][n - 1][o - 1]))
    f2.close()


f = open("input2.txt", "r")
X = f.readline().rstrip()
Y = f.readline().rstrip()
Z = f.readline().rstrip()

LCS(X, Y, Z)
