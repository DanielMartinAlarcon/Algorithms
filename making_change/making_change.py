#!/usr/bin/python

import sys

def making_change(amount, denominations, cache=None):

  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif n == 1:
    return 1
  else: 
    if cache[n] > 0:
      return cache[n]
    else:
      cache[n] = sum([making_change(n-d) for d in denominations])
      return cache[n]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")