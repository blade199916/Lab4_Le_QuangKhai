# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:42:21 2023
@author: Quang Khai Le
"""
#import libraries, including ahkab
import numpy as np
from matplotlib.pyplot import *

#Calling "inline" backend of pyplot and set the size of the figure
get_ipython().run_line_magic('pylab', 'inline')
figsize = (25, 12)
import ahkab

print("We're using ahkab %s" % ahkab.__version__)

# Create a new circuit object titled 'RLC bandpass' (bpf for Band-Pass Filter)
bpf = ahkab.Circuit('RLC bandpass filter')

# Add inductors, capacitors, resistors, and the input source to the circuit
bpf.add_inductor('L1', 'in', 'n1', 2e-6)
bpf.add_capacitor('C1', 'n1', 'n2', 2.1e-11)
bpf.add_resistor('R1', 'n2', bpf.gnd, 20e3)

bpf.add_resistor('R2', 'out', bpf.gnd, 30e3)
bpf.add_inductor('L2', 'out', 'n2', 2e-6)
bpf.add_capacitor('C2', 'out', bpf.gnd, 2.1e-11)

# Add a voltage source V1 with start node "in" and end node "gnd"
bpf.add_vsource('V1', 'in', bpf.gnd, dc_value=1, ac_value=1)

# Import sympy and initialize printing
import sympy
sympy.init_printing()

# Assign the AC analysis settings
aca = ahkab.new_ac(start=1e7, stop=6e7, points=5e3, x0=None)
rac = ahkab.run(bpf, aca)['ac']

symba = ahkab.new_symbolic(source='V1')
rs, tfs = ahkab.run(bpf, symba)['symbolic']
print("numpy path")
# Print the symbolic analysis results stored in "rs"
print(rs)

# Print transfer function following the results stored in "tfs" of symbolic analysis
print(tfs)

# Print the values from the transfer function
Hs = tfs['VOUT/V1']['gain']
Hs
print('Hs=', Hs)
