__author__ = 'dkcira'
import random
import numpy as np
import matplotlib.pyplot as plt


def target_function(x1,x2, c0, c1, c2):
    """ define the target function """
    if x2 > -c0+(c2+c0)*(c1-x1)/(c1+c0): # point is above the line
        return +1
    else:
        return -1


def pla(nr_training, nr_iterations, do_plot):
    """ run the perceptron learning algorithm
    :param nr_training: number of training points
    :param nr_iterations: number of iterations
    :param do_plot: whether to do an illustrative plot of points above and below target
    :return: did it converge, nr of iterations until converged, weights array
    """
    c0 = -1.; # square between -c0, c0 in 2 dimensions
    c1=random.uniform(-c0,c0); # points where target function crosses the axes x1 and x2
    c2=random.uniform(-c0,c0)
    # generate training points
    xx1 = [random.uniform(-c0,c0) for i in range(nr_training)]
    xx2 = [random.uniform(-c0,c0) for i in range(nr_training)]
    yy_true=[]; # generate labels according to the target function
    for i in range(len(xx1)):
        yy_true.append(target_function(xx1[i],xx2[i], c0, c1, c2))

    if do_plot:
        # create scatter plot to check that labels are properly assigned according to the target function
        plt.scatter(xx1,xx2,s=200, c=yy_true, marker=(5,1))
        plt.plot([c1, -c0], [-c0, c2], 'k-', lw=1) # plot the target function
        # axes ranges
        plt.ylim([-1.01,1.01])
        plt.xlim([-1.01,1.01])
        plt.title('target function and true labels of the classification')
        plt.savefig('perceptron_new1.png')

    # run the perceptron algorithm
    x0 = 1; # constant term
    w=[0,0,0]; # weights, w[0] -> constant term, w[1] -> x1, w[2] -> x2
    for iteration in range(1,nr_iterations):
        not_converged = []
        for j in range(0,len(xx1)):
            hyp = cmp(w[0]*1. + w[1]*xx1[j] + w[2]*xx2[j], 0); # hypothesis
            if hyp != yy_true[j]: # if hypothesis does not match true label, change weights
                not_converged.append(j)
        if len(not_converged) > 0:
            i = random.choice(not_converged); # pick random element from the non-converged
            w[0] = w[0] + yy_true[i]*x0
            w[1] = w[1] + yy_true[i]*xx1[i]
            w[2] = w[2] + yy_true[i]*xx2[i]
        else:
            return [1, iteration, w]
    return [-1, iteration, w]



if __name__ == '__main__':
    nr_training=10;
    nr_iterations=100;
    nr_runs = 1000
    # print "nr_training", nr_training
    # print "nr_iterations", nr_iterations
    # print "nr_runs", nr_runs
    iterations = []
    for r in range(1,nr_runs+1):
        [did_it_converge, iteration, weights] = pla(nr_training,nr_iterations, False);
        if did_it_converge == 1:
            iterations.append(iteration)
        # print r, "did it converge? ", did_it_converge, "iteration", iteration, "weights", weights
    print "iterations mean, median", np.mean(iterations), np.median(iterations)
