def Armstrong_num(num):
    temp = num
    n = 0
    count = 0
    arm_str_num = 0
    while num > 0:
        n = num % 10
        count += 1
        num = num // 10
    num = temp
    while num > 0:
        n = num % 10
        arm_str_num = arm_str_num + (n ** count)
        num = num // 10
    print(arm_str_num)
    if arm_str_num == temp:
        return True
    else:
        return False

print(Armstrong_num(371))
