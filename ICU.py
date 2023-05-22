# -*- coding: utf-8 -*-
"""
Created on Sun May 21 15:25:55 2023

@author: lqkvn
"""

# -*- coding: utf-8 -*-


#ICU saturated
#import necessary packages

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#function ICU1 for doctorcoming and leave

def ICU1(doctor,t):
    # doctorcoming at rate 0.9 and leaving at rate 0.3
    rate_come = 0.9
    rate_leave = 0.3
    totaldoctor= 100 # Total doctor
    ICUdoctor= 25 # Total ICU doctor

    qin = 5  # doctorcoming everyday
    qout1 = rate_come * doctor[0]*0.5 # Leaving hospital per hour
    qout2 = rate_leave * doctor[1]*0.5 #
    
    #calculate number of doctorcoming and leaving ICU
    dhdt1 = (qin - qout1) / totaldoctor
    dhdt2 = (qin - qout2) / totaldoctor
    dhdt3 = (qout1 - qout2) / ICUdoctor
   # Overflow conditions
    if doctor[0] >= 1 or (dhdt1 >= 1 or dhdt2 >= 1):
       dhdt1 = 0
       dhdt2 = 0
    if doctor[1] >= 1 and dhdt3 >= 0:
       dhdt3 = 0
    ICU1 = [dhdt1,dhdt3]
    return ICU1
# Integrate the equations
t = np.linspace(0,100) 
doctor0 = [0,0]            # Set height to initial condition
y = odeint(ICU1,doctor0,t) # Integration
# plot results
plt.figure(1)
plt.plot(t,y[:,0],'b-')
plt.plot(t,y[:,1],'r--')
plt.xlabel('Time')
plt.ylabel('Ratio of doctor')
plt.legend(['ERU doctor','ICU doctor'])
plt.title('Scenario 3: ICU is saturated')
plt.show()

#function ICU2: both saturated
def ICU2(eq,t):
    # equipments coming to ICU at rate 0.7 and leaving at rate 0.1
    rate_come = 0.7
    rate_leave = 0.1
    totaleq = 50 # Total equipments 
    ICUeq = 15 # Total ICU equipments
    
    # Inflow
    qin = 10  # Equipment gets in ICU/day
    
    # Outflow: calculate number of equipment coming and leaving ICU/days
    qout1 = rate_come * eq[0]*0.5 # Leaving hospital per hour
    qout2 = rate_leave * eq[1]*0.5 #
    
    #calculate number of equipment coming and leaving ICU
    dhdt1 = (qin - qout1) / totaleq
    dhdt2 = (qin - qout2) / totaleq
    dhdt3 = (qout1 - qout2) / ICUeq
   # Overflow conditions
    if eq[0] >= 1 or (dhdt1 >= 1 or dhdt2 >= 1):
       dhdt1 = 0
       dhdt2 = 0
    if eq[1] >= 1 and dhdt3 >= 0:
       dhdt3 = 0
    ICU2 = [dhdt1,dhdt3]
    return ICU2
# Integrate the equations
t = np.linspace(0,100) 
eq0 = [0,0]            # Set height to initial condition
y = odeint(ICU2,eq0,t) # Integration
# plot results
plt.figure(2)
plt.plot(t,y[:,0],'b-')
plt.plot(t,y[:,1],'r--')
plt.xlabel('Time')
plt.ylabel('Ratio of equipment')
plt.legend(['ERU equipment','ICU equipment'])
plt.title('Scenario 4: both ERU and ICU are saturated')
plt.show()