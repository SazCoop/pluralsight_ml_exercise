# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Helper functions
def check_unique(data, primary_key):
    if(len(data[primary_key].unique())< len(data)):
        return(print("Duplicate Entries"))
        
def count_unique(data):
    print("Length of Dataset : %s" % len(data))
    for col in data.columns:
        len_u = data[col].nunique()
        print("Length of Column %s Unqiue Entries %s" %(col, len_u))        

