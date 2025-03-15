"""
1     1
12   21
123 321
12344321
"""

def pattern12(n):
    space_count = (2 * n - 1)
    for i in range(1, n + 1):
        for num in range(1, i + 1):
            print(num, end="")
        for space in range(1, space_count):
            print(" ", end="")
        space_count -=2
        for num in range(i, 0, -1):
            print(num, end="")
        print()
    print()

pattern12(4)
