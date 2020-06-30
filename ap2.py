#!/usr/bin/env python
# coding: utf-8

# In[ ]:


with open("ap2.txt") as f:
    data=f.readlines()
    for line in data:
        word=line.split()
        print(word)


