# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 23:56:40 2021

@author: MRDV
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy
import importlib
from scipy.stats import skew,kurtosis,chi2

print("Primer Codigo")

#simulating random variables
df=5
lam=2
dist_name= 'exponential'
if dist_name == 'normal':
    x=np.random.standard_normal(10**5)
elif dist_name == 'exponential':
    x=np.random.exponential(lam,10**5)
elif dist_name == 'uniform':
    x=np.random.uniform(0,2,10**5)
elif dist_name == 'student':
    x=np.random.standard_t(df,10**5)


#plot histograms (run all at time)
plt.figure()
plt.hist(x,bins=100)
plt.title('Histograma normal'+str(df))
plt.show()

#test of edition in GITHUB
