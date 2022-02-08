"""
match() : finds a match of a pattern (beginning) in the string
search() : finds a match of a pattern (anywhere) in the string
findall() : returns a list of all substring that match the pattern
"""


import re
pattern = r"Taehyung"
if re.match(pattern,"Taehyung is a kidol,he is my fav kidol"):
    print("Match")
else:
    print("Not matched")

pattern = r"kidol"
if re.match(pattern, "Taehyung is a kidol,he is my fav kidol"):
    print("Match")
else:
    print("Not matched")




pattern = r"kidol"
if re.search(pattern, "Taehyung is a kidol,he is my fav kidol"):
    print("Match")
else:
    print("Not matched")


pattern = r"kidol"
print(re.findall(pattern,"Taehyung is a kidol,he is my fav kidol"))