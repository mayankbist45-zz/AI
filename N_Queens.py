print("Enter the value of n for which you want to solve N queens:")
n = int(input())

mat = [['_' for i in range(n)] for j in range(n)]


def valid(a, b):
    ta = a - 1
    tb = b - 1
    while ta >= 0 and tb >= 0:
        if mat[ta][tb] == 'Q':
            return False
        ta -= 1
        tb -= 1
    ta = a - 1
    tb = b + 1

    while ta >= 0 and tb < n:
        if mat[ta][tb] == 'Q':
            return False
        ta -= 1
        tb += 1
    return True


def solve(pos, mask):
    if pos == n:
        print("Found a solution")
        for i in range(0, n):
            for j in range(0, n):
                print(mat[i][j], end=" ")
            print()
        return

    for i in range(0, n):
        if (not ((1 << i) & mask)) and valid(pos, i):
            mat[pos][i] = 'Q'
            solve(pos + 1, mask | (1 << i))
            mat[pos][i] = '_'
    return


solve(0, 0)
