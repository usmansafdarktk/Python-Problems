def reverse_num(num):
    n = 0
    count = 0
    newNum = 0
    while num > 0:
        n = num % 10
        newNum = n + 10 * newNum
        count += 1
        num = num // 10
        return newNum
 
 
print(reverse_num(123))
