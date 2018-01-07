#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 13:07:32 2018

@author: macbookpro
"""

import numpy as np
import pandas 
import random

y_o =50

beta = 0.2

alpha = 2

N = 3



 

def eleni(y_o, beta,alpha, N):
    
  
    y =[y_o]

    for i in range(N):
       epsilon = np.random.normal()
       y_i= alpha + beta*y[-1] + epsilon
       
       y.append(y_i)

    return y


np.random.seed(0)
simulate  = eleni(40,beta,alpha,100)

print(simulate)
print(simulate[-1])
     
    
            