from utils import print_error

# represents all binary operators by its command name.
# each value of the dictionary represents the function to be applied and 
# the type of which their arguments must be. 
# if the type is None, it means that both must be of the same type, no matter
# what type is it.
binary_operations = {
  'ADD': [lambda x,y: x + y, int],
  'SUB': [lambda x,y: x - y, int],
  'MUL': [lambda x,y: x * y, int],
  'DIV': [lambda x,y: x // y, int],
  'AND': [lambda x,y: x and y, bool],
  'OR': [lambda x,y: x or y, bool],
  'LT': [lambda x,y: x < y, int],
  'LE': [lambda x,y: x <= y, int],
  'GT': [lambda x,y: x > y, int],
  'GE': [lambda x,y: x >= y, int],
  'EQ': [lambda x,y: x == y, None],
  'NEQ': [lambda x,y: x != y, None]
}

unary_operations = {
  'UMINUS': [lambda x: -x, int],
  'NOT': [lambda x: not x, bool]
}

def binary(operation, stack):
  """
    Operates the element in the top of the stack and the element below it
    with the given operation.
  """

  # check if there are enough elements in the stack
  if stack.lenght() < 2:
    print_error('No hay suficientes elementos en la pila.')
    stack.print()
    return

  # get element on the top and below it to operate.
  op2, op1 = stack.top2()

  # get the function to be applied and the required types.
  func, typ = binary_operations[operation]

  # if the type is None, it means that both have to be of the same type.
  if typ == None:
    typ = type(op1)

  # check that operands have the correct types.
  if type(op1) != typ or type(op2) != typ:
    print_error('Los operadores deben ser del mismo tipo y deben tener el' + \
                f' tipo correcto. \033[1;37mOperando 1:\033[0m {op1}. ' + \
                f'\033[1;37mOperando 2:\033[0m {op2}')
    return

    # remove the elements from the stack.
  stack.pop()
  stack.pop()

  # operate the elements and add the result to the top of the stack.
  try:
    stack.stack.append(func(op1, op2))
  except ZeroDivisionError:
    print_error('No es posible dividir entre 0.')
    stack.stack.append(op2)
    stack.stack.append(op1)
    return

def unary(operation, stack):
  """
    Operates the element in the top of the stack with the given operation.
  """

  # check if there are enough elements in the stack
  if stack.lenght() < 1:
    print_error('No hay suficientes elementos en la pila.')
    stack.print()
    return
  
  # get the element to which the operation will be applied
  op = stack.top()

  # get the operation and the expected type.
  func, typ = unary_operations[operation]

  # check if the operator is of the expected type.
  if type(op) != typ:
    print_error('El operador no tiene el tipo correcto.' + \
                f'\033[1;37mOperando:\033[0m {op}. ')
    return

  # remove the element from the stack
  stack.pop()

  # add it back but operated.
  stack.stack.append(func(op))