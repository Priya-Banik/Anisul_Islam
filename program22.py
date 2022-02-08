"""
1.start
2.input guess number
3.generate random number
4.if guess  == random number
    i)yes,print won
    ii)no,print lost
5.end
"""
from random import randint

for x in range(1, 6):
     guessnumber =int(input("Enter your guess number between 1 to 5 :"))
     randomnumber = randint(1,5)

     if guessnumber == randomnumber:
        print("You have won")
     else:
        print("You have lost")
        print("The random is ",randomnumber)

