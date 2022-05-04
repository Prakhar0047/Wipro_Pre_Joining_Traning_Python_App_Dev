def is_palinrome(name):
  if name == name[::-1]:
    print(name,"is a palindrome")
  else:
    print(name,"is not a palindrome")

def count_the_vowels(name):
  count = 0
  for x in name:
    if x in ("a","e","i","o","u"):
      count+=1
  print("Number of Vowel:",count)

def frequency_of_letter(name):
  l = []
  for i in set(name):
    temp = i+"-"+str(name.count(i))
    l.append(temp)
  print("Frequency Of letters:",*l)