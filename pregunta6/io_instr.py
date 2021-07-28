from typing import cast
from utils import print_error, check_number_of_args, cast_value
import sys

def read_id(instr, ids):
  """
    Reads a boolean or integer literal.
    If introduced type is incorrect, will ignore and report an error.
  """

  # check that we have an id to store the value
  if not check_number_of_args(instr, 2):
    return
  
  # look for id
  id = instr[1]

  # get user input
  value = input(f'Por favor, ingrese un valor para el identificador {id}. ' +
                '(Entero o true/false): ')

  # check if the entered value has a valid type
  casted_value = cast_value(value)
  if casted_value == None:
    print_error('El valor introducido no es un literal entero o booleano.' + \
                f' Valor: {value}')
    return

  # assign the value to the id
  ids[id] = casted_value

def print_id(instr, ids):
  """
    Prints the value that has been assigned to an id.
    If no value has been assigned, ignores and reports an error.
  """

  # check that we have an id print a value
  if len(instr) < 2:
    print(f'Instrucción inválida. Instrucción {instr}')
    return

  # gets the id
  id = instr[1]

  # checks if the has a value
  if not id in ids or ids[id] == None:
    print_error('No ha sido asignado ningún valor para este identificador.' + \
                f' Identificador: {id}')
  else:
    print(f'\033[1;37mIdentificador:\033[0m {id}, \033[1;37mValor:\033[0m {ids[id]}')
