"""
*********
 ******* 
  *****  
   ***   
    *  

"""

def pattern8(n):
    for i in range(n):
        for space in range(i):
            print(" ", end="")
        for star in range(2 * (n - i) - 1):
            print("*", end="")
        for space in range(i):
            print(" ", end="")
        print()

    row = 0
    while row < n:
        space = 0
        while space < row:
            print(" ", end="")
            space += 1
        star = 0
        while star < 2 * (n - row) - 1:
            print("*", end="")
            star += 1
        space = 0
        while space < row:
            print(" ", end="")
            space += 1
        print()
        row += 1

pattern8(5)
