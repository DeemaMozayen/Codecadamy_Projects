# Codecadamy Project 8 - Functions for Physics Class

# Use functions to solve some basic physics equations

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3 *10**8

def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print('\n'+ "The GE train supplies", train_force, "Newtons of force.")

def get_energy(mass, c):
  return(mass*c**2)
bomb_energy = get_energy(bomb_mass, c)
print("A 1kg bomb supplies", (bomb_energy), "Joules.")

def get_work(mass, acceleration, distance):
  return (get_force(mass, acceleration)*distance)
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")
 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return round(c_temp, 2)

f100_in_celsius = f_to_c(90)
print("90F in degC is: " + str(f100_in_celsius))

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return round(f_temp, 2)

c0_in_fahrenheit = c_to_f(0)
print("0 degC in F is: " + str(c0_in_fahrenheit) + '\n')