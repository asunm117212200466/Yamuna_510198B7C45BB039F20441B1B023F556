#write a prigram that determines whether a year entered by the user is a leap year or not using if elfi..else statements
def isLeapYear(year):
  if(year%400==0 or (year%4==0 and year%100!=0)):
    return True
  else:
    return False
year=int(input("Enter a year:"))
if isLeapYear(year):
  print("This is a leap year.",format(year))
else:
  print("This is not a leap year.", format(year))