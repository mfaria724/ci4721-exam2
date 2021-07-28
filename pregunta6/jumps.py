from utils import print_error, check_number_of_args
import sys

def goto(instr, labels):
  """
    Returns the index at which a label points. If it doesn't exists return None.
  """

  # check that we have an id to jump
  if not check_number_of_args(instr, 2):
    print_error(f'Instrucción inválida. Instrucción {instr}')
    return

  # get the label to where we wanna jump 
  label = instr[1]

  # if the label doesn't exists, report an error
  if not label in labels:
    print_error(f'Error: No existe la etiqueta. \033[1;37mEtiqueta:\033[0m {label}')
    return None
  
  # return the previous index that will be incremented in the end of iteration
  return labels[label] - 1

def goto_contional(instr, top, labels, condition):  
  """
    Calls goto function depending on the value on the top of the stack.
  """
  # check that we have an id to store the value
  value = goto(instr, labels)
    
  return value if top == condition else None
