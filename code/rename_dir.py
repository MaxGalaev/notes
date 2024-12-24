import os

tree = os.walk('/Users/max/Documents')
for i in tree:
  print(i)
