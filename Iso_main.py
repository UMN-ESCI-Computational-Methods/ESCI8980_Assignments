#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Function ("main") which gives specified outputs of the IsoFilter class. 

Created by Nick Wang and Julia Nissen, 2017

"""

import os
import IsoFilter

def main():
    print("Standard U_filter")
    filename = raw_input("Enter the source file name: ")
    columnletter = raw_input("What column are we looking at? ")
    
    i = 1
    validEntry = False
    while i<3:
        while not validEntry:
            try:
                wb = IsoFilter.IsoFilter(str(filename),str(columnletter))
                validEntry = True     
            except IOError as e:
                print(os.strerror(e.errno))
                filename = raw_input("No such file exist. Enter the correct source file name: ")
        i += 1
    wb.getMean()
    wb.getStanddev()
    wb.getCounts()
    wb.theFilter()
    print(wb)
    
main()
            

       