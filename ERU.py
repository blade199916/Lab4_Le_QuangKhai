# -*- coding: utf-8 -*-
"""

@author: lqkvn
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def ERU1(bed,t):
   # constants
   no_bed =200;
   no_bed_ERU =10;
   # people coming rate (person/hour)
   qin = 10  
   # people moving to ICU rate (person/hour)
   # free bed of ERU (bed/hour)
   c1= 0.4
   # nedded bed of ICU (bed/hour)
   c2= 0.6 
   # outflow happens condition
   qout1 = c1 * bed[0]**0.5
   qout2 = c2 * bed[1]**0.5
   # differential equations
   dhdt1 = (qin   - qout1) / no_bed
   dhdt2 = (qout1 - qout2) / no_bed_ERU
   # overflow conditions to avoid
   if bed[0]>=1 and dhdt1>=0:
       dhdt1 = 0
   if bed[1]>=1 and dhdt2>=0:
       dhdt2 = 0
   dhdt = [dhdt1,dhdt2]
   return dhdt

# integrate those above equations
t = np.linspace(0,10) # times to report solution
bed0 = [0,0]            # initial conditions for height
y = odeint(ERU1,bed0,t) # integrate

# showing the plot results
plt.figure(1)
plt.plot(t,y[:,0],'r')
plt.plot(t,y[:,1],'y--')
plt.xlabel('Time (hrs)')
plt.ylabel('Number of bed used')
plt.legend(['Number of used bed in ERU','Number of used bed in ICU'])
plt.show()

# ERU saturated 

def ERU2(doctor,t):
   # constants

   no_doctor = 30;
   no_doctor_ERU=10;
   # doctor coming rate (person/hour)
   qin = 4  
   # doctor moving to ICU rate (person/hour)
   c1= 0.6
   # doctor leaving ICU (doctor/hour)
   c2= 0.4 
   # outflow
   qout1 = c1 * doctor[0]**0.5
   qout2 = c2 * doctor[1]**0.5
   # differential equations
   dhdt1 = (qin   - qout1) / no_doctor
   dhdt2 = (qout1 - qout2) / no_doctor_ERU
   # overflow conditions
   if doctor[0]>=1 and dhdt1>=0:
       dhdt1 = 0
   if doctor[1]>=1 and dhdt2>=0:
       dhdt2 = 0
   dhdt = [dhdt1,dhdt2]
   return dhdt

# integrate the equations
t = np.linspace(0,15) # times to report solution
doctor0 = [0,0]            # initial conditions for height
y = odeint(ERU2,doctor0,t) # integrate


# showing the plot results
plt.figure(2)
plt.plot(t,y[:,0],'r')
plt.plot(t,y[:,1],'y--')
plt.xlabel('Time (hrs)')
plt.ylabel('Number of doctors')
plt.legend(['Number of doctor in ERU','Total of doctor in ICU'])
plt.show()


def ERU3(EMSdevice,t):
   # constants

   no_EMSdevice = 90;
   no_EMSdevice_ERU=10;
   # doctor coming rate (person/hour)
   qin = 6  
   # doctor moving to ICU rate (person/hour)
   c1= 0.8
   # doctor leaving ICU (doctor/hour)
   c2= 0.5 
   # outflow
   qout1 = c1 * EMSdevice[0]**0.5
   qout2 = c2 * EMSdevice[1]**0.5
   # differential equations
   dhdt1 = (qin   - qout1) / no_EMSdevice
   dhdt2 = (qout1 - qout2) / no_EMSdevice_ERU
   # overflow conditions
   if EMSdevice[0]>=1 and dhdt1>=0:
       dhdt1 = 0
   if EMSdevice[1]>=1 and dhdt2>=0:
       dhdt2 = 0
   dhdt = [dhdt1,dhdt2]
   return dhdt

# integrate the equations
t = np.linspace(0,15) # times to report solution
EMSdevice0 = [0,0]            # initial conditions for height
y = odeint(ERU3,EMSdevice0,t) # integrate


# showing the plot results
plt.figure(2)
plt.plot(t,y[:,0],'r')
plt.plot(t,y[:,1],'y--')
plt.xlabel('Time (hrs)')
plt.ylabel('Number of available EMS device')
plt.legend(['Number of available EMS device in ERU','Total of EMS device in ICU'])
plt.show()