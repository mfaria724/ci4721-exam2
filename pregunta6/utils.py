def cast_value(value):
  """
    Checks if the value is an integer or boolean literal
    If it isn't, returns None.
  """

  # cast value as boolean
  if value == 'true':
    value = True
  elif value == 'false':
    value = False
  # cast value as integer or report error
  else:
    try:
      value = int(value)
    except:
      return None

  return value

def print_error(message):
  """
    Prints an error with a coloured marker.
  """
  print(f'\033[1;31mError: \033[0m', message)

def check_number_of_args(instr, n_args):
  """
    Checks if an instruction has the given number of arguments. If it doesn't
    prints an error.
  """

  if len(instr) < n_args:
    print_error(f'Instrucción inválida. Instrucción {instr}')
    return False

  return True
