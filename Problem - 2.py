
# *
# **
# ***
# ****
# *****
def pattern2(n):
    row = 1
    while row <= n:
        col = 0
        while col != row:
            print("*", end="")
            col += 1
        print()
        row += 1

    for row in range(n):
        for col in range(row + 1):
            print("*", end="")
        print()
pattern2(5)
