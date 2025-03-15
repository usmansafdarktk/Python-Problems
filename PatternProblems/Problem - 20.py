"""
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

"""

def pattern20(n):
    k = n - 1
    m = 1
    for i in range(1, 2 * n):
        if i < n + 1:
            for l in range(0, i):
                print("*", end="")
            for s in range(2 * n - (2 * i)):
                print(" ", end="")
            for r in range(0 , i):
                print("*", end="")
            print()
        else:
            for l in range(k):
                print("*", end="")
            for s in range(2 * m):
                print(" ", end="")
            for r in range(k):
                print("*", end="")
            print()
            k -= 1
            m += 1

pattern20(5)
