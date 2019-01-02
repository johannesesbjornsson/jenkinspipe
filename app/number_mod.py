import random

def get_some_numbers():
  numbers = []
  for x in range(100):
    random_int = random.randint(0,27)
    numbers.append(random_int)
  return numbers
