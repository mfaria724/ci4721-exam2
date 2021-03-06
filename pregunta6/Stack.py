from utils import cast_value, check_number_of_args, print_error

class Stack:

  def __init__(self) -> None:
    """
      Initializes the stack.
    """
    self.stack = []

  def push(self, instr):
    """
      Reads the value in the command and pushes it to the top of the stack.
    """
    
    # check that we have an id to store the value
    if not check_number_of_args(instr, 2):
      return

    # get the value provided
    val = instr[1]
    casted_val = cast_value(val)

    # check if the value is correct
    if casted_val == None:
      print_error('El valor debe ser un literal entero o booleano.' + \
                  f' Valor: {val}')
      return

    # adds it to the top of the stack
    self.stack.append(casted_val)

  def pop(self):
    """
      Pops an element from the stack.
    """
    self.stack.pop()

  def top(self):
    """
      Returns the last element of the stack.
    """
    return self.stack[-1]

  def top2(self):
    """
      Returns the 2 top elements in the stack
    """
    return self.stack[-2:]

  def print(self):
    """
      Prints the state of the stack
    """
    print('\033[1;37mPila (Fondo <<==>> Tope):\033[0m ', self.stack)

  def length(self):
    """
      Returns the number of elements in the stack
    """
    return len(self.stack)
