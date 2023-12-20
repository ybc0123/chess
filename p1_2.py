# -*- coding: utf-8 -*-
"""P1_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15bfSILW2fptbmCTQRwS1MtsshIn1-6t1
"""

S = input().split()
D = input().split()
x1,y1 = int(S[0]),int(S[1])
x2,y2 = int(D[0]),int(D[1])

if checkerboard[x2][y2]==1:
    print("No")
elif (abs(y2 - y1) != abs(x2 - x1) and (x1 != x2 and y1 != y2)):
    print("No")
else:
    if x1==x2:
        a_x = 0
    else:
        a_x=(x2-x1)//abs(x2-x1)
    if y1 == y2:
        a_y = 0
    else:
        a_y=(y2-y1)//abs(y2-y1)
    tmp_x,tmp_y=x1+a_x,y1+a_y
    while tmp_x != x2 or tmp_y !=y2:
        if tmp_x < 0 or tmp_x > 7 or tmp_y < 0 or tmp_y > 7:
            break
        elif checkerboard[tmp_x][tmp_y]==1:
            break
        else:
            tmp_x = tmp_x + a_x
            tmp_y = tmp_y + a_y
    if tmp_x ==x2 and tmp_y==y2:
        print("Yes")
    else:
        print("No")