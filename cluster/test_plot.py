#-*- coding:utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from kmeans_plus_plus import KmeansPlusPlus
import matplotlib.pyplot as plt

import random

alist = []
blist = []
for i in range(100):
    alist.append(int(100*random.random()))
    blist.append(int(100*random.random()))
data = []
for a,b in zip(alist,blist):
    data.append([a,b])
kpp = KmeansPlusPlus()
res = kpp.clustering(data,2)

plt.figure(figsize=(8, 5), dpi=80)
axes = plt.subplot(111)

ax = []
ay = []
bx = []
by = []
for i,j in zip(res,data):
    if i == 0:
        ax.append(j[0])
        ay.append(j[1])
    else:
        bx.append(j[0])
        by.append(j[1])
axes.scatter(ax,ay,s=20,c='red')
axes.scatter(bx,by,s=20,c='blue')
plt.show()

