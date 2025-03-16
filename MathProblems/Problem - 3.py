def checkPalindrome(n):
    newNum = 0
    temp = n
    num = n
    while temp > 0:
        n = temp % 10
        newNum = 10 * newNum + n
        print(newNum)
        temp = temp // 10
    if num == newNum:
        print(f"{num} is a Palindrome")
        return True
    else:
        print(f"{num} is not a Palindrome")
        return False

checkPalindrome(444)
