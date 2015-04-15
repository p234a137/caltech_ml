__author__ = 'dkcira'
import random
import numpy as np
import matplotlib.pyplot as plt

def pla(nr_training, nr_iterations):
    # points where target function crosses the axes x1 and x2
    c0=1.;
    c1=random.uniform(-c0,c0);
    c2=random.uniform(-c0,c0);
    def target_function(x1,x2):
        if x2 > -c0+(c2+c0)*(c1-x1)/(c1+c0): # point is above the line
            return +1;
        else:
            return -1;
    xx1 = [random.uniform(-c0,c0) for i in range(100)]
    xx2 = [random.uniform(-c0,c0) for i in range(100)]
    yy=[];
    for i in range(len(xx1)):
        yy.append(target_function(xx1[i],xx2[i]))
    plt.scatter(xx1,xx2,s=100, c=yy, marker=(5,0))
    print "c1=",c1, " c2=",c2;
    plt.plot([c1, -c0], [-c0, c2], 'k-', lw=2) # plot the target function
    # axes ranges
    plt.ylim([-1.01,1.01])
    plt.xlim([-1.01,1.01])
    plt.title('target function and real values of the classification')
    plt.savefig('perceptron_new1.png')


if __name__ == '__main__':
    pla(10,1000);