import os, sys
import numpy as np

#//--------------------------------------------------------------------------------------

def fitfun(x, a, b, c):
    return a * np.exp(-b * x) + c

def getEWKW( pt):

    weight = 1.0
    if pt < 170: weight  = 0.96648144722
    elif (pt >= 170.0 and pt <  200.0): weght  = 0.958350896835
    elif (pt >= 200.0 and pt < 230.0):  weight = 0.94851320982
    elif (pt >= 230.0 and pt < 260.0):   weight = 0.938303768635
    elif (pt >= 260.0 and pt < 290.0):  weight =  0.929393827915
    elif (pt >= 290.0 and pt < 320.0):  weight =  0.919687867165
    elif (pt >= 320.0 and pt < 350.0):  weight =  0.910424590111
    elif (pt >= 350.0 and pt < 390.0):  weight =  0.900288462639
    elif (pt >= 390.0 and pt < 430.0):  weight =  0.889121949673
    elif (pt >= 430.0 and pt < 470.0):  weight =  0.877254605293
    elif (pt >= 470.0 and pt < 510.0):  weight =  0.866529941559
    elif (pt >= 510.0 and pt < 550.0):  weight =   0.856031835079
    elif (pt >= 550.0 and pt < 590.0):  weight =   0.845360279083
    elif (pt >= 590.0 and pt < 640.0):  weight =   0.834675312042
    elif (pt >= 640.0 and pt < 690.0):  weight =   0.822288095951
    elif (pt >= 690.0 and pt < 740.0):  weight =   0.810778558254
    elif (pt >= 740.0 and pt < 790.0):  weight =   0.799689173698
    elif (pt >= 790.0 and pt < 840.0):  weight =   0.788566112518
    elif (pt >= 840.0 and pt < 900.0):  weight =   0.777413368225
    elif (pt >= 900.0 and pt < 960.0):  weight =   0.765404522419
    elif (pt >= 960.0 and pt < 1020.0): weight =    0.753710508347
    elif (pt >= 1020.0 and pt < 1090.0): weight =    0.74226218462
    elif (pt >= 1090.0 and pt < 1160.0): weight =    0.729250490665
    elif (pt >= 1160.0):  weight =   0.716423392296

    return weight


#//--------------------------------------------------------------------------------------
def getEWKZ(  pt):

    weight = 1.0
    if (pt <  170.0): weight = 0.970592081547
    elif (pt >= 170.0  and pt <  200.0): weight =    0.964424192905
    elif (pt >= 200.0  and pt <  230.0): weight =    0.956695139408
    elif (pt >= 230.0  and pt <  260.0): weight =    0.948747217655
    elif (pt >= 260.0  and pt <  290.0): weight =    0.94176107645
    elif (pt >= 290.0  and pt <  320.0): weight =    0.934245705605
    elif (pt >= 320.0  and pt <  350.0): weight =    0.927089333534
    elif (pt >= 350.0  and pt <  390.0): weight =    0.919180750847
    elif (pt >= 390.0  and pt <  430.0): weight =    0.909925639629
    elif (pt >= 430.0  and pt <  470.0): weight =    0.900910794735
    elif (pt >= 470.0  and pt <  510.0): weight =    0.892561435699
    elif (pt >= 510.0  and pt <  550.0): weight =    0.884353041649
    elif (pt >= 550.0  and pt <  590.0): weight =    0.876099944115
    elif (pt >= 590.0  and pt <  640.0): weight =    0.867687404156
    elif (pt >= 640.0  and pt <  690.0): weight =    0.858047068119
    elif (pt >= 690.0  and pt <  740.0): weight =    0.849013924599
    elif (pt >= 740.0  and pt <  790.0): weight =    0.840316832066
    elif (pt >= 790.0  and pt <  840.0): weight =    0.832017362118
    elif (pt >= 840.0  and pt <  900.0): weight =    0.823544859886
    elif (pt >= 900.0  and pt <  960.0): weight =    0.814595520496
    elif (pt >= 960.0  and pt <  1020.0): weight =    0.806228935719
    elif (pt >= 1020.0 and pt <   1090.0): weight =    0.798037588596
    elif (pt >= 1090.0 and pt <   1160.0): weight =    0.789693713188
    elif (pt >= 1160.0): weight =    0.781163275242

    return weight

def getEWKG(pt):
    weight = 1.0
    if (pt <   170.0): weight =        0.993447899818
    elif (pt >=170.0 and pt <    200.0): weight =        0.990594148636
    elif (pt >=200.0  and pt <   230.0): weight =        0.987151265144
    elif (pt >=230.0  and pt <   260.0): weight =        0.983324110508
    elif (pt >=260.0  and pt <   290.0): weight =        0.980437457561
    elif (pt >=290.0  and pt <   320.0): weight =        0.977336466312
    elif (pt >=320.0  and pt <   350.0): weight =        0.974327743053
    elif (pt >=350.0  and pt <   390.0): weight =        0.970767736435
    elif (pt >=390.0  and pt <   430.0): weight =        0.968093931675
    elif (pt >=430.0  and pt <   470.0): weight =        0.963285326958
    elif (pt >=470.0  and pt <   510.0): weight =        0.959663629532
    elif (pt >=510.0 and pt <    550.0): weight =        0.955693006516
    elif (pt >=550.0  and pt <   590.0): weight =        0.95195555687
    elif (pt >=590.0  and pt <   640.0): weight =        0.948179006577
    elif (pt >=640.0  and pt <   690.0): weight =        0.943959712982
    elif (pt >=690.0  and pt <   740.0): weight =        0.940430998802
    elif (pt >=740.0  and pt <   790.0): weight =        0.936878621578
    elif (pt >=790.0  and pt <   840.0): weight =        0.933292031288
    elif (pt >=840.0  and pt <   900.0): weight =        0.929643988609
    elif (pt >=900.0  and pt <   960.0): weight =        0.925767362118
    elif (pt >=960.0  and pt <   1020.0): weight =        0.922028303146
    elif (pt >=1020.0 and pt <    1090.0): weight =        0.918239414692
    elif (pt >=1090.0  and pt <   1160.0): weight =        0.914257109165
    elif (pt >=1160.0): weight =  0.910161197186


def getQCDZ( pt):

  weight = fitfun(pt, 1.434, 2.210e-3, 0.443)
  return weight


def getQCDW(  pt):

  weight = fitfun(pt,1.053, 3.163e-3, 0.746)
  return weight


def getQCDG(pt):
    weight = fitfun(gen_v_pt, 1.159, 1.944e-3, 1.0)
    return weight
