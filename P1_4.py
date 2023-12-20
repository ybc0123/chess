#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s=input().split()
d=input().split()
x1,y1=int(s[0]),int(s[1])
x2,y2=int(d[0]),int(d[1])
if checkerboard[x2][y2]==1:
    print('No')
elif abs(x1-x2)==0 and abs(y1-y2)==0:
    print('No')
elif abs(x1-x2)==2 and abs(y1-y2)==1:
    print('Yes')
elif abs(x1-x2)==1 and abs(y1-y2)==2:
    print('Yes')
else:
    print('No')

