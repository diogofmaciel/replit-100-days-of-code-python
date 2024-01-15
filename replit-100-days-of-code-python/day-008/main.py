print("Affirmations generator")

name = input("Hello! What is your name? ")
if name == "Diogo":
  print("Hello " + name + "!")
elif name == "diogo":
  print("Mmm... no capitalization... Alright... hello " + name + "!")
else:
  print("Hello " + name + "! I don't think I've seen you around here before!")

weekday = input("What day of the week is it today? ")
validWeekdays = ["Monday", "monday", "Tuesday", "tuesday", "Wednesday", "wednesday", "Thursday", "thursday", "Friday", "friday", "Saturday", "saturday", "Sunday", "sunday"]
while weekday not in validWeekdays:
  weekday = input("Sorry I didn't catch that. State a day of the week with the correct spelling. ")
if weekday in validWeekdays:
  if weekday == "Monday" or weekday == "monday":
    print("Weak... still the whole week to go!")
  elif weekday == "Tuesday" or weekday == "tuesday":
    print("Keep pushing! You will get there!")
  elif weekday == "Wednesday" or weekday == "wednesday":
    print("Hump day! You are doing great!")
  elif weekday == "Thursday" or weekday == "thursday":
    print("Almost there! Just a little more work to do!")
  elif weekday == "Friday" or weekday == "friday":
    print("Wheee! It's Friday! Party time!")
  elif weekday == "Saturday" or weekday == "saturday" or weekday == "Sunday" or       weekday == "sunday":
    print("I hope you are enjoying the weekend!")

average = 5

feeling = int(input("From 1-10, how are you feeling today? "))
if feeling <= int(average):
  print("Keep going! It will get better!")
elif feeling > int(average) and feeling <= 10:
  print("Good to hear! Keep it up!")
elif feeling > 10:
  print("That's amazing! You are having a great time!")
else:
  print("Sorry I didn't catch that. State a number from 1 to 10.")
