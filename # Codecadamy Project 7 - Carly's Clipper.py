# Codecadamy Project 7 - Carly's Clippers

# Project around loops and list comprehensions

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0

for price in prices:
  total_price += price
print('\n' + "The sum of all the different haircut prices is: " + str(total_price))
average_price = total_price/(len(prices))
print("Average Haircut Price: ", str(average_price))

new_prices = [price - 5 for price in prices]
print("New prices with discount of 5: ", new_prices)
total_revenue = 0

for i in range(0, len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
print("Total Revenue: ", str(total_revenue))
average_daily_revenue = total_revenue/7
print("Average Daily Revenue:", average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print("The following haircuts cost less than 30: ", cuts_under_30, '\n')