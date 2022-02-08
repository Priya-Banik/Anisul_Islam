class student:
    roll = " "
    gpa = " "

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"roll : {self.roll},gpa : {self.gpa}")


rahim = student(101,3.50)
rahim.display()

karim = student(102,3.72)
karim.display()
