# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:09:09 2021

@author: trupti
"""


def anagram():
    x=str(input("Enter frst string: "))
    y=str(input("Enter second string: "))
    if len(x)==len(y):
        print("True")
    else:
        print("False")
        
anagram()        