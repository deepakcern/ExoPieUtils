import numpy as np
import sys
sys.path.append('../../ExoPieProducer/ExoPieAnalyzer/')

from Year import era
if era=='2016':
    import SFFactory_2016 as SfF
elif era=='2017':
    import SFFactory_2016 as SfF
elif era=='2018':
    import SFFactory_2018 as SfF

def getEleTrigSF(pt,eta):
    matrix = np.matrix(SfF.eleTrig_hEffEtaPt)
    pT_range=[10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 150.0, 200.0]
    Eta_range=[-2.5, -2.0, -1.566, -1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]

def getElelooseIDSF(pt,eta):
    matrix = np.matrix(SfF.eleLooseIDSF_EGamma_SF2D)
    Eta_range =  [-2.5, -2.0, -1.566, -1.444, -0.8, 0.0, 0.8, 1.444, 1.566, 2.0, 2.5]
    pT_range =  [10.0, 20.0, 35.0, 50.0, 90.0, 150.0, 500.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getEleTightIDSF(pt,eta):
    matrix = np.matrix(SfF.eleTightIDSF_EGamma_SF2D)
    Eta_range =  [-2.5, -2.0, -1.566, -1.444, -0.8, 0.0, 0.8, 1.444, 1.566, 2.0, 2.5]
    pT_range =  [10.0, 20.0, 35.0, 50.0, 90.0, 150.0, 500.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getEleRecoLowSF(pt,eta):
    matrix = np.matrix(SfF.eleRecoSF_EGamma_SF2D_ptlt_20)
    Eta_range =  [-2.5, -2.0, -1.566, -1.444, -1.0, 0.0, 1.0, 1.444, 1.566, 2.0, 2.5]
    pT_range =  [10.0, 20.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

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

    return matrix[binyj,binxi]


def getMuTrigRunBCDEF_SF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonTrigSFs_EfficienciesAndSF_RunBtoF)
    Eta_range =  [0.0, 0.9, 1.2, 2.1, 2.4]
    pT_range =  [26.0, 30.0, 40.0, 50.0, 60.0, 120.0, 200.0, 500.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getMuTrigRunGH_SF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonTrigSFs_EfficienciesAndSF_Period4)
    Eta_range =  [0.0, 0.9, 1.2, 2.1, 2.4]
    pT_range =  [26.0, 30.0, 40.0, 50.0, 60.0, 120.0, 200.0, 500.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getMuTrig_SF(pt,eta):
    lumi_BCDEF=19.69;lumi_GH=16.22;lumi_tot=35.91
    bcdef_weight = lumi_BCDEF*getMuTrigRunBCDEF_SF(pt,eta)
    gh_weight = lumi_GH*getMuTrigRunGH_SF(pt,eta)
    weight = (bcdef_weight + gh_weight)/lumi_tot
    return weight


def getMulooseRunBCDEF_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_BCDEF)
    Eta_range =  [-2.4, -2.3, -2.2, -2.1, -2.0, -1.7, -1.6, -1.5, -1.4, -1.2, -0.8, -0.5, -0.3, -0.2, 0.0, 0.2, 0.3, 0.5, 0.8, 1.2, 1.4, 1.5, 1.6, 1.7, 2.0, 2.1, 2.2, 2.3, 2.4]
    pT_range =  [20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 120.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]

def getMulooseGH_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_GH)
    Eta_range =  [-2.4, -2.3, -2.2, -2.1, -2.0, -1.7, -1.6, -1.5, -1.4, -1.2, -0.8, -0.5, -0.3, -0.2, 0.0, 0.2, 0.3, 0.5, 0.8, 1.2, 1.4, 1.5, 1.6, 1.7, 2.0, 2.1, 2.2, 2.3, 2.4]
    pT_range =  [20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 120.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getMuloose_IDSF(pt,eta):
    lumi_BCDEF=19.69;lumi_GH=16.22;lumi_tot=35.91
    bcdef_weight = lumi_BCDEF*getMulooseRunBCDEF_IDSF(pt,eta)
    gh_weight = lumi_GH*getMulooseGH_IDSF(pt,eta)
    weight = (bcdef_weight + gh_weight)/lumi_tot
    return weight


def getMuTightRunBCDEF_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonTightIDSFs_EfficienciesAndSF_BCDEF)
    Eta_range =  [-2.4, -2.3, -2.2, -2.1, -2.0, -1.7, -1.6, -1.5, -1.4, -1.2, -0.8, -0.5, -0.3, -0.2, 0.0, 0.2, 0.3, 0.5, 0.8, 1.2, 1.4, 1.5, 1.6, 1.7, 2.0, 2.1, 2.2, 2.3, 2.4]
    pT_range =  [20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 120.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]

def getMuTightGH_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_GH)
    Eta_range =  [-2.4, -2.3, -2.2, -2.1, -2.0, -1.7, -1.6, -1.5, -1.4, -1.2, -0.8, -0.5, -0.3, -0.2, 0.0, 0.2, 0.3, 0.5, 0.8, 1.2, 1.4, 1.5, 1.6, 1.7, 2.0, 2.1, 2.2, 2.3, 2.4]
    pT_range =  [20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 120.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getMuTight_IDSF(pt,eta):
    lumi_BCDEF=19.69;lumi_GH=16.22;lumi_tot=35.91
    bcdef_weight = lumi_BCDEF*getMuTightRunBCDEF_IDSF(pt,eta)
    gh_weight = lumi_GH*getMuTightGH_IDSF(pt,eta)
    weight = (bcdef_weight + gh_weight)/lumi_tot
    return weight


def getMulooseBCDEF_lowpT_IDSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF)
    Eta_range =  [0.0, 0.9, 1.2, 2.1, 2.4]
    pT_range =  [2.0, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj]

