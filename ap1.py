#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
    f=open("sample.txt")
except:
    print("file cant be opened")
    exit()
for line in f:
    if line.startswith(""):
        print(line)

