def secret(filename):
  word_count = {}
  with open(filename, 'r+') as infile:
    ff = infile.read()
    no_lines = len(ff)
    # print("No of lines are: ", no_lines)
    unique_words = set(ff.split())
    words = ff.split()
    # print("Unique Words are as follows: ", unique_words)
    # print("Words are as follows: ", words)
  
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