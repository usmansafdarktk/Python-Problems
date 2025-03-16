def GCD(m, n):
    
    while m > 0 and n > 0:
        if m > n:
            m = m % n
        else:
            n = n % m
    
    if m == 0: return n
    return m
    

n = int(input("Enter your No: "))
m = int(input("Enter your No: "))

print(GCD(m, n))
