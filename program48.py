"""
class phone:
    def __init__(self):
        print("I am in phone class")

class samsung(phone):
    pass
s = samsung()


class phone:
    def __init__(self):
        print("I am in phone class")

class samsung(phone):
    def __init__(self):
        print("I am in samsung class")
s = samsung()
"""

class phone:
    def __init__(self):
        print("I am in phone class")

class samsung(phone):
     def __init__(self):
        super(samsung, self).__init__()
        print("I am in samsung class")

s = samsung()
