#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  def rps(list1):
    list2 = []
    for item in list1:
      list2.append(item + ['rock'])
      list2.append(item + ['paper'])
      list2.append(item + ['scissors'])
    return list2
  
  starting_list = [['rock'],['paper'],['scissors']]
  
  if n == 0:
    return [[]]
  elif n == 1:
    return starting_list
  else:
    list1 = starting_list
    list2 = []
    for i in range(1, n):
      list2 = rps(list1)
      list1 = list2

    return list2


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')