import re
pattern = R"colour"
text1 = "Red is a colour.i love red colour"
text2 = re.sub(pattern,"color",text1)
print(text2)

import re
pattern = R"colour"
text1 = "Red is a colour.i love red colour"
text2 = re.sub(pattern,"color",text1,count=1)
print(text2)