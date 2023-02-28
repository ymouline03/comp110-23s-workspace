'''Utils'''
__author__ = '730611189'

def all(num_list: list[int], num: int) -> bool:
  '''returns whether or not a number is part of a list'''
  list_len: int = len(num_list)
  index: int = 0
  if list_len == 0:
    return False
  while index < list_len:
    if num != num_list[index]:
      return False
    index += 1
  return True

def max(num_list: list[int]) -> int:
  '''returns ther max number in a list'''
  list_len: int = len(num_list)
  if list_len == 0:
    raise ValueError("max() arg is an empty List")
  index: int = 0
  max_num: int = num_list[0]
  while index < list_len:
    if num_list[index] > max_num:
      max_num = num_list[index]
    index += 1
  return max_num

def is_equal(list1: list[int], list2: list[int]) -> bool:
  '''returns whether or not 2 lists are identical'''
  list1_len = len(list1)
  list2_len = len(list2)
  index = 0
  if list1_len == 0 or list2_len == 0:
    return False
  if list1_len == 0 and list2_len == 0:
    return True
  if list1_len != list2_len:
    return False
  while index < list1_len:
    if list1[index] == list2[index]:
      index += 1
    else:
      return False
  return True



