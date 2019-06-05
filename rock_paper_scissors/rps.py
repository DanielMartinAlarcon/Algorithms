#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  
  # Helper function that takes each item from a list, creates the three possible
  # permutations from that seed, and adds them to another list.
  def rps(list1):
    result = []
    for item in list1:
      result.append(item + ['rock'])
      result.append(item + ['paper'])
      result.append(item + ['scissors'])
    return result
  
  starting_list = [['rock'],['paper'],['scissors']]
  
  # Hard code base cases
  if n == 0:
    return [[]]
  else:
    result = starting_list
    # Run the helper function n-1 times:
    for i in range(1, n):
      result = rps(result)
    
    return result


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')