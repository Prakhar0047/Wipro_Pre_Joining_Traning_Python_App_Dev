# Replacing Vowels
s = input()
l = list(s.lower())

for x in range(len(l)):
  if l[x] == "a" or l[x] == "e" or l[x] == "i" or l[x] == "o" or l[x] == "u":
    l[x] = "z"
print("".join(l))