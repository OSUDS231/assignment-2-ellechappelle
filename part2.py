# Author: Elle Chappelle
# GitHub Username: ellechappelle
# Date: 04/29/2026
# Description: Calcultaes a plant's future height by applying a fixed percentage increase each day and a fixed boost amount every 7 days

# task 2.1
initial_height = float(input("Please enter initial height of the plant (in cm): "))
daily_growth = float(input("Please enter the daily growth rate (as a decimal): "))
days = int(input("Please enter the number of days: "))
boost_amount = float(input("Please enter the boost amount (in cm): "))

# task 2.2
height = initial_height
for i in range(days):
    height += height * daily_growth
    if i in range(6,days,7):
        height += boost_amount

# task 2.3
print(f"After {days} days (with a {boost_amount} cm boost every 7th day), the plant is {round(height,2)} cm tall.")

