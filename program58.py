import re

pattern = r"[aeiou]"
if re.match(pattern,"anunnhfufui"):
    print("matched1")

pattern = r"[a-z]"
if re.match(pattern,"ggghh"):#(Asss)it will not work
    print("matched2")

pattern = r"[0-9]"
if re.match(pattern,"0ggghh"):#(a0ujk)it will not work
    print("matched3")

pattern = r"[A-Z][a-z][0-9]"
if re.match(pattern,"Ag0gghh"):#(Agg0),(g0A) it will not work..you have match the syquence
    print("matched4")

