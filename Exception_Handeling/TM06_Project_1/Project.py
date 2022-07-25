data = []
zz = 0
total = 0
try:
    k = open("buy.txt",'r') 
    lines = k.readlines() 
    for line in lines:
        if not line.isspace():
            data += line.strip().split(" ")
    
            if str('free') in data:
                c = data.count('free')
                nw = len(data[1::2]) - 1
            else:
                nw = len(data[1::2])
                c = 0
    nw = len(data[1::2]) - 1
    for element in data:
        if isinstance(element, int) or element.isdigit():
            total += int(element)
    
    if str('Discount') in data:
        k = data.index('Discount')
        y = k + 2
        dis = data[k+1:y:]
        zz = dis[0]
        total = total - int(zz)
    print("No. of items purchased:",nw-c)
    print("No. of free items:", c)
    print("Amount to pay:",total)
    print("Dicount given:",zz)
    print("Final amount paid:",total-int(zz))

except IOError:
    print("file Not found")