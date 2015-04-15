__author__ = 'dkcira'
import random
import numpy as np
import matplotlib.pyplot as plt

def pla(nr_training, nr_iterations):

    # defome the target function, generate the points
    # points where target function crosses the axes x1 and x2
    c0=1.;
    c1=random.uniform(-c0,c0);
    c2=random.uniform(-c0,c0);
    def target_function(x1,x2):
        if x2 > -c0+(c2+c0)*(c1-x1)/(c1+c0): # point is above the line
            return +1;
        else:
            return -1;
    xx1 = [random.uniform(-c0,c0) for i in range(nr_training)]
    xx2 = [random.uniform(-c0,c0) for i in range(nr_training)]
    yy_true=[];
    for i in range(len(xx1)):
        yy_true.append(target_function(xx1[i],xx2[i]))
    plt.scatter(xx1,xx2,s=100, c=yy_true, marker=(5,0))
    #print "c1=",c1, " c2=",c2;
    plt.plot([c1, -c0], [-c0, c2], 'k-', lw=1) # plot the target function
    # axes ranges
    plt.ylim([-1.01,1.01])
    plt.xlim([-1.01,1.01])
    plt.title('target function and true labels of the classification')
    plt.savefig('perceptron_new1.png')

    # run the perceptron
    x0 = 1;
    w=[0,0,0]; # w[0] -> constant term, w[1] -> x1, w[2] -> x2
    for iteration in range(1,nr_iterations):
        # pick randomly a point from the arrays
        j = random.randint(0,len(xx1)-1);
        hyp = cmp(w[0]*1. + w[1]*xx1[j] + w[2]*xx2[j], 0); # hypothesis
        if hyp != yy_true[j]: # if hypothesis does not match true label, change weights
            w[0] = w[0] + yy_true[j]*x0
            w[1] = w[1] + yy_true[j]*xx1[j]
            w[2] = w[2] + yy_true[j]*x2[j]



if __name__ == '__main__':
    nr_training=10;
    nr_iterations=100;
    pla(nr_training,nr_iterations);