from curses.ascii import isspace
import sys
# s = '   \t'
# print(s.isspace())
file_name = sys.argv[1]

try:
  file_read = open(file_name, "r")
  lines = file_read.readlines()

  for line in lines:
    if line.isspace() == False:
      print(line)
  file_read.close()

except:
  print("\nFile not Found..")
