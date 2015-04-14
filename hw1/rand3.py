#!/usr/bin/python

import random
import numpy

def rndstretch(n,lo,hi):
    a=[]
    k=0
    while  k < n:
        a.append(random.random()*(hi-lo)+lo)
        k=k+1
    return a

x = rndstretch(1000,0.,1.)
y=numpy.sqrt(-numpy.log(x))


import matplotlib.pyplot as plt

#hist1=plt.hist(x,10)
hist2=plt.hist(y,100)
plt.savefig('hist2.png')
