print("Welcome to Classified Leap year or not?")
year = int(input("What year would you like to determine?\n"))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year!")
    else:
      print("Not a leap year")
  else:
    print("Leap year!")
else:
  print("Not a leap year")