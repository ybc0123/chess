#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s=input().split()
d=input().split()
x1,y1=int(s[0]),int(s[1])
x2,y2=int(d[0]),int(d[1])
if (x2-x1)==1 and (y1==y2) and checkerboard[x2][y2]==0:
    print("Yes")
else:
    print("No")


# In[ ]:




