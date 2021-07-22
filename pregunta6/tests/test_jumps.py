import unittest
from unittest import result
from jumps import goto_contional, goto

class TestJumps(unittest.TestCase):

  # check if go conditional returns the correct index
  def test_goto_conditional(self):
    instr = ['GOTO', 'GOTO']
    labels = {
      'GOTO': 15
    }
    result = goto_contional(instr, True, labels, True)
    self.assertEqual(result, 14)

  # checks if reports that the label doesn't exists.
  def test_goto_conditional_doesnt_exist(self):
    instr = ['GOTO', 'GOTO']
    labels = {
      'GOTO1': 15
    }
    result = goto_contional(instr, True, labels, True)
    self.assertEqual(result, None)

if __name__ == '__main__':
  unittest.main()
