# Codecadamy Project 4 - Saul's Shipping

# This script calculates and presents the cheapest shipping method (out of 3) for a given parcel weight

# Generate a random parcel weight:
import random
weight = random.randint(1, 50)

# Alternatively, manually input weight in lb here:
    #weight = 41.5
print('\n' + "Your package weighs " + str(weight) + "lb"'\n')

# Ground Shipping:
if weight <= 2:
  Ground = 1.5*weight+20
elif weight <= 6:
  Ground = 3*weight+20
elif weight <= 10:
  Ground = 4*weight+20
else:
  Ground = 4.75*weight+20

# Premium Ground Shipping:
Premium = 125

# Drone Shipping:
if weight <= 2:
  Drone = 4.5*weight
elif weight <= 6:
  Drone = 9*weight
elif weight <= 10:
  Drone = 12*weight
else:
  Drone = 14.25*weight

print("Ground Shipping: $" + str(Ground))
print(("Premium Ground Shipping: $" + str(Premium)))
print("Drone Shipping: $" + str(Drone),'\n')

cheapest_cost = min(Ground, Premium, Drone)

if cheapest_cost == Ground:
  print("The cheapest cost for this weight is: $" +str(cheapest_cost) + " by - Ground Shipping" + '\n')
if cheapest_cost == Premium:
  print("The cheapest cost for this weight is: $" +str(cheapest_cost) + " by - Premium Ground Shipping" + '\n')
if cheapest_cost == Drone:
  print("The cheapest cost for this weight is: $" +str(cheapest_cost) + " by - Drone Shipping" + '\n')