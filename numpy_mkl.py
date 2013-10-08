"""
From: http://dpinte.wordpress.com/2010/01/15/numpy-performance-improvement-with-the-mkl/
Date: 08 Oct 2013
Benchmark script to be used to evaluate the performance improvement of the MKL
"""
 
import os
import sys
import timeit
 
import numpy
from numpy.random import random
 
def test_eigenvalue():
    """
    Test eigen value computation of a matrix
    """
    i = 500
    data = random((i,i))
    result = numpy.linalg.eig(data)
 
def test_svd():
    """
    Test single value decomposition of a matrix
    """
    i = 1000
    data = random((i,i))
    result = numpy.linalg.svd(data)
    #result = numpy.linalg.svd(data, full_matrices=False)
 
def test_inv():
    """
    Test matrix inversion
    """
    i = 1000
    data = random((i,i))
    result = numpy.linalg.inv(data)
 
def test_det():
    """
    Test the computation of the matrix determinant
    """
    i = 1000
    data = random((i,i))
    result = numpy.linalg.det(data)
 
def test_dot():
    """
    Test the dot product
    """
    i = 1000
    a = random((i, i))
    b = numpy.linalg.inv(a)
    result = numpy.dot(a, b) - numpy.eye(i)
 
# Tests to start. 
# Each key is a function, the item is list of thread counts to use
threads_range = range(1,12,3)
tests = (test_eigenvalue, test_svd, test_inv, test_det, test_dot)
 
# Setting the following environment variable in the shell executing the script allows
# you limit the maximal number threads used for computation
THREADS_LIMIT_ENV = 'OMP_NUM_THREADS'
 
def start_benchmark():
    print "Benchmark starting timing with numpy %s\nVersion: %s" % (numpy.__version__, sys.version)

    for cur_threads in threads_range:
        header_set = False
        os.environ[THREADS_LIMIT_ENV] = '%d' % cur_threads
        print "Maximum number of threads used for computation is : %s" % os.environ[THREADS_LIMIT_ENV]
        print ("-" * 80)

        header_str = "%20s" % "Function"
        header_str += ' - N=%02d [ms]' % cur_threads

        for fun in tests:

            result_str = "%20s" % fun.__name__
            t = timeit.Timer(stmt="%s()" % fun.__name__, setup="from __main__ import %s" % fun.__name__)
            res = t.repeat(repeat=3, number=1)
            timing =  1000.0 * sum(res)/len(res)
        
            result_str += ' - %9.1f' % timing
                 
            if not header_set is True:
                print header_str
                header_set = True
        
            print result_str    
        
        
if __name__ == '__main__':
    start_benchmark()