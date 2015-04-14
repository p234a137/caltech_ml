
# coding: utf-8

# # Perceptron example improved

# In[13]:

#get_ipython().magic(u'pylab inline')
import random
#import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt


# In[2]:

# the perceptron learning algorithm
def pla(number_iterations,number_training,do_plot):
    # target function
    x1=random.uniform(-1,1); y1=-1; #y1=random.uniform(-1,1);
    x2=random.uniform(-1,1); y2=+1; #y2=random.uniform(-1,1);
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
            #print "PLA for ",number_training," points converged after ",iter," iterations"
            #################################
            if(do_plot):
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
                    ##########################
            return [iter, w[0], w[1], w[2], x1, y1, x2, y2]
            #break; # stop iterations
    return [-1, w[0], w[1], w[2], x1, y1, x2, y2];


# In[57]:

number_runs=1000
number_training=100
number_max_iterations=100000
sum_iter=0
sum_probs=0
for irun in range(1,number_runs):
    if irun==number_runs-1 :
        [iter, w0, w1, w2, x1, y1, x2, y2] = pla(number_max_iterations,number_training, True)
    else:
        [iter, w0, w1, w2, x1, y1, x2, y2] = pla(number_max_iterations,number_training, False)
    # sum up iterations to use for calculating average
    if iter > -1:
        sum_iter += iter
    else:
        print iter
    # calculate P[ hyp != trg ]
    def fun_trg(x):
        return y1+(x-x1)*(y2-y1)/(x2-x1)
    def fun_hyp(x):
        return -(w0+w1*x)/w2
    the_integral = 0.;
    n_sampling=1000
    n_agreement=0
    xsampling=np.random.uniform(-1,1,n_sampling)
    ysampling=np.random.uniform(-1,1,n_sampling)
    for s in range(0,n_sampling-1):
        #if irun==number_runs -1:
        #    print "sampling",s, xsampling[s], ysampling[s], fun_trg(xsampling[s]), fun_hyp(xsampling[s])
        if ysampling[s] > fun_trg(xsampling[s]) and ysampling[s] > fun_hyp(xsampling[s]):
            n_agreement = n_agreement + 1
            #if irun==number_runs -1:
            #    print "yes +"
        if ysampling[s] < fun_trg(xsampling[s]) and ysampling[s] < fun_hyp(xsampling[s]):
            n_agreement = n_agreement + 1
            #if irun==number_runs-1:
            #    print "yes -"
    # add disagreement probabilities in order to calculate average
    #print "disagreement probability for run",irun," is", float(n_sampling-n_agreement)/n_sampling
    #print n_agreement, n_sampling
    #if irun==number_runs-1 :
    #    print "disagreement probability for run",irun," is", float(n_sampling-n_agreement)/n_sampling, n_agreement, n_sampling
    sum_probs = sum_probs + float(n_sampling-n_agreement)/n_sampling

"""
    # integrate abs(diff) of functions in order to calculate probability
    nr_slices = 1000
    slice_width=2./nr_slices
    for islice in range(1,nr_slices):
        f1=fun_trg(-1+islice*slice_width)
        f2=fun_hyp(-1+islice*slice_width)
        if f1>1:
            f1=1.
        if f2>1:
            f2=1.
        if f1<-1:
            f1=-1.
        if f2<-1:
            f2=-1.
        if (iter>-1):
            the_integral = slice_width*abs(f1-f2)
"""

# average nr of iterations
print "number of iterations to conversion =",sum_iter / number_runs
#print the_integral/4.
print "disagreement probability =",sum_probs / number_runs


# In[ ]:



