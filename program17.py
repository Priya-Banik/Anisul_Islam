subjects = ["C","C++","Java","Algo","Swift"]
print(len(subjects))

subjects = ["C","C++","Java","Algo","Swift"]
subjects.append("TOC")
print(subjects)

subjects = ["C","C++","Java","Algo","Swift"]
subjects.insert(2,"TOC")
print(subjects)

subjects = ["C","C++","Java","Algo","Swift"]
subjects.remove("Java")
print(subjects)

subjects = ["C","C++","Java","Algo","Swift"]
subjects.sort()
print(subjects)

subjects = [20,4,10,15,9,55]
subjects.sort()
print(subjects)

subjects = ["C","C++","Java","Algo","Swift"]
subjects.reverse()
print(subjects)

subjects = [20,4,10,15,9,55]
subjects.reverse()
print(subjects)

subjects = ["C","C++","Java","Algo","Swift"]
subjects.pop()
subjects.pop()
print(subjects)

subjects = [20,4,10,15,9,55]
pos = subjects.index(4)
print(pos)

subjects = [20,4,10,15,9,55,4,5,44,4]
pos = subjects.count(4)
print(pos)

subjects = ["C","C++","Java","Algo","Swift","Swift","Swift"]
pos = subjects.count("Swift")
print(pos)


subjects = ["C","C++","Java","Algo","Swift"]
subjects2 = subjects.copy()
print(subjects2)

subjects = ["C","C++","Java","Algo","Swift","Swift","Swift"]
subjects.clear()
print(subjects)









