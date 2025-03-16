def primeorNot(n):
    i = 1
    count = 0
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            print(i, end=" ")
            count += 1
            temp = n // i
            if n % temp == 0 and temp != i:
                print(temp, end=" ")
                count += 1
        i += 1
    print()
    if (count == 2):
        print(f"{n} is Prime")
        return True
    else:
        print(f"{n} is not Prime")
        return False


n = int(input("Enter your No: "))
primeorNot(n)
