# Codecadamy Project 6 - Len's Slice

# Project introducing 2D lists [Price, Type of Pizza]

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# Count the number of different types of pizza with price 2:
num_two_dollar_slices = prices.count("2")

num_pizzas = len(toppings)
print('\n' + "We sell " + str(num_pizzas) + " different kinds of pizza!" + '\n')

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"],  [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
sorted_pizzas = sorted(pizza_and_prices)
cheapest_pizza = sorted_pizzas[0]
priciest_pizza = sorted_pizzas[-1]

# .pop removes a given element (default -1) from a list and returns it in isolation:
sorted_pizzas.pop()

# Adds new element with price 2.5, at position 4:
sorted_pizzas.insert(4, [2.5, "peppers"])
print("The pizzas in ascending price order: ", sorted_pizzas, '\n')

three_cheapest = sorted_pizzas[0:3]
print("The three cheapest pizzas: ", three_cheapest, '\n')