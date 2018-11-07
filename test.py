#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 00:01:50 2018

@author: thomas
"""

# Python version
import YearlyDatatype
import MonthlyDatatype

year = YearlyDatatype.YearlyDatatype(1995)

tup = year.returnDetails()

print(tup[1])