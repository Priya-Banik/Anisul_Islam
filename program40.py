"""
#runtime error/incorrect input/incorrect code
num = int(input("Enter a number:"))#without int() ,type error
result = 20/num
print(result)
print('Done')

"""
"""
num = int(input("Enter a number:"))
result = 20/num#divide by zero,zero divition error
print(result)
print('Done')
"""
"""
text = "Priya"
print(text[5])#index error
"""


try:
    list = [20,0,30]
    result = list[0] / list[1]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Divition by zero is not possible")

try:
    list = [20, 0, 30]
    result = list[0] / list[3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Divition by zero is not possible")
except IndexError:
    print("Index Error")
print("Successful")

try:
    list = [20, 0, 30]
    result = list[0] / list[3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Divition by zero is not possible")
finally:
    print("Successful")

