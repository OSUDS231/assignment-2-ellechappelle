# Author: Elle Chappelle
# GitHub Username: ellechappelle
# Date: 04/29/2026
# Description:

# task 1.1
initial_height = float(input("Please enter initial height og the plant (in cm): "))
daily_growth = float(input("Please enter the daily growth rate (as a decimal): "))
days = int(input("Please enter the number of days: "))

# task 1.2
height = initial_height
for i in range(days):
    height += height * daily_growth

# task 1.3
print(f"After {days} days, the plant is {round(height, 2)} cm tall.")