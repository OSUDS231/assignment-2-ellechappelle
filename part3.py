# Author: Elle Chappelle
# GitHub Username: ellechappelle
# Date: 04/29/2026
# Description: Calculates the number of days needed for a plant to reach the target height give its initial height, growth rate, and boost amount

# task 3.1
initial_height = float(input("Please enter initial height of the plant (in cm): "))
daily_growth = float(input("Please enter the daily growth rate (as a decimal): "))
target_height = float(input("Please enter the desired height (in cm): "))
boost_amount = float(input("Please enter the boost amount (in cm): "))

# task 3.2
elapsed_days = 0
height = initial_height
while target_height > height:
    height += height * daily_growth
    if elapsed_days % 7 == 6:
        height += boost_amount
    elapsed_days += 1

# task 3.3
print(f"After {elapsed_days} days (with a {boost_amount} cm boost every 7th day), the plant reaches at least {target_height} cm.")
