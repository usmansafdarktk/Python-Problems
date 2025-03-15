"""
"Notes to myself"

char_A = 'A'
ascii_value = ord(char_A)
print(ascii_value)
char_b = chr(ord(char_A) + 1)
print(char_b)

"""

def pattern14(n):
    for i in range(1, n + 1):
        char = "A"
        for j in range(1, i + 1):
            print(char, end="")
            char = chr((ord(char)) + 1)
        print()

pattern14(5)
