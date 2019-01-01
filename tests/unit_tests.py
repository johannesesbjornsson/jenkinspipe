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

class TestLogic(unittest.TestCase):

  def test_number_gen(self):
    number_list = number_mod.get_some_numbers()
    self.assertEqual(type(number_list),list)
    self.assertEqual(all(isinstance(n, int) for n in number_list),True)

  def test_gen_letters(self):
    string = letter_mod.get_some_letters([0,1,2])
    self.assertEqual(string, 'abc')

if __name__ == '__main__':
  unittest.main()
