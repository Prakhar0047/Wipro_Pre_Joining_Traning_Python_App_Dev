# Print number of Char
s = input()
l = list(s)
l_loop = set(list(s))
for x in l_loop:
  print(x," - ",l.count(x))