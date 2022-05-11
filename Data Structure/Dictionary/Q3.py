d={1:1,2:2,3:3}
key=input("Enter key to check:")
if key in d.keys():
  print("Value at key is",d[key])
else:
  print("Key isn't present!")