import json

with open('student_data.txt','r') as r:
    sd=json.load(r)
for i in sd['students']:
    print(i['name'] +" average marks are:"+i['avg'])

