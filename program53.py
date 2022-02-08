"""
magic methods for comparision
_eq_(self,other)..every of this end with(self,other)
_eq_for ==
_ne_for !=
_lt_ for <
_le_ for <=
_gt_ for >
_ge_ for >=

magic methods for arithmetic calculation
_add _(self,other)
_sub _(self,other)
_mul _(self,other)
_div _(self,other)
"""


class bike:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __eq__(self, other):
          return self.name == other.name and self.color == other.color

    def __str__(self):
        return(f"name = {self.name},color = {self.color}")

    def display(self):
        print(f"name = {self.name},color = {self.color}")

"""
bike1 = bike("yamaha R15","blue")
bike2 = bike("yamaha FZ","red")
print(str(bike1))

"""

bike1 = bike("yamaha R15","blue")
bike2 = bike("yamaha R15","blue")
print(bike1 == bike2)


