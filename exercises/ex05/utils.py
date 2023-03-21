'''More Utils.'''
__author__ = '730611189'

def only_evens(ints_list: list[int]) -> list[int]:
  '''return all eveent numbers in a list'''
  evens_list: list[int] = []
  for index in range(0, len(ints_list)):
    if ints_list[index] % 2 == 0:
      evens_list.append(ints_list[index])
  return evens_list

def concat(int_list_1: list[int], int_list_2: list[int]) -> list[int]:
  '''combines the numbers in 2 lists'''
  new_list: list[int] = []
  for index in int_list_1:
    new_list.append(index)
  for index in int_list_2:
    new_list.append(index)
  return new_list

def sub(ints_list: list[int], start_idx: int, end_idx: int) -> list[int]:
  '''returns certain numbers in a list'''
  if start_idx < 0: start_idx = 0
  if end_idx > len(ints_list): end_idx = len(ints_list)
  if len(ints_list) == 0: return []
  if start_idx == len(ints_list): return []
  new_list: list[int] = []
  for index in range(start_idx, end_idx):
    new_list.append(ints_list[index])
  return new_list

