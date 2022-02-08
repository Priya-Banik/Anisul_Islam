def add(a,b):
    sum = a+b
    return  sum

result = add(20,30)
print("result = ",result)

def large(a,b):
    if a>b:
       return  a
    else:
        return b
result = large(20,30)
print("result = ",result)
print("result = ",large(100,30))

max = large
print(max(20,30))

