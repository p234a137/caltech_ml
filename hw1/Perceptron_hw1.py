
# coding: utf-8

# # Perceptron exercise from homework 1, April 8, 2013

# In[15]:

#get_ipython().magic(u'pylab inline')
import random
import numpy as np


# In[31]:

number_runs=20
number_iterations=1000
number_training=10

iterations_to_convergence=[];
for run in range(0,number_runs):
    # target function
    x1=random.uniform(-1,1); y1=random.uniform(-1,1);
    x2=random.uniform(-1,1); y2=random.uniform(-1,1);
    # classifies points as +1 or -1 depending on whether they are above or below the line
    def target(x,y):
        if y>=(y1+(x-x1)*(y2-y1)/(x2-x1)):
            return 1
        else:
            return -1
    # training points
    xn=[]; yn=[]; zn=[];
    for i in range(1,number_training):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        xn.append(x)
        yn.append(y)
        # classify using zn depending on whether they fall above or below the line
        if y>(y1+(x-x1)*(y2-y1)/(x2-x1)):
            zn.append(+1)
        else:
            zn.append(-1)
    # iterate PLA until it converges
    x0=1
    w = [0,0,0] # [w0=b, w1 for x, w2 for y]
    for iter in range(1,number_iterations):
        i = random.randint(0,len(xn)-1); # pick randomly a point from xn
        # use cmp to simulate the sign function
        hyp = cmp(w[0]*1. + w[1]*xn[i] + w[2]*yn[i], 0); # hypothesis
        trg = target(xn[i],yn[i]); # target function
        if not cmp(hyp, trg) == 0 :
            w[0] = w[0] + trg*x0
            w[1] = w[1] + trg*xn[i]
            w[2] = w[2] + trg*yn[i]
        #compare two arrays to check whether algorithm converged
        converged = False
        nr_converged = 0;
        for j in range(0,len(xn)):
            hyp = cmp(w[0]*1. + w[1]*xn[j] + w[2]*yn[j], 0); # hypothesis
            trg = target(xn[j],yn[j]); # target function
            if cmp(hyp, trg) == 0:
                nr_converged = nr_converged+1
        if nr_converged == len(xn):
            converged= True
            iterations_to_convergence.append(iter);
            print "PLA for ",number_training," points converged after ",iter," iterations"
            break; # stop iterations

# In[ ]:
print("iterations mean, median, rms", np.mean(iterations_to_convergence), np.median(iterations_to_convergence), np.sqrt(np.std(iterations_to_convergence)));
