def secret(filename):
  word_count = {}
  with open(filename, 'r+') as infile:
    print(infile.read())
    no_lines = len(infile.readlines())
    unique_words = set(infile.read().split())
    words = infile.read().split()
  
  print("No of line",no_lines)
  print("Unique Words",unique_words)
  print("Words are:",words)

  for x in unique_words:
    word_count[words.count(x)] = x
  
  if no_lines>12:
    print("Meeting Time:",24-no_lines,"PM")
  else:
    print("Meeting Time:",no_lines,"AM")

  print("Meeting Place",word_count[max(word_count)],"Street")

secret('sample.txt')