
"""
    A    
   ABA   
  ABCBA  
 ABCDCBA 
ABCDEDCBA

"""

def pattern17(n):
    k = n
    for i in range(n):
        for space in range(k - 1):
            print(" ", end="")
        chara = "A"
        brpoint = i
        for char in range(2 * i + 1):
            print(chara, end="")
            if char < brpoint:
                chara = chr(ord(chara) + 1)
            else:
                chara = chr(ord(chara) - 1)
        for space in range(k-1 , 0, -1):
            print(" ", end="")
        print()
        k -= 1

pattern17(5)
