# -*- coding: utf-8 -*-
"""first 2 max elemrnts in list.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qtSbjSxh12O7q3GYKSa3otKGyjYVPlKx
"""

#Write a python code to find first two maximum no in a list.

mylist=[]
n=int(input())
for i in range (0,n):
    x=int(input())
    mylist.append(x)
sorted(mylist)
y=max(mylist)
print(max(mylist))
mylist.remove(max(mylist))
print(max(mylist))
mylist.append(y)