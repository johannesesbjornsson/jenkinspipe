import string
def get_some_letters(numbers):
  lowercase_letters = string.ascii_lowercase
  new_awesome_string = ''
  for number in numbers:
    new_awesome_string += lowercase_letters[number]

  return new_awesome_string

