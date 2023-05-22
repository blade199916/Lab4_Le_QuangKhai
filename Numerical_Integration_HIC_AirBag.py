# -*- coding: utf-8 -*-
"""


@author: Quang Khai Le
Title: Airbag Simulation
"""
#plot the deceleration plot over time to find out the best fit in order to help mechanical design the airbag simulation 
import math as m #import library 
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integ
from scipy import integrate
#pick the number of acceleration
D = [22,35,41,57,65]
#domain range
for d in D:
    #Without Airbag equation
    WOA = lambda t:0.1*d*(((1/d)*(16400/(((t-68)**2)+400)+1480/((t-93)**2+18)))**2.5)
    #With Airbag equation
    WA = lambda t:0.1*d*(((1/d)*(22000/(((t-74)**2)+500)))**2.5)
    integ.quad(WOA,0,4)
    integ.quad(WA,0,100)
    
xv = [t for t in range(140)]
for d in D:
    yv1 = [integ.quad(WOA, t, t + d) for t in xv]
    plt.legend(['22','35','41','57','65'])
    plt.xlabel('Deceleration')
    plt.ylabel('Time')
    plt.plot(xv, yv1)
#Show two plotin the result
plt.show()
for d in D:
    yv2 = [integ.quad(WA, t, t + d) for t in xv ]
    plt.legend(['22','35','41','57','65'])
    plt.xlabel('Time')
    plt.ylabel('Deceleration')
    plt.plot(xv,yv2)