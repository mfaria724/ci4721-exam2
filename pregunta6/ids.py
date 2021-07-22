from utils import check_number_of_args, print_error
import sys

def rvalue(instr, ids, stack):
  """
    Adds to the stack the content of the given id.
    If it doesn't exists reports an error.
  """
  
  # check that we have an id to store the value
  if not check_number_of_args(instr, 2):
    sys.exit(1)

  # get the id we will look for
  id = instr[1]

  # if the id doesn't exists, report an error.
  if not id in ids:
    print_error('El identificador no tiene ningún valor asignado.' + \
                f' Identificador: {id}')
    return 

  # add the value to the top of the stack
  stack.stack.append(ids[id])

def lvalue(instr, stack):
  """
    Adds to the stack the "address" of an id.
    Adding a list to the stack represents an special case that is handled in the
    assign method.
  """
  
  # check that we have an id to store the value
  if not check_number_of_args(instr, 2):
    sys.exit(1)

  # gets the id of which we want the address
  id = instr[1]

  # add the "address" to the stack.
  # we use the type list to identify ids that doesn't have a value
  # they are treated as an special case on assign method.
  stack.stack.append([id])

def assign(stack, labels):
  """
    Assigns the r-value below the top of the stack to the l-value in the top of
    the stack.
    If there are not enough elements or the top isn't an l-value, reports an 
    error.
  """

  # check if there's at least 2 elements in the stack  
  if stack.lenght() < 2:
    print_error('No hay suficientes elementos en la pila.')
    return

  # extract the top 2 elements
  rvalue, lvalue = stack.top2()

  # as described in lvalue method, lists represent l-values.
  if not isinstance(lvalue, list):
    print_error(f'No existe un lvalue en el tope de la pila. Valor: {lvalue}')
    return

  # remove from stack top 2 elements.
  stack.pop()
  stack.pop()

  # assigns the value to the identifier.
  labels[lvalue[0]] = rvalue
