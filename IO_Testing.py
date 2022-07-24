with open('sample.txt', 'r+') as infile:
    ff = infile.read()
    no_lines = len(ff)
    print("No of lines are: ",no_lines)
    unique_words = set(ff.split())
    words = ff.split()
    print("Unique Words are as follows: ",unique_words)
    print("Words are as follows: ",words)