
# coding: utf-8

# # Exercise 1.4 from the book

# In[131]:

#get_ipython().magic(u'pylab inline')
import random
import scipy
import numpy as np


# In[82]:

dimension=2
number_sampling=10


# In[83]:

x1=-0.2; y1=-1
x2=0.5; y2=1
def target(x,y):
    if y>=(y1+(x-x1)*(y2-y1)/(x2-x1)):
         return 1
    else:
        return -1

#print target(0.0,0.1)


# In[97]:

# generate random training points
xn=[]; yn=[]; zn=[];
for i in range(1,number_sampling):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    xn.append(x)
    yn.append(y)
    # classify using zn depending on whether they fall above or below the line
    if y>(y1+(x-x1)*(y2-y1)/(x2-x1)):
        zn.append(+1)
    else:
        zn.append(-1)


# In[98]:

#fig, ax1 = plt.subplots(1, 1)
# the target function
plt.plot([x1,x2],[y1,y2],linewidth=1)
# the square phase space
plt.plot([-1,1],[1,1]); plt.plot([1,1],[1,-1]);
plt.plot([1,-1],[-1,-1]);plt.plot([-1,-1],[-1,1]);
# plot the traning points
for i in range(1,len(xn)):
    if zn[i]>0:
        plt.scatter(xn[i], yn[i], s=30, c='b', marker="+")
    else:
        plt.scatter(xn[i], yn[i], s=30, c='r', marker="o")
# axes ranges
plt.ylim([-1.3,1.3])
plt.xlim([-1.3,1.3])


# ## Perceptron Learning Algorithm

# In[177]:

# re-generate random training points
number_sampling=10
xn=[]; yn=[]; zn=[];
for i in range(1,number_sampling):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    xn.append(x)
    yn.append(y)
    # classify using zn depending on whether they fall above or below the line
    if y>(y1+(x-x1)*(y2-y1)/(x2-x1)):
        zn.append(+1)
    else:
        zn.append(-1)


# In[183]:

nruns=10000; # number of runs, times to iterate the PLA
x0=1;
w = [0,0,0] # [w0=b, w2 for x, w3 for y]
for t in range(1,nruns):
    i = random.randint(0,len(xn)-1)
    # use cmp to simulate the sign function
    hyp = cmp(w[0]*1. + w[1]*xn[i] + w[2]*yn[i], 0)
    trg = target(xn[i],yn[i])
    if not cmp(hyp, trg) == 0 :
        w[0] = w[0] + trg*x0
        w[1] = w[1] + trg*xn[i]
        w[2] = w[2] + trg*yn[i]
        if trg*xn[i]/w[1] < 0.01:
            print 'converged at iteration',t

#fig, ax1 = plt.subplots(1, 1)
# the target function
plt.plot([x1,x2],[y1,y2],linewidth=1)
# the square phase space
plt.plot([-1,1],[1,1]); plt.plot([1,1],[1,-1]);
plt.plot([1,-1],[-1,-1]);plt.plot([-1,-1],[-1,1]);
# plot the traning points
for i in range(1,len(xn)):
    if zn[i]>0:
        plt.scatter(xn[i], yn[i], s=30, c='b', marker="+")
    else:
        plt.scatter(xn[i], yn[i], s=30, c='r', marker="o")
# hypothesis
xx = np.linspace(-1,1,100)
yy = -(w[0]+w[1]*xx)/w[2]
plt.plot(xx,yy)
# axes ranges
plt.ylim([-1.3,1.3])
plt.xlim([-1.3,1.3])


# In[ ]:



