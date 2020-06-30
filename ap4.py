#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
if os.path.exists("abc.txt"):
    os.remove("abc.txt")
else:
    print("file doesnt exist")

