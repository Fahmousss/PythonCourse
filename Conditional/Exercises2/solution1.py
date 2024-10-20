scores = int(input("Enter your score: "))

if scores >= 80 and scores <= 100:
   print("A")
elif scores >= 70 and scores < 80:
   print("B")
elif scores >= 60 and scores < 70:
   print("C")
elif scores >= 50 and scores < 60:
   print("D")
else:
   print("F")