my_age = 20
your_age = int(input("Enter your age : "))
diff = my_age - your_age

if diff > 0:
   if diff == 1:
      print(f"You are {diff} year younger than me")
   elif diff > 1:
      print(f"You are {diff} years younger than me")      
elif diff < 0:
   diff = diff * -1
   if diff == 1:
      print(f"You are {diff} year older than me")
   elif diff > 1:
      print(f"You are {diff} years older than me")
elif diff == 0:
   print("We are equal")
