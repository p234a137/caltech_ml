__author__ = 'dkcira'
import random
import numpy as np
import matplotlib.pyplot as plt

def pla(nr_training, nr_iterations):
    # points where target function crosses the axes x1 and x2
    c1=random.uniform(-1,1);
    c2=random.uniform(-1,1);
    def target_function(x1,x2):
        if x2 > c2*(c1-x1)/c1: # point is above the line
            return +1;
        else:
            return -1;



    return
