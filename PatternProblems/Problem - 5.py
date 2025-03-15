#
# *****
# ****
# ***
# **
# *
def pattern5(n):
    k = n
    for i in range(n):
        for j in range(k):
            print("*", end="")
        k -= 1
        print()
    row = n
    while row > 0:
        col = 0
        while col < row:
            print("*", end="")
            col += 1
        row -= 1
        print()
pattern5(5)
