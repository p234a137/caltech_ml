# coding: utf-8

# ## EXERCISE 1.10 from the book of Abu-Mostafa

# In[1]:

# In iPython or the iPython notebook, it's easiest to use the pylab magic, which
# imports matplotlib, numpy, and scipy.
# The inline flag means that images will be shown here in the notebooks, rather
# than in pop-up windows.
#get_ipython().magic(u'pylab inline')
# If you are using 'regular' Python, however, you'll want the following. You'll
# need to also separately import numpy and any other packages that you might need.

import numpy as np
import matplotlib.pyplot as plt
import random


# In[2]:

ncoins=30
ntosses=10
ntimes=10000
mu=0.5


# In[3]:

# gather statistics as proposed in exercise 1.10
times=0
nu1=[] # first coin
nu2=[] # random coin
nu3=[] # coin with smallest frequency
while times<ntimes:
    times = times + 1
    i=0
    coins=[]
    while i < ncoins:
        j=0
        sum=0.
        while j < ntosses:
            toss_value = np.random.binomial(1,mu)
            sum = sum + toss_value
            j=j+1    
        coins.append(sum/ntosses)
        i=i+1
    nu1.append(coins[1])
    nu2.append(random.choice(coins))
    nu3.append(min(coins))


# In[4]:

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
##ax1.plot(x,y1, label='sin')
#hist1=plt.hist(nu1,20)
#plt.savefig("hist1.png")
#fig = plt.figure()
#ax = fig.add_subplot(111)
n1, bins1, patches1 = ax1.hist(nu1, 50, normed=1, facecolor='green', alpha=0.75)
n2, bins2, patches2 = ax2.hist(nu2, 50, normed=1, facecolor='blue', alpha=0.75)
n3, bins3, patches3 = ax3.hist(nu3, 50, normed=1, facecolor='red', alpha=0.75)
#plt.show()
fig.savefig('nus.png')


# In[ ]:
