'''Utils'''
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
  for index in int_list_2:
    int_list_1.append(index)
  return int_list_1

def sub(ints_list: list[int], start_idx: int, end_idx: int) -> list[int]:
  '''returns certain numbers in a list'''
  new_list: list[int] = []
  for index in range(start_idx, end_idx):
    new_list.append(ints_list[index])
  return new_list


      