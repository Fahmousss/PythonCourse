# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

check_month = input("Enter month: ")

season = {
    "Autumn": ["September", "October", "November"],
    "Winter": ["December", "January", "February"],
    "Spring": ["March", "April", "May"],
    "Summer": ["June", "July", "August"],
}

for seasons, month in season.items():
   if check_month in month:
      print(seasons)
   else:
      print("Month doesnt exist")
