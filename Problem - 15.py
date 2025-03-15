"""
ABCDE
ABCD
ABC
AB
A
"""

def pattern15(n):
    for i in range(1, n + 1):
        char = "A"
        for j in range(i, n + 1):
            print(char, end="")
            char = chr((ord(char)) + 1)
        print()

pattern15(5)
