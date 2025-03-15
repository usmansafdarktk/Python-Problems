"""
A
BB
CCC
DDDD
EEEEE
"""

def pattern16(n):
    char = "A"
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(char, end="")
        char = chr((ord(char)) + 1)
        print()

pattern16(5)


