# Author: Elle Chappelle
# GitHub Username: ellechappelle
# Date: 04/29/2026
# Description:

# task 3.1
initial_height = float(input("Please enter initial height of the plant (in cm): "))
daily_growth = float(input("Please enter the daily growth rate (as a decimal): "))
target_height = float(input("Please enter the desired height (in cm): "))
boost_amount = float(input("Please enter the boost amount (in cm): "))

# task 3.2
days = 0
height = initial_height
while target_height >= height:
    height += height * daily_growth
    if days % 7 == 6:
        height += boost_amount
    days += 1

print(f"After {days} days (with a {round(boost_amount, 2)} cm boost every 7th day), the plant reaches at least {round(target_height, 2)} cm.")