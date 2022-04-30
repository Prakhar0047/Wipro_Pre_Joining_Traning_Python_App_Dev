w = input()

with open("Q6.txt",'r') as infile:
  words = infile.read().split()

print("User Entered words occured",words.count(w),"times.")