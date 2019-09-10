import os 

from ROOT import TH1F, TH2F 

def Set1DHistParameters(h1, parameterList):
    ## the parameter list should have: 
    ## Y minimum, Y maximum, 
    ## Marker Style, Marker Size 
    ## Line Width, Line color 
    ## more can be added 
    
    if len(parameterList) >= 2 :
        h1.SetMinimum(parameterList[0])
        h1.SetMaximum(parameterList[1])
    if len(parameterList) >= 4 :
        h1.SetMarkerStyle(parameterList[2])
        h1.SetMarkerSize(parameterList[3])
        
    if len(parameterList) >= 6 :
        h1.SetLineWidth(parameterList[4])
        h1.SetLineColor(parameterList[5])

    return h1
    
    
