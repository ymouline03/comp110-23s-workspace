def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
  '''building a dictionary'''
  new_dict: dict[str, int] = {}
  if len(str_list) != len(int_list):
    return new_dict
  if len(str_list) == 0:
    return new_dict
  if len(int_list) == 0:
    return new_dict
  for i in range(0, len(str_list)):
    for i in range(0, len(int_list)):
      new_dict[str_list[i]] = int_list[i]
  return new_dict

strl = ['choc', 'van', 'straw']
intl = [2, 3, 4]
print(zip(strl, intl))
