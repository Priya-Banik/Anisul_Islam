sum = 0
i = 1
while i<=100:
    sum = sum+i
    i = i+1
print(sum)

n = int(input("Enter the last term: "))
f = int(input("Enter the update:"))
sum = 0
i = 1
while i<=n:
    sum = sum+i
    i = i+f
print(sum)
