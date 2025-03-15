def pattern21(n):
    k = 1
    for i in range(n):
        if i == 0 or i == n - 1:
            for fline in range(n):
                print("*", end="")
            print()
        else:
            for l in range(k):
                print("*", end="")
            for s in range(n -2):
                print(" ", end="")
            for r in range(k):
                print("*", end="")
            print()

pattern21(7)
