try:
  file1 = open("Q1.txt","r+")
  print("Output of Read function is ")
  print(file1.read())
  file1.close()
except:
  print("File Doesn't Exist")