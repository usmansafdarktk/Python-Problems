"""
*
**
***
****
*****
****
***
**
*
"""

def pattern10(n):
    count = n
    for i in range(2 * n - 1):
        if i < n:
            for j in range(i + 1):
                print("*", end="")
            print()
        else:
            for k in range(count - 1):
                print("*", end="")
            count -= 1
            print()

    r = 1
    while r <= 2 * n - 1:
        c = 0
        if r <= n:
            while c < r:
                print("*", end="")
                c += 1
            print()
            r += 1
        else:
            star = 0
            while  star < 2 * n - r:
                print("*", end="")
                star += 1
            print()
            r += 1

pattern10(5)