def getMuLooseGH_lowpT_IDSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_GH)
    Eta_range =  [0.0, 0.9, 1.2, 2.1, 2.4]
    pT_range =  [2.0, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj]


def getMuLoose_lowpT_IDSF(pt,eta):
    lumi_BCDEF=19.69;lumi_GH=16.22;lumi_tot=35.91
    bcdef_weight = lumi_BCDEF*getMulooseBCDEF_lowpT_IDSF(pt,eta)
    gh_weight = lumi_GH*getMuLooseGH_lowpT_IDSF(pt,eta)
    weight = (bcdef_weight + gh_weight)/lumi_tot
    return weight


def getMulooseRunBCDEF_ISOSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIsoSFs_EfficienciesAndSF_BCDEF)
    Eta_range =  [-2.4, -2.3, -2.2, -2.1, -2.0, -1.7, -1.6, -1.5, -1.4, -1.2, -0.8, -0.5, -0.3, -0.2, 0.0, 0.2, 0.3, 0.5, 0.8, 1.2, 1.4, 1.5, 1.6, 1.7, 2.0, 2.1, 2.2, 2.3, 2.4]
    pT_range =  [20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 120.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if pt < pT_range[0]:pt = pT_range[0]
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getMulooseGH_ISOSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIsoSFs_EfficienciesAndSF_GH)
    Eta_range =  [-2.4, -2.3, -2.2, -2.1, -2.0, -1.7, -1.6, -1.5, -1.4, -1.2, -0.8, -0.5, -0.3, -0.2, 0.0, 0.2, 0.3, 0.5, 0.8, 1.2, 1.4, 1.5, 1.6, 1.7, 2.0, 2.1, 2.2, 2.3, 2.4]
    pT_range =  [20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 120.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if pt < pT_range[0]:pt = pT_range[0]
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getMuLoose_ISOSF(pt,eta):
    lumi_BCDEF=19.69;lumi_GH=16.22;lumi_tot=35.91
    bcdef_weight = lumi_BCDEF*getMulooseRunBCDEF_ISOSF(pt,eta)
    gh_weight = lumi_GH*getMulooseGH_ISOSF(pt,eta)
    weight = (bcdef_weight + gh_weight)/lumi_tot
    return weight


def getMuTightRunBCDEF_ISOSF(pt,eta):
    matrix = np.matrix(SfF.muonTightIsoSFs_EfficienciesAndSF_BCDEF)
    Eta_range =  [-2.4, -2.3, -2.2, -2.1, -2.0, -1.7, -1.6, -1.5, -1.4, -1.2, -0.8, -0.5, -0.3, -0.2, 0.0, 0.2, 0.3, 0.5, 0.8, 1.2, 1.4, 1.5, 1.6, 1.7, 2.0, 2.1, 2.2, 2.3, 2.4]
    pT_range =  [20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 120.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if pt < pT_range[0]:pt = pT_range[0]
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getMuTightGH_ISOSF(pt,eta):
    matrix = np.matrix(SfF.muonTightIsoSFs_EfficienciesAndSF_GH)
    Eta_range =  [-2.4, -2.3, -2.2, -2.1, -2.0, -1.7, -1.6, -1.5, -1.4, -1.2, -0.8, -0.5, -0.3, -0.2, 0.0, 0.2, 0.3, 0.5, 0.8, 1.2, 1.4, 1.5, 1.6, 1.7, 2.0, 2.1, 2.2, 2.3, 2.4]
    pT_range =  [20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 120.0]
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if pt < pT_range[0]:pt = pT_range[0]
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binyj,binxi]

def getMuTight_ISOSF(pt,eta):
    lumi_BCDEF=19.69;lumi_GH=16.22;lumi_tot=35.91
    bcdef_weight = lumi_BCDEF*getMuTightRunBCDEF_ISOSF(pt,eta)
    gh_weight = lumi_GH*getMuTightGH_ISOSF(pt,eta)
    weight = (bcdef_weight + gh_weight)/lumi_tot
    return weight


def getMuTrackingSF(eta):
    eta = abs(eta)
    matrix = np.array(SfF.muonTrackingSFs_EfficienciesAndSF_BCDEFGH)
    Eta_range =  [0.0, 0.026399999999999996, 0.05279999999999999, 0.07919999999999999, 0.10559999999999999, 0.13199999999999998, 0.15839999999999999, 0.18479999999999996, 0.21119999999999997, 0.23759999999999998, 0.26399999999999996, 0.29039999999999994, 0.31679999999999997, 0.34319999999999995, 0.36959999999999993, 0.39599999999999996, 0.42239999999999994, 0.4487999999999999, 0.47519999999999996, 0.5015999999999999, 0.5279999999999999, 0.5543999999999999, 0.5807999999999999, 0.6072, 0.6335999999999999, 0.6599999999999999, 0.6863999999999999, 0.7127999999999999, 0.7391999999999999, 0.7656, 0.7919999999999999, 0.8183999999999999, 0.8447999999999999, 0.8711999999999999, 0.8975999999999998, 0.9239999999999998, 0.9503999999999999, 0.9767999999999999, 1.0031999999999999, 1.0295999999999998, 1.0559999999999998, 1.0823999999999998, 1.1087999999999998, 1.1351999999999998, 1.1615999999999997, 1.188, 1.2144, 1.2408, 1.2671999999999999, 1.2935999999999999, 1.3199999999999998, 1.3463999999999998, 1.3727999999999998, 1.3991999999999998, 1.4255999999999998, 1.4519999999999997, 1.4783999999999997, 1.5047999999999997, 1.5312, 1.5575999999999999, 1.5839999999999999, 1.6103999999999998, 1.6367999999999998, 1.6631999999999998, 1.6895999999999998, 1.7159999999999997, 1.7423999999999997, 1.7687999999999997, 1.7951999999999997, 1.8215999999999997, 1.8479999999999996, 1.8743999999999998, 1.9007999999999998, 1.9271999999999998, 1.9535999999999998, 1.9799999999999998, 2.0063999999999997, 2.0328, 2.0591999999999997, 2.0856, 2.1119999999999997, 2.1384, 2.1647999999999996, 2.1912, 2.2175999999999996, 2.2439999999999998, 2.2703999999999995, 2.2967999999999997, 2.3231999999999995, 2.3495999999999997, 2.376, 2.4023999999999996, 2.4288, 2.4551999999999996, 2.4816, 2.5079999999999996, 2.5343999999999998, 2.5607999999999995, 2.5871999999999997, 2.6135999999999995, 2.6399999999999997]
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj]


def puweight(pu):
    matrix = np.array(SfF.pileup2016histo)
    PU_range =  [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0,46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0]
    if pu >= PU_range[-1]:pu = PU_range[-2]
    if pu <= PU_range[0]:pu = PU_range[1]

    binyj=sorted([i for i, j in enumerate(PU_range) if j<=pu])[-1]
    return matrix[binyj]


def getMETtrig_First(met):
    matrix = np.array(SfF.metTrig_firstmethod)
    met_range =  [0.0, 50.0, 60.0, 70.0, 80.0, 85.0, 95.0, 100.0, 110.0, 120.0, 130.0, 140.0, 150.0, 160.0, 180.0, 200.0, 225.0, 250.0, 275.0, 300.0, 350.0, 400.0, 450.0, 500.0, 550.0, 650.0, 800.0, 1000.0, 1250.0]
    if met >= met_range[-1]:pu = met_range[-2]
    if met <= met_range[0]:pu = met_range[1]

    binyj=sorted([i for i, j in enumerate(met_range) if j<=met])[-1]
    return matrix[binyj]


def getMETtrig_Second(met):
    matrix = np.array(SfF.metTrig_secondmethod)
    met_range =  [0.0, 50.0, 60.0, 70.0, 80.0, 85.0, 95.0, 100.0, 110.0, 120.0, 130.0, 140.0, 150.0, 160.0, 180.0, 200.0, 225.0, 250.0, 275.0, 300.0, 350.0, 400.0, 450.0, 500.0, 550.0, 650.0, 800.0, 1000.0, 1250.0]
    if met >= met_range[-1]:pu = met_range[-2]
    if met <= met_range[0]:pu = met_range[1]

    binyj=sorted([i for i, j in enumerate(met_range) if j<=met])[-1]
    return matrix[binyj]
