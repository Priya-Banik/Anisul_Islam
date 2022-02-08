class student:
    roll = " "
    gpa = " "

    def setvalue(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"roll : {self.roll},gpa : {self.gpa}")


rahim = student()
rahim.setvalue(101,3.50)
rahim.display()

karim = student()
karim.setvalue(102,3.72)
karim.display()
