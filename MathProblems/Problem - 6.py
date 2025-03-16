import math

def divisordigits(n):
    i = 1
    temp = n
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            print(i, end=" ")
            temp = n // i
            if n % temp == 0 and temp != i:
                print(temp)
        i += 1
    print()
    return


n = int(input("Enter your No: "))
divisordigits(n)
