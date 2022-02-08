""""
#multi_level inheritance
class A :
    def dispaly1 (self):
        print("I am in A class")

class B(A) :
    def dispaly2 (self):
        print("I am in B class")

class C(B) :
    def dispaly3 (self):

    print("I am in C class")


obj1 = C()
obj1.dispaly1()
obj1.dispaly2()
obj1.dispaly3()



"""
#multiple inheritance

class A:
    def dispaly(self):
        print("I am in A class")

class B :
    def display (self):
        print("I am in B class")



class C(A,B) :
      pass


obj1 = C()
obj1.dispaly()


