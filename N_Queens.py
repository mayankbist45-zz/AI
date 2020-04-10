print("N QUEENS PROBLEM")
print("The printing of state space graph makes the output messy. So, we are printing the state space as a line graph")
print("The program uses recursion and backtracking to solve the problem")
print("The time complexity of the program is exponential\n\n")

print("Enter the value of n for which you want to solve N queens:", end='')
n = int(input())

print("Do you want to print the state space for the problem (Y/N):", end='')
s = input()

flag = False
if (s[0] == 'Y') or (s[0] == 'y'):
    flag = True

mat = [['.' for i in range(n)] for j in range(n)]


# [a, b] -> checks whether a, b is a valid point to put a queen
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
    # Reach the base case only when we find a sol
    if pos == n:
        print("Found a solution")
        for i in range(0, n):
            for j in range(0, n):
                print(mat[i][j], end=" ")
            print()
        print("---------------------------------------------------------\n")
        return 1
    pl = False

    ans = 0
    # [pos, i] -> put a queen there
    for i in range(0, n):
        if (not ((1 << i) & mask)) and valid(pos, i):
            if flag:
                for ii in range(0, n):
                    for jj in range(0, n):
                        print(mat[ii][jj], end=" ")
                    print("")
                print()
            pl = True
            mat[pos][i] = 'Q'
            ans += solve(pos + 1, mask | (1 << i))
            # Backtracking part
            mat[pos][i] = '.'
    if not pl and flag:
        print('The state can have no solution')
        print("---------------------------------------------------------\n")
    return ans


print("No of solution found :", solve(0, 0))

