
def  calculate(a,b):
    return a*a+2*a*b+b*b
print(calculate(2,3))

print((lambda a,b : a*a+2*a*b+b*b)(2,3))

def cube(x):
    return x*x*x
print(cube(2))

print((lambda x : x*x*x)(2))