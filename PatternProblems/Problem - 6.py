
# 12345
# 1234
# 123
# 12
# 1
def pattern6(n):

    row = n
    while row > 0:
        col = 1
        while col <= row:
            print(col, end="")
            col += 1
        print()
        row -= 1
    k = n
    for i in range(n):
        for j in range(1, k + 1):
            print(j, end="")
        k -= 1
        print()
pattern6(5)
