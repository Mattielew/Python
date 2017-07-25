#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: nba.py
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
#      CREATED: Tue Jul 25 10:28:47 PDT 2017
#     REVISION: ---
#===============================================================================

import requests

r = requests.get('')

#Types of response data 
p = r.json()
#p =r.text

print(p)
head = r.headers
print(head)


#import requests
##
#r = requests.get('http://stats.nba.com/stats/commonplayerinfo?LeagueID=00&PlayerID=201566&SeasonType=Regular+Season/')
##
### request the URL and parse the JSON
##request.raise_for_status() # raise exception if invalid response
#shots = r.text
#print(shots)
### do whatever we want with the shots data
##print(shots)
