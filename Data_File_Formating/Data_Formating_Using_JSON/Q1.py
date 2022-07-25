#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

students_data='''
{
 "students":[
     {
      "name":"James",
      "maths":"30",
      "physics":"18",
      "chemistry":"24",
      "avg":"24"
      },
     {
      "name":"June",
      "maths":"25",
      "physics":"23",
      "chemistry":"27",
      "avg":"25"
      },
      {
      "name":"Max",
      "maths":"27",
      "physics":"21",
      "chemistry":"27",
      "avg":"25"
      },
     {
      "name":"selena",
       "maths":"30",
      "physics":"23",
      "chemistry":"27",
      "avg":"27"
      }
     ]
     }'''
s_data=json.loads(students_data)

with open('student_data.json','w') as f:
    json.dump(s_data,f)
print(s_data)

