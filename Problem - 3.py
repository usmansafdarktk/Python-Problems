def pattern3(n):
    row = 1
    while row <= n:
        col = 1
        while col <= row:
            print(col, end="")
            col += 1
        print()
        row += 1
    for row in range(n):
        for col in range(row + 1):
            print(col + 1, end="")
        print()
pattern3(5)
