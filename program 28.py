#stack
books = []
books.append("Bangla")
books.append("English")
books.append("Math")
print(books)

books.pop()
print("Now the upper book is ",books[-1])

books.pop()
print("Now the upper book is ",books[-1])

books.pop()
if not books:
   print("No books left")

#queue
from collections import deque

bank = deque(["Priya","Pinky","Anis"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
if not bank :
    print("No person left")