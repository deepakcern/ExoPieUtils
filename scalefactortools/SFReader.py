import numpy as np
import SFFactory as SfF

def getEleTrigSF(pt,eta):
    matrix = np.matrix(SfF.eleTrig_hEffEtaPt)
    pT_range=[10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 150.0, 200.0]
    Eta_range=[-2.5, -2.0, -1.566, -1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])


    return matrix[binyj,binxi]


def getElelooseIDSF(pt,eta):
    matrix = np.matrix(SfF.eleRecoSF_EGamma_SF2D_ptgt_20)
    Eta_range = [-2.5, -2.0, -1.566, -1.444, -0.8, 0.0, 0.8, 1.444, 1.566, 2.0, 2.5]
    pT_range = [10.0, 20.0, 35.0, 50.0, 90.0, 150.0, 500.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binyj,binxi]


def getEleTightIDSF(pt,eta):
    matrix = np.matrix(SfF.eleTightIDSF_EGamma_SF2D)

    pT_range=[10.0, 20.0, 35.0, 50.0, 90.0, 150.0, 500.0]
    Eta_range=[-2.5, -2.0, -1.566, -1.444, -0.8, 0.0, 0.8, 1.444, 1.566, 2.0, 2.5]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binyj,binxi]


def getEleRecoLowSF(pt,eta):
    matrix = np.matrix("SFs/EGM2D_BtoH_low_RecoSF_Legacy2016.txt")
    Eta_range =  [-2.5, -2.0, -1.566, -1.444, -1.0, 0.0, 1.0, 1.444, 1.566, 2.0, 2.5]
    pT_range =  [10.0, 20.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])


    return matrix[binyj,binxi]

def getEleRecoHighSF(pt,eta):
    matrix = np.matrix(SfF.eleRecoSF_EGamma_SF2D_ptgt_20)
    Eta_range =  [-2.5, -2.0, -1.566, -1.444, -1.0, -0.5, 0.0, 0.5, 1.0, 1.444, 1.566, 2.0, 2.5]
    pT_range =  [20.0, 45.0, 75.0, 100.0, 500.0]

    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])


    return matrix[binyj,binxi]

def getMuTrigRunBCDEF_SF(pt,eta):
    matrix = np.matrix(SfF.muonTrigSFs_EfficienciesAndSF_RunBtoF)
    pT_range=[10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 150.0, 200.0]
    Eta_range=[-2.5, -2.0, -1.566, -1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binyj,binxi]


def getMuTrigRunGH_SF(pt,eta):
    matrix = np.matrix(SfF.muonTrigSFs_EfficienciesAndSF_Period4)
    pT_range=[10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 150.0, 200.0]
    Eta_range=[-2.5, -2.0, -1.566, -1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binyj,binxi]


def getMulooseRunBCDEF_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_BCDEF)
    Eta_range = [-2.5, -2.0, -1.566, -1.444, -0.8, 0.0, 0.8, 1.444, 1.566, 2.0, 2.5]
    pT_range = [10.0, 20.0, 35.0, 50.0, 90.0, 150.0, 500.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binyj,binxi]


def getMuTightRunBCDEF_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonTightIDSFs_EfficienciesAndSF_BCDEF)
    pT_range=[10.0, 20.0, 35.0, 50.0, 90.0, 150.0, 500.0]
    Eta_range=[-2.5, -2.0, -1.566, -1.444, -0.8, 0.0, 0.8, 1.444, 1.566, 2.0, 2.5]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binyj,binxi]


def getMulooseGH_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_GH)
    Eta_range =  [-2.5, -2.0, -1.566, -1.444, -1.0, 0.0, 1.0, 1.444, 1.566, 2.0, 2.5]
    pT_range =  [10.0, 20.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])


    return matrix[binyj,binxi]

def getMuTightGH_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_GH)
    Eta_range =  [-2.5, -2.0, -1.566, -1.444, -1.0, -0.5, 0.0, 0.5, 1.0, 1.444, 1.566, 2.0, 2.5]
    pT_range =  [20.0, 45.0, 75.0, 100.0, 500.0]

    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binyj,binxi]

def getMulooseBCDEF_lowpT_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF)
    Eta_range =  [0.0, 0.9, 1.2, 2.1, 2.4]
    pT_range =  [2.0, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    eta = abs(eta)
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binxi,binyj]

