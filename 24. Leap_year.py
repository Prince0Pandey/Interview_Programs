# Leap year using calender module of python

# import calendar
# year = int(input("Please Enter a year: "))
# leap_year = "Leap year" if calendar.isleap(year) else "Not a leap year"
# print(leap_year)

# year = int(input("Please Enter a year: "))
# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 ==0:
#             print(f"{year} is leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is leap year")
# else:
#     print(f"{year} is not a leap year")

year = int(input("Please Enter a year: "))
leap_year = "Leap year" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "Not a leap year"
print(leap_year)
