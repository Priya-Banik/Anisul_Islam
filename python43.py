class student:
    roll = ""
    gpa = ""


rahim = student()
print(isinstance(rahim,student))
rahim.roll = 101
rahim.gpa = 3.71
print(f"roll : {rahim.roll},gpa : {rahim.gpa}")

karim = student()
karim.roll = 102
karim.gpa = 3.76
print(f"roll : {karim.roll},gpa : {karim.gpa}")