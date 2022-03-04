def transpose(matr):
    res=[]
    n = len(matr)
    m = len(matr[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [matr[i][j]]
        res = res + [tmp]
    return res


matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in transpose(matrix):
    print(*line)