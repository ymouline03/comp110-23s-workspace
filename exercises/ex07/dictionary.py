'''Dictionary utils'''

__author__ = '730611189'

def invert(reg_dict: dict[str, str]) -> dict[str, str]:
  '''Inverts the keys and values in a dictionary'''
  inverted_dict = {}
  key_list = []
  value_list = []
  dupe_test = []
  for i in reg_dict:
    key_list.append(i)
  for i in reg_dict:
    value_list.append(reg_dict[i])
  for i in value_list:
    if i not in dupe_test:
      dupe_test.append(i)
  if len(dupe_test) != len(value_list):
    raise KeyError('Cannot have duplicate keys!')
  for i in range(0, len(value_list)):
    for i in range(0, len(key_list)):
      inverted_dict[value_list[i]] = key_list[i]
  return inverted_dict
  
def favorite_color(colors_dict: dict[str, str]) -> str:
  '''Outputs the most common color in the dictionary'''
  value_list = []
  for i in colors_dict:
    value_list.append(colors_dict[i])
  count: int = 0
  color: str = value_list[0]
  for i in value_list:
    freq = value_list.count(i)
    if(freq > count):
      count = freq
      color = i
  return color

def count(any_list: list[str]) -> dict[str, int]:
  '''counts number of each item appearance in a list'''
  new_dict = {}
  key_list = any_list
  value_list = []
  for i in key_list:
    freq = key_list.count(i)
    value_list.append(freq)
  for i in range(0, len(key_list)):
    for i in range(0, len(value_list)):
      new_dict[key_list[i]] = value_list[i]
  return new_dict


