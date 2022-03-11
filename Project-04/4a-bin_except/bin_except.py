# Author: Timur Guner
# Date: 2021-04-28
# Description: Project 4a takes the binary sort from the module and adds an exception when the item is not found


class TargetNotFound(Exception):
  """Target Not Found"""
  pass

def bin_except(a_list, target):
  """
  Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, raise TargetNotFound
  """
  first = 0
  last = len(a_list) - 1
  while first <= last:
    middle = (first + last) // 2
    if a_list[middle] == target:
      return middle
    if a_list[middle] > target:
      last = middle - 1
    else:
      first = middle + 1
  raise TargetNotFound

def main():
    try:
      binary_list = bin_except([1,2,3,4,5],6)
      print(binary_list)
    except TargetNotFound:
      print("Not in list")

if __name__ == '__main__':
  main()