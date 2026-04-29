# Author: Elle Chappelle
# GitHub Username: ellechappelle
# Date: 04/29/2026
# Description: Determines the necessary frequency of boosts ofr a plant to reach the target height within the days available given its initial height, growth rate, and boost amount

# task 4.1
initial_height = float(input("Please enter initial height of the plant (in cm): "))
daily_growth = float(input("Please enter the daily growth rate (as a decimal): "))
target_height = float(input("Please enter the desired height (in cm): "))
days = int(input("Please enter the number of days available: "))
boost_amount = float(input("Please enter the boost amount (in cm): "))

# task 4.2
best_interval = 0
for i in range(days, 0, -1):
    height = initial_height
    for day in range(days):
        height += height * daily_growth
        if day in range(i - 1, days, i):
            height += boost_amount
    if height >= target_height:
        best_interval = i
        break

# task 4.3
if best_interval > 0:
    print(f"To reach at least {target_height} cm in {days} days, apply a {boost_amount} cm boost every {best_interval} days.")
else:
    print(f"Target height not achievable within {days} days, even with daily boosts.")

# TO-DO: CHECK IF target_height SHOULD BE INT OR FLOAT