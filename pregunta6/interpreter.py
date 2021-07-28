from Stack import Stack
from operations import binary_operations, unary_operations, binary, unary
from io_instr import read_id, print_id
from jumps import goto, goto_contional
from ids import rvalue, lvalue, assign
from utils import print_error
import sys

def format_instruction(instr, index, labels):
  """
    Checks if the format for an instruction is correct.
    Also sets all the labels contained in the code.
  """

  # remove new line characters
  new_instr = instr.replace('\n', '')

  # split the line by spaces
  new_instr = new_instr.split(' ')

  # if there's something in the instruction
  if len(new_instr) > 0:
    first_token = new_instr[0]
    if first_token.endswith(':'):
      labels[first_token[:-1]] = index
      new_instr = new_instr[1:]
  # if instruction is empty, there's an error.
  else:
    print_error(f'Instrucción Inválida en la línea {index+1}. \n\tInstrucción: {instr}')
    return
  
  return new_instr  

def main():

  # gets the name of the file that contains the program
  try:
    filename = sys.argv[1]
  except:
    print('\033[1;37mUsage:\033[0m python3 interpreter.py PROGRAM')
    sys.exit(1)

  try:
    # reads the program
    file = open(filename)
    lines = file.readlines()

  except FileNotFoundError:
    print('El archivo especificado no fue encontrado.')
    sys.exit(1)

  # initializes the structures for labels and ids
  labels = {}
  ids = {}
  
  # format every line in the file.
  lines = [format_instruction(line, index, labels) for index, line in enumerate(lines)] 

  # instaciates the stack
  stack = Stack()

  # initializes values to iterate
  index = 0
  binary_ops = list(binary_operations.keys())
  unary_ops = list(unary_operations.keys())

  while index < len(lines):
    # gets the instruction
    instr = lines[index]

    first_token = instr[0]

    # checks which function needs to be called.
    if first_token == 'EXIT':
      sys.exit(0)
    elif first_token == 'RESET':
      stack.stack = []
      labels = {}
      ids = {}
      print('stack: ', stack.stack)
      print('labels: ', labels)
      print('ids: ', ids)

    elif first_token == 'READ':
      read_id(instr, ids)
    elif first_token == 'PRINT':
      print_id(instr, ids)
    elif first_token == 'PUSH':
      stack.push(instr)
    elif first_token == 'POP':
      stack.pop()
    elif first_token == 'GOTO':
      label_index = goto(instr, labels)
      if label_index:
        index = label_index
    elif first_token == 'GOTRUE':
      label_index = goto_contional(instr, stack.top(), labels, True)
      if label_index:
        index = label_index
    elif first_token == 'GOFALSE':
      label_index = goto_contional(instr, stack.top(), labels, False)
      if label_index:
        index = label_index
    elif first_token == 'RVALUE':
      rvalue(instr, ids, stack)
    elif first_token == 'LVALUE':
      lvalue(instr, stack)
    elif first_token == 'ASSIGN':
      assign(stack, ids) 
    elif first_token in binary_ops:
      binary(first_token, stack)
    elif first_token in unary_ops:
      unary(first_token, stack)
    else:
      print_error(f'Opción inválida. Opción: {first_token}')

    index += 1

if __name__ == '__main__':
  main()
