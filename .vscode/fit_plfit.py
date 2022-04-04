import plfit
import matplotlib.pyplot as plt
from numpy.random import rand,seed

# generate a power law using the "inverse" power-law generator code
X=plfit.plexp_inv(rand(1000),1,2.5)
# print(X)
# use the numpy version to fit (usefortran=False is only needed if you installed the fortran version)
myplfit=plfit.plfit(X,usefortran=False)
# output should look something like this:
# PYTHON plfit executed in 0.201362 seconds
# xmin: 0.621393 n(>xmin): 263 alpha: 2.39465 +/- 0.0859979   Log-Likelihood: -238.959   ks: 0.0278864 p(ks): 0.986695

# generate some plots
from pylab import *
figure(1)
myplfit.plotpdf()

# figure(2)
# myplfit.plotcdf()

plt.show()