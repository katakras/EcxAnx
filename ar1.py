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
    
  
    variable =[]
    s = y_o
    for i in range(N):
       epsilon = random.randint(0,1)
       y_i= alpha + beta*s + epsilon
       
       variable  = np.variable.append(y_i)
      
       s = y_i

    return variable


simulate  = eleni(40,2,2,100)

print(simulate)
  
     
    
            