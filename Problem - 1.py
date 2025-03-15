# *****
# *****
# *****
# *****
# *****
def pattern1(n):
    for row in range(n):
        for col in range(n):
            print("*", end="")
        print()
    row = 0
    while row < n:
        col = 0
        while col < n:
            print("*", end="")
            col += 1
        print()
        row += 1
pattern1(5)
