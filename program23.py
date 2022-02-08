n = input("Enter a text of Numbers:")  # 10 20 30
list = n.split()  # 10,20,30
sum = 0

for num in list:
    sum = sum + int (num)
print(sum)


numofletters = 0
numofwords = 0
numofdigits = 0
text = input("Enter a text of numbers:")   # My name is Priya banik 233

for x in text:
    x = x.lower()
    if x >= 'a' and x <='z':
        numofletters = numofletters+1

    elif x == " " :
        numofwords = numofwords + 1

    elif x >= "0" and x <= "9" :
        numofdigits = numofdigits + 1

print("Num of letters are: ", numofletters)
print("Num of words are: ", numofwords +1)
print("Num of digits are: ", numofdigits)









