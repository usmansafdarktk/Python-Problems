def pattern13(n):
    count = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(count, end="")
            print(" ", end="")
            count += 1
        print()


pattern13(5)