def getMuTightGH_lowpT_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_GH)
    Eta_range =  [0.0, 0.9, 1.2, 2.1, 2.4]
    pT_range =  [2.0, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0]
    eta = abs(eta)
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binxi,binyj]

def getMulooseRunBCDEF_ISOSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIsoSFs_EfficienciesAndSF_BCDEF)
    Eta_range = [-2.5, -2.0, -1.566, -1.444, -0.8, 0.0, 0.8, 1.444, 1.566, 2.0, 2.5]
    pT_range = [10.0, 20.0, 35.0, 50.0, 90.0, 150.0, 500.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binyj,binxi]


def getMuTightRunBCDEF_ISOSF(pt,eta):
    matrix = np.matrix(SfF.muonTightIsoSFs_EfficienciesAndSF_BCDEF)
    pT_range=[10.0, 20.0, 35.0, 50.0, 90.0, 150.0, 500.0]
    Eta_range=[-2.5, -2.0, -1.566, -1.444, -0.8, 0.0, 0.8, 1.444, 1.566, 2.0, 2.5]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binyj,binxi]


def getMulooseGH_ISOSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIsoSFs_EfficienciesAndSF_GH)
    Eta_range =  [-2.5, -2.0, -1.566, -1.444, -1.0, 0.0, 1.0, 1.444, 1.566, 2.0, 2.5]
    pT_range =  [10.0, 20.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binyj,binxi]


def getMuTightGH_ISOSF(pt,eta):
    matrix = np.matrix(SfF.muonTightIsoSFs_EfficienciesAndSF_GH)
    Eta_range =  [-2.5, -2.0, -1.566, -1.444, -1.0, -0.5, 0.0, 0.5, 1.0, 1.444, 1.566, 2.0, 2.5]
    pT_range =  [20.0, 45.0, 75.0, 100.0, 500.0]

    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binyj,binxi]

def getMuTrackingSF(eta):
    eta = abs(eta)
    matrix = np.array(SfF.muonTrackingSFs_EfficienciesAndSF_BCDEFGH)
    Eta_range =  [0.0, 0.026399999999999996, 0.05279999999999999, 0.07919999999999999, 0.10559999999999999, 0.13199999999999998, 0.15839999999999999, 0.18479999999999996, 0.21119999999999997, 0.23759999999999998, 0.26399999999999996, 0.29039999999999994, 0.31679999999999997, 0.34319999999999995, 0.36959999999999993, 0.39599999999999996, 0.42239999999999994, 0.4487999999999999, 0.47519999999999996, 0.5015999999999999, 0.5279999999999999, 0.5543999999999999, 0.5807999999999999, 0.6072, 0.6335999999999999, 0.6599999999999999, 0.6863999999999999, 0.7127999999999999, 0.7391999999999999, 0.7656, 0.7919999999999999, 0.8183999999999999, 0.8447999999999999, 0.8711999999999999, 0.8975999999999998, 0.9239999999999998, 0.9503999999999999, 0.9767999999999999, 1.0031999999999999, 1.0295999999999998, 1.0559999999999998, 1.0823999999999998, 1.1087999999999998, 1.1351999999999998, 1.1615999999999997, 1.188, 1.2144, 1.2408, 1.2671999999999999, 1.2935999999999999, 1.3199999999999998, 1.3463999999999998, 1.3727999999999998, 1.3991999999999998, 1.4255999999999998, 1.4519999999999997, 1.4783999999999997, 1.5047999999999997, 1.5312, 1.5575999999999999, 1.5839999999999999, 1.6103999999999998, 1.6367999999999998, 1.6631999999999998, 1.6895999999999998, 1.7159999999999997, 1.7423999999999997, 1.7687999999999997, 1.7951999999999997, 1.8215999999999997, 1.8479999999999996, 1.8743999999999998, 1.9007999999999998, 1.9271999999999998, 1.9535999999999998, 1.9799999999999998, 2.0063999999999997, 2.0328, 2.0591999999999997, 2.0856, 2.1119999999999997, 2.1384, 2.1647999999999996, 2.1912, 2.2175999999999996, 2.2439999999999998, 2.2703999999999995, 2.2967999999999997, 2.3231999999999995, 2.3495999999999997, 2.376, 2.4023999999999996, 2.4288, 2.4551999999999996, 2.4816, 2.5079999999999996, 2.5343999999999998, 2.5607999999999995, 2.5871999999999997, 2.6135999999999995, 2.6399999999999997]

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])
    return matrix[binyj]
