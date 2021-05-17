#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
student_marks ={}
for i in range(n):
    name , *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_student = input()
s=0
for i in student_marks[query_student] :
    s+= i
print("{0:.2f}".format(s/3))


# 2
# 

# In[ ]:





# In[ ]:




