# 1
# 22
# 333
# 4444
# 55555
def pattern4(n):
    for row in range(1, n + 1):
        for j in range(1, row + 1):
            print(row, end="")
        print()
    row = 1
    while row <= n:
        col = 0
        while col < row:
            print(row, end="")
            col += 1
        print()
        row += 1
pattern4(5)
