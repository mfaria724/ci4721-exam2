import unittest

from utils import cast_value, check_number_of_args

class TestUtils(unittest.TestCase):

  # check if returns true when has correct number of arguments
  def test_has_2_arguments(self):
    instr = ['PUSH', '1']
    n_args = 2
    result = check_number_of_args(instr, n_args)
    self.assertTrue(result)

  # check if returns false when has incorrect number of arguments
  def test_has_not_2_arguments(self):
    instr = ['PUSH']
    n_args = 2
    result = check_number_of_args(instr, n_args)
    self.assertFalse(result)

  # checks if it casts to true
  def test_cast_to_true(self):
    value = 'true'
    result = cast_value(value)
    self.assertTrue(result)

  # checks if it casts to false
  def test_cast_to_false(self):
    value = 'false'
    result = cast_value(value)
    self.assertFalse(result)

  # checks if it casts to int
  def test_cast_to_int(self):
    value = '2'
    result = cast_value(value)
    self.assertEqual(result, 2)

  # checks if it casts to none
  def test_cast_to_none(self):
    value = 'asasas'
    result = cast_value(value)
    self.assertEqual(result, None)

if __name__ == '__main__':
  unittest.main()
