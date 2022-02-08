#xargs
def student (*details):
    print(details)

student(101,"Priya")
student(101,"Priya",5.00)

#xargs
def student (*details):
    print(details[0])

student(101,"Priya")
student(101,"Priya",5.00)

#xargs
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

add(20,30)
add(20,30,40)
add(30,40,203)


#xxargs
def student(**details):
   print(details)

student(id=101,name="Priya")

#xxargs
def student(**details):
   print(details['name'])

student(id=101,name="Priya")

