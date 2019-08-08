import os 
import sys 
import optparse

import numpy
import pandas
import math
from root_pandas import read_root
from pandas import  DataFrame
from pandas import Series 
from ROOT import TLorentzVector, TMath
import numpy 


def logical_AND(all_booleans):
    return (len(all_booleans) == all_booleans.count(True))


def logical_OR(all_booleans):
    return  (all_booleans.count(True) > 0)


def logical_AND_List2(a, b):
    return (numpy.array(a) & numpy.array(b))


def logical_AND_List3(a, b, c):
    return   ( logical_AND_List2( logical_AND_List2(a,b), c) )


def logical_AND_List4(a, b, c, d):
    return logical_AND_List2 (   logical_AND_List2(a,b) , logical_AND_List2(c,d) )

def logical_AND_List5(a, b, c, d, e):
    return logical_AND_List2( logical_AND_List3(a, b, c), logical_AND_List2(d, e)  )

def logical_AND_List6(a, b, c, d, e, f):
    return logical_AND_List2( logical_AND_List3(a, b, c), logical_AND_List3(d, e, f)  )

def logical_AND_List7(a, b, c, d, e, f, g):
    return logical_AND_List3( logical_AND_List3(a, b, c), logical_AND_List3(d, e, f), g  )


def WhereIsTrue(testList_, nCut_=0):
    pass_index=[]
    if len(testList_)>=nCut_:
        pass_index = numpy.where(testList_)[0]
    return pass_index




