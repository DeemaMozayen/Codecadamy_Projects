# Codecadamy Project 3 - Magic8Ball

# This script generates a random number and uses it to produce a response to a Y/N question
import random
random_number = random.randint(1, 12)

name = "Deema"

# input yes or no question:
question = "Is the sky blue? \n"
answer = ""

if len(question) == 0:
  print("Invalid Question")
elif len(name) == 0:
  print("Question: " + question)
else:
   print('\n' + name + " asks: " + question)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Aww hell no"
elif random_number == 11:
  answer = "lol"
elif random_number == 12:
  answer = "Get outta here"
else:
  answer = "Error"

print("Magic 8-Ball's answer: " + answer + '\n')
