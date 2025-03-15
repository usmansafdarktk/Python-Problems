
"""
E 
D E 
C D E 
B C D E 
A B C D E

"""
def pattern18(n):
    chara = "E"
    for i in range(n):
        for j in range(i + 1):
            print(chr(ord(chara) - i + j), end="")
            print(" ", end="")
        print()

pattern18(5)



