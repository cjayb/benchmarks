import numpy
import numpy.fft as fft
numpy.use_fastnumpy = True
import time
#from scipy.fftpack import fft
import mkl

print 'Intel MKL version:', mkl.get_version_string()
print 'Intel cpu_clocks:', mkl.get_cpu_clocks()
print 'Intel cpu_frequency:', mkl.get_cpu_frequency()
#print 'Intel MKL, freeing buffer memory:', mkl.thread_free_buffers()

print 'max Intel threads:', mkl.get_max_threads()

mkl.set_num_threads(2)

N = 2**16

print 'using numpy', numpy.__version__
a = numpy.random.rand(2, N)
print a.shape, 'items'
t0 = time.clock()
for i in range(100):
    continue
base = time.clock()-t0
fftn = fft.fftn
t0 = time.clock()
for i in range(100):
    r = fftn(a, (N,), (1,))
print 'simple loop', time.clock()-t0-base

