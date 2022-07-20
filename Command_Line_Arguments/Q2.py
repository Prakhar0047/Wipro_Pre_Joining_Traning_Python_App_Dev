import os, sys
f_name, f_ext = os.path.splitext('Q2.txt')
welcome_message = sys.argv[1]
print(welcome_message, "File Name is:", f_name)