"""
  *
 ***
*****
"""
def pattern7(n):
    for i in range(n):
        for space in range(i, n - 1):
            print(" ", end="")
        for star in range(2 * i + 1):
            print("*", end="")
        for space in range(i, n - 1):
            print(" ", end="")
        print()
    row = n
    star_val = 0
    while row > 0:
        space = 0
        while space < row - 1:
            print(" ", end="")
            space += 1
        star = 0
        while star < 2 * star_val + 1:
            print("*", end="")
            star += 1
        space = 0
        while space < row - 1:
            print(" ", end="")
            space += 1
        row -= 1
        star_val += 1
        print()
pattern7(3)
