def countdigits(n):
    temp = n
    count = 0
    while temp > 0:
        n = temp % 10
        temp = temp // 10
        print(n, end = " ")
        count += 1
    print()
    print(f"The count of digits is {count}")
    return

countdigits(123457)
