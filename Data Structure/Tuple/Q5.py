l = [(10,20,30),(40,50,60),(70,80,90)]
edit_tup = list(l[2][2])
edit_tup[2] = 100
l.append(tuple(edit_tup))
print(l)