import unittest
from Stack import Stack
from ids import rvalue, lvalue, assign

class TestIds(unittest.TestCase):

  def test_rvalue_correct(self):
    instr = ['RVALUE', 'a']
    ids = {
      'a': 1
    }
    stack = Stack()
    rvalue(instr, ids, stack)
    self.assertEqual(stack.stack, [1])

  def test_rvalue_not_defined(self):
    instr = ['RVALUE', 'a']
    ids = {}
    stack = Stack()
    rvalue(instr, ids, stack)
    self.assertEqual(stack.stack, [])

  def test_lvalue_correct(self):
    instr = ['LVALUE', 'a']
    stack = Stack()
    lvalue(instr, stack)
    self.assertEqual(stack.stack, [['a']])

  def test_assign_correct(self):
    labels = {}
    stack = Stack()

    stack.stack.append(1)
    stack.stack.append(['a'])
    assign(stack, labels)
    self.assertEqual(labels, { 'a': 1 })
  
  def test_assign_missing_args(self):
    labels = {}
    stack = Stack()

    stack.stack.append(['a'])
    assign(stack, labels)
    self.assertEqual(labels, {})

if __name__ == '__main__':
  unittest.main()
