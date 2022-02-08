class Triangle:
    def _init_(self,base,height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("Area = ",area)

t1 = Triangle(4,20)
t1.calculate_area()

t2 = Triangle(8,30)
t2.calculate_area()


