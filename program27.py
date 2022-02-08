num = {1,2,3,4,5}
print(num)
num = {1,2,3,4,5,5}
print(num)

num1 = {1,2,3,4,5}
num2 = set([4,5,6,7])
print(num2)
print(7 in num2)

num2.add(8)
num2.remove(7)
print(num2)
print(7 in num2)
print(6 not in num1)

num1 = {1,2,3,4,5}
num2 = set([4,5,6,7])
print(num1 | num2)
print(num1 & num2)
print(num1 - num2)
print(num2 - num1)




