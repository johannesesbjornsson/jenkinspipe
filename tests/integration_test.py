import os
from inspect import getsourcefile
import sys
current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]
sys.path.insert(0, parent_dir+'/app')


import letter_mod
import number_mod

import unittest

class IntegrationTest(unittest.TestCase):

  def test_get_random_letters(self):
    numbs = number_mod.get_some_numbers()
    string = letter_mod.get_some_letters(numbs)
    self.assertEqual(type(string),str)
    self.assertEqual(len(string),100)


if __name__ == '__main__':
  unittest.main()
