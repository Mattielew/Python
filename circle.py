#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: circle.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: 
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: Mon Jul 10 11:47:35 PDT 2017
#     REVISION: ---
#===============================================================================

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.0, 1.0, 100)
y = np.linspace(-1.0, 1.0, 100)
X, Y = np.meshgrid(x,y)
F = X**2 + Y**2 - 0.6
plt.contour(X,Y,F,[0])
plt.show()

