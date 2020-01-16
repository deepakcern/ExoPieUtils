import numpy as np
import sys
import SFFactory_2017 as SfF

def getEleTrigSF(pt,eta):
    matrix = np.matrix(SfF.eleTrig_hEffEtaPt)
    Eta_range=SfF.eleTrig_hEffEtaPt_X_range
    pT_range=SfF.eleTrig_hEffEtaPt_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]

def getElelooseIDSF(pt,eta):
    matrix = np.matrix(SfF.eleLooseIDSF_EGamma_SF2D)
    Eta_range = SfF.eleLooseIDSF_EGamma_SF2D_X_range
    pT_range = SfF.eleLooseIDSF_EGamma_SF2D_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getEleTightIDSF(pt,eta):
    matrix = np.matrix(SfF.eleTightIDSF_EGamma_SF2D)
    Eta_range =  SfF.eleTightIDSF_EGamma_SF2D_X_range
    pT_range =  SfF.eleTightIDSF_EGamma_SF2D_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getEleRecoLowSF(pt,eta):
    matrix = np.matrix(SfF.eleRecoSF_EGamma_SF2D_ptlt_20)
    Eta_range =  SfF.eleRecoSF_EGamma_SF2D_ptlt_20_X_range
    pT_range =  SfF.eleRecoSF_EGamma_SF2D_ptlt_20_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getEleRecoHighSF(pt,eta):
    matrix = np.matrix(SfF.eleRecoSF_EGamma_SF2D_ptgt_20)
    Eta_range =  SfF.eleRecoSF_EGamma_SF2D_ptgt_20_X_range
    pT_range =  SfF.eleRecoSF_EGamma_SF2D_ptgt_20_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getMuTrig_SF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonTrigSFs_EfficienciesAndSF_RunBtoF)
    Eta_range =  SfF.muonTrigSFs_EfficienciesAndSF_RunBtoF_X_range
    pT_range =  SfF.muonTrigSFs_EfficienciesAndSF_RunBtoF_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi]


def getMuloose_IDSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_BCDEF)
    Eta_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_BCDEF_Y_range
    pT_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_BCDEF_X_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj]


def getMuTight_IDSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonTightIDSFs_EfficienciesAndSF_BCDEF)
    Eta_range =  SfF.muonTightIDSFs_EfficienciesAndSF_BCDEF_Y_range
    pT_range =  SfF.muonTightIDSFs_EfficienciesAndSF_BCDEF_X_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj]


def getMuLoose_lowpT_IDSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF)
    Eta_range = SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF_Y_range
    pT_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF_X_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj]


def getMuLoose_ISOSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonLooseIsoSFs_EfficienciesAndSF_BCDEF)
    Eta_range =  SfF.muonLooseIsoSFs_EfficienciesAndSF_BCDEF_Y_range
    pT_range =  SfF.muonLooseIsoSFs_EfficienciesAndSF_BCDEF_X_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if pt < pT_range[0]:pt = pT_range[0]
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj]


def getMuTight_ISOSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonTightIsoSFs_EfficienciesAndSF_BCDEF)
    Eta_range =  SfF.muonTightIsoSFs_EfficienciesAndSF_BCDEF_Y_range
    pT_range =  SfF.muonTightIsoSFs_EfficienciesAndSF_BCDEF_X_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if pt < pT_range[0]:pt = pT_range[0]
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj]


def getMuTrackingSF(eta):
    eta = abs(eta)
    matrix = np.array(SfF.muonTrackingSFs_EfficienciesAndSF_BCDEFGH)
    Eta_range =  SfF.muonTrackingSFs_EfficienciesAndSF_BCDEFGH_X_range
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj]


def puweight(pu):
    matrix = np.array(SfF.pileup2017histo)
    PU_range =  SfF.pileup2017histo_X_range
    if pu >= PU_range[-1]:pu = PU_range[-2]
    if pu <= PU_range[0]:pu = PU_range[1]

    binyj=sorted([i for i, j in enumerate(PU_range) if j<=pu])[-1]
    return matrix[binyj]


def getMETtrig_First(met):
    matrix = np.array(SfF.metTrig_firstmethod)
    met_range =  SfF.metTrig_firstmethod_X_range
    if met >= met_range[-1]:pu = met_range[-2]
    if met <= met_range[0]:pu = met_range[1]

    binyj=sorted([i for i, j in enumerate(met_range) if j<=met])[-1]
    return matrix[binyj]
