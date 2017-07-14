#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: nedtx.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: graphing and social science? 
#
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED:  
#     REVISION: Wed Jun 21 08:15:41 PDT 2017
#===============================================================================

# -*- coding: iso-8859-15 -*-
#This is sgoing to be an example of the netx utility 
#we are going to be establishing the graphing and tehunderstanding of social
#science interpretation. This should be interesting :) 

import networkx as nx

# you are ggoing  to create an emptu grpah with no edges and no nodes
G=nx.Graph()

G.add_nodes_from([1,10])
G.add_edge([2,3])
print(G)

