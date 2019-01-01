import string
import random

def get_some_numbers():
  numbers = []
  for x in range(100):
    random_int = random.randint(0,25)
    numbers.append(random_int)
  return numbers

def get_some_letters(numbers):
  lowercase_letters = string.ascii_lowercase
  new_awesome_string = ''
  for number in numbers:
    new_awesome_string += lowercase_letters[number]

  return new_awesome_string
