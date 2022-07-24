fname = input("Enter file name: ")
num_lines = 0
frequency = 0
frequent_word = ""
words = []
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
        line_word = line.lower().replace(',','').replace('.','').split(" ")
        for w in line_word:  
            words.append(w)
    for i in range(0, len(words)):
        count = 1 
        for j in range(i+1, len(words)):  
            if(words[i] == words[j]):  
                count = count + 1
        if(count > frequency):  
            frequency = count 
            frequent_word = words[i]
if num_lines > 12:
    num_lines = num_lines - 12
    print("Metting time:",num_lines,"P.M")
else:
    print("Metting time:",num_lines,"A.M")
print("Meting Place:",frequent_word.capitalize(),"Street")