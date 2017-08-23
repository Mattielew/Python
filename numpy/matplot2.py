#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: matplot22.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: Demonstration of plotting graphics 
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED:  
#     REVISION: ---
#===============================================================================


import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', linewidth=2.0)
plt.show()

# -- = dashes s = square and ^ = triangles. I know it's screwy...don't look at me I didn't invent it.
