# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn’t exist in the list add the fruit to the list and print the modified list. If the fruit exists print(‘That fruit already exist in the list’)

# TODO

new_fruit = input("Enter new fruit: ")


if new_fruit in fruits:
   print("That fruit already exist in the list")
else:
   fruits.append(new_fruit)
   print(fruits)