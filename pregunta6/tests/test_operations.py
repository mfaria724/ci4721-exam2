import unittest
from Stack import Stack
from operations import binary, unary

class TestOperations(unittest.TestCase):

  # check if sum works
  def test_sum(self):
    stack = Stack()
    stack.push(['PUSH', '1'])
    stack.push(['PUSH', '1'])
    binary('ADD', stack)
    self.assertEqual(stack.stack, [2])

  # check if "not" works
  def test_not(self):
    stack = Stack()
    stack.push(['PUSH', 'false'])
    unary('NOT', stack)
    self.assertEqual(stack.stack, [True])

  # check if reports division by 0
  def test_div_by_zero(self):
    stack = Stack()
    stack.push(['PUSH', '0'])
    stack.push(['PUSH', '1'])
    binary('DIV', stack)
    self.assertEqual(stack.stack, [0, 1])

  # check if checks for types with unary operators
  def test_incorrect_type_unary(self):
    stack = Stack()
    stack.push(['PUSH', 'false'])
    unary('UMINUS', stack)
    self.assertEqual(stack.stack, [False])

  # check if checks for types in binary operators
  def test_incorrect_type_binary(self):
    stack = Stack()
    stack.push(['PUSH', 'false'])
    stack.push(['PUSH', '1'])
    binary('ADD', stack)
    self.assertEqual(stack.stack, [False, 1])
    

if __name__ == '__main__':
  unittest.main()
