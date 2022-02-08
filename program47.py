class phone:#parent class,super class,base class
    def call(self):
        print("You can call")
    def message(self):
        print("You can message")


class samsung(phone):#sub class,child class,derived class
    def photo(self):
        print("You can take photo")

p = phone()
p.message()
p.call()

q = samsung()
q.message()
q.call()
q.photo()
print(issubclass(samsung,phone))