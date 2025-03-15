
"""
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 

"""

def pattern22(n):
    i = 0
    while i < 2 * n - 1:
        j = 0
        while j < 2 * n - 1:
            top = i
            left = j
            right = 2 * n - 2 - j
            bottom = 2 * n - 2 - i
            print(n - min(min(top, left), min(right, bottom)), end="")
            print(" ", end="")
            j += 1
        print()
        i += 1

pattern22(4)
