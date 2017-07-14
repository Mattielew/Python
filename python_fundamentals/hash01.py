#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: hash01.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: hashes 
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
#     REVISION: ---
#===============================================================================


import hashlib

print(hashlib.algorithms_available)
hash_object =  hashlib.md5(b"Hello world")


print(hash_object)


hash_object = hashlib.sha1(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)


