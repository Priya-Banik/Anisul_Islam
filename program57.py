"""
.(dot)(any characyter)
^col..r,col have to in the first
r$ ,r have to in the last
*(0 or more)
+(1 or more)
{1,7}(1 to 7)

"""

import re
pattern = r"colo..r"

#1
if re.match(pattern,"coloubr"):
    print("matched1")

#2
pattern = r"^colo..r$"

if re.match(pattern,"coloubr"):
    print("matched2")

#3
pattern = r"a*"

if re.match(pattern,"colouraaaaa"):
    print("matched3")

pattern = r"(ab)*"

if re.match(pattern,"colourababbaaa"):
    print("matched3!")


#4
pattern = r"a+"

if re.match(pattern, "aaaa"):
    print("matched4")

pattern = r"a+b"

if re.match(pattern, "aaabbbabab"):
    print("matched4!")

pattern = r"a*b"

if re.match(pattern, "b"):
    print("matched4!!")

#5

pattern = r"ice-?cream"

if re.match(pattern, "ice-cream"):
    print("matched5")


#6
pattern = r"a{1,3}"#1,2,3..1 to 3

if re.match(pattern, "aas"):
    print("matched6")










