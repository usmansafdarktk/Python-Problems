"""
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

"""

def pattern19(n):
    k = n
    for i in range(n):
        for l in range(k):
            print("*", end="")
        for s in range(2 * i):
            print(" ", end="")
        for r in range(k):
            print("*", end="")
        print()
        k -= 1
    k = 1
    f = 2 * n - 2
    for i in range(n):
        for l in range(k):
            print("*", end="")
        for s in range(f):
            print(" ", end="")
        for r in range(k):
            print("*", end="")
        print()
        k += 1
        f -= 2

pattern19(5)
