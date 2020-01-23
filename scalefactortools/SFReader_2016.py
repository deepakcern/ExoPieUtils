import numpy as np
import sys
import SFFactory_2016 as SfF
import SFFactorySystUp_2016 as SfF_SystUp
import SFFactorySystDown_2016 as SfF_SystDown

def getEleTrigSF(pt,eta):
    matrix = np.matrix(SfF.eleTrig_hEffEtaPt)
    matrix_SystUp = np.matrix(SfF_SystUp.eleTrig_hEffEtaPt_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.eleTrig_hEffEtaPt_SystDown)
    Eta_range=SfF.eleTrig_hEffEtaPt_X_range
    pT_range=SfF.eleTrig_hEffEtaPt_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]

def getElelooseIDSF(pt,eta):
    matrix = np.matrix(SfF.eleLooseIDSF_EGamma_SF2D)
    matrix_SystUp = np.matrix(SfF_SystUp.eleLooseIDSF_EGamma_SF2D_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.eleLooseIDSF_EGamma_SF2D_SystDown)
    Eta_range = SfF.eleLooseIDSF_EGamma_SF2D_X_range
    pT_range = SfF.eleLooseIDSF_EGamma_SF2D_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0

    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getEleTightIDSF(pt,eta):
    matrix = np.matrix(SfF.eleTightIDSF_EGamma_SF2D)
    matrix_SystUp = np.matrix(SfF_SystUp.eleTightIDSF_EGamma_SF2D_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.eleTightIDSF_EGamma_SF2D_SystDown)
    Eta_range =  SfF.eleTightIDSF_EGamma_SF2D_X_range
    pT_range =  SfF.eleTightIDSF_EGamma_SF2D_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getEleRecoLowSF(pt,eta):
    matrix = np.matrix(SfF.eleRecoSF_EGamma_SF2D_ptlt_20)
    matrix_SystUp = np.matrix(SfF_SystUp.eleRecoSF_EGamma_SF2D_ptlt_20_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.eleRecoSF_EGamma_SF2D_ptlt_20_SystDown)
    Eta_range =  SfF.eleRecoSF_EGamma_SF2D_ptlt_20_X_range
    pT_range =  SfF.eleRecoSF_EGamma_SF2D_ptlt_20_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getEleRecoHighSF(pt,eta):
    matrix = np.matrix(SfF.eleRecoSF_EGamma_SF2D_ptgt_20)
    matrix_SystUp = np.matrix(SfF_SystUp.eleRecoSF_EGamma_SF2D_ptgt_20_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.eleRecoSF_EGamma_SF2D_ptgt_20_SystDown)
    Eta_range =  SfF.eleRecoSF_EGamma_SF2D_ptgt_20_X_range
    pT_range =  SfF.eleRecoSF_EGamma_SF2D_ptgt_20_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getMuTrigRunBCDEF_SF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonTrigSFs_EfficienciesAndSF_RunBtoF)
    matrix_SystUp = np.matrix(SfF_SystUp.muonTrigSFs_EfficienciesAndSF_RunBtoF_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonTrigSFs_EfficienciesAndSF_RunBtoF_SystDown)
    Eta_range =  SfF.muonTrigSFs_EfficienciesAndSF_RunBtoF_X_range
    pT_range =  SfF.muonTrigSFs_EfficienciesAndSF_RunBtoF_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getMuTrigRunGH_SF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonTrigSFs_EfficienciesAndSF_Period4)
    matrix_SystUp = np.matrix(SfF_SystUp.muonTrigSFs_EfficienciesAndSF_Period4_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonTrigSFs_EfficienciesAndSF_Period4_SystDown)
    Eta_range =  SfF.muonTrigSFs_EfficienciesAndSF_Period4_X_range
    pT_range =  SfF.muonTrigSFs_EfficienciesAndSF_Period4_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getMuTrig_SF(pt,eta):
    lumi_BCDEF=19.69;lumi_GH=16.22;lumi_tot=35.91
    bcdef_weight = lumi_BCDEF*getMuTrigRunBCDEF_SF(pt,eta)[0]
    bcdef_weight_SystUp = lumi_BCDEF*getMuTrigRunBCDEF_SF(pt,eta)[1]
    bcdef_weight_SystDown = lumi_BCDEF*getMuTrigRunBCDEF_SF(pt,eta)[2]
    gh_weight = lumi_GH*getMuTrigRunGH_SF(pt,eta)[0]
    gh_weight_SystUp = lumi_GH*getMuTrigRunGH_SF(pt,eta)[1]
    gh_weight_SystDown = lumi_GH*getMuTrigRunGH_SF(pt,eta)[2]
    weight = (bcdef_weight + gh_weight)/lumi_tot
    weight_SystUp = (bcdef_weight_SystUp + gh_weight_SystUp)/lumi_tot
    weight_SystDown = (bcdef_weight_SystDown + gh_weight_SystDown)/lumi_tot
    return weight,weight_SystUp,weight_SystDown


def getMulooseRunBCDEF_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_BCDEF)
    matrix_SystUp = np.matrix(SfF_SystUp.muonLooseIDSFs_EfficienciesAndSF_BCDEF_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonLooseIDSFs_EfficienciesAndSF_BCDEF_SystDown)
    Eta_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_BCDEF_X_range
    pT_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_BCDEF_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]

def getMulooseGH_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_GH)
    matrix_SystUp = np.matrix(SfF_SystUp.muonLooseIDSFs_EfficienciesAndSF_GH_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonLooseIDSFs_EfficienciesAndSF_GH_SystDown)
    Eta_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_GH_X_range
    pT_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_GH_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getMuloose_IDSF(pt,eta):
    lumi_BCDEF=19.69;lumi_GH=16.22;lumi_tot=35.91
    bcdef_weight = lumi_BCDEF*getMulooseRunBCDEF_IDSF(pt,eta)[0]
    bcdef_weight_SystUp = lumi_BCDEF*getMulooseRunBCDEF_IDSF(pt,eta)[1]
    bcdef_weight_SystDown = lumi_BCDEF*getMulooseRunBCDEF_IDSF(pt,eta)[2]
    gh_weight = lumi_GH*getMulooseGH_IDSF(pt,eta)[0]
    gh_weight_SystUp = lumi_GH*getMulooseGH_IDSF(pt,eta)[1]
    gh_weight_SystDown = lumi_GH*getMulooseGH_IDSF(pt,eta)[2]
    weight = (bcdef_weight + gh_weight)/lumi_tot
    weight_SystUp = (bcdef_weight_SystUp + gh_weight_SystUp)/lumi_tot
    weight_SystDown = (bcdef_weight_SystDown + gh_weight_SystDown)/lumi_tot
    return weight,weight_SystUp,weight_SystDown


def getMuTightRunBCDEF_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonTightIDSFs_EfficienciesAndSF_BCDEF)
    matrix_SystUp = np.matrix(SfF_SystUp.muonTightIDSFs_EfficienciesAndSF_BCDEF_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonTightIDSFs_EfficienciesAndSF_BCDEF_SystDown)
    Eta_range =  SfF.muonTightIDSFs_EfficienciesAndSF_BCDEF_X_range
    pT_range =  SfF.muonTightIDSFs_EfficienciesAndSF_BCDEF_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]

def getMuTightGH_IDSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_GH)
    matrix_SystUp = np.matrix(SfF_SystUp.muonLooseIDSFs_EfficienciesAndSF_GH_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonLooseIDSFs_EfficienciesAndSF_GH_SystDown)
    Eta_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_GH_X_range
    pT_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_GH_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getMuTight_IDSF(pt,eta):
    lumi_BCDEF=19.69;lumi_GH=16.22;lumi_tot=35.91
    bcdef_weight = lumi_BCDEF*getMuTightRunBCDEF_IDSF(pt,eta)[0]
    bcdef_weight_SystUp = lumi_BCDEF*getMuTightRunBCDEF_IDSF(pt,eta)[1]
    bcdef_weight_SystDown = lumi_BCDEF*getMuTightRunBCDEF_IDSF(pt,eta)[2]
    gh_weight = lumi_GH*getMuTightGH_IDSF(pt,eta)[0]
    gh_weight_SystUp = lumi_GH*getMuTightGH_IDSF(pt,eta)[1]
    gh_weight_SystDown = lumi_GH*getMuTightGH_IDSF(pt,eta)[2]
    weight = (bcdef_weight + gh_weight)/lumi_tot
    weight_SystUp = (bcdef_weight_SystUp + gh_weight_SystUp)/lumi_tot
    weight_SystDown = (bcdef_weight_SystDown + gh_weight_SystDown)/lumi_tot
    return weight,weight_SystUp,weight_SystDown


def getMulooseBCDEF_lowpT_IDSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF)
    matrix_SystUp = np.matrix(SfF_SystUp.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF_SystDown)
    Eta_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF_Y_range
    pT_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF_X_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj],matrix_SystUp[binxi,binyj],matrix_SystDown[binxi,binyj]

def getMuLooseGH_lowpT_IDSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_GH)
    matrix_SystUp = np.matrix(SfF_SystUp.muonLooseIDSFs_EfficienciesAndSF_lowpt_GH_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonLooseIDSFs_EfficienciesAndSF_lowpt_GH_SystDown)
    Eta_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_GH_Y_range
    pT_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_GH_X_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj],matrix_SystUp[binxi,binyj],matrix_SystDown[binxi,binyj]


def getMuLoose_lowpT_IDSF(pt,eta):
    lumi_BCDEF=19.69;lumi_GH=16.22;lumi_tot=35.91
    bcdef_weight = lumi_BCDEF*getMulooseBCDEF_lowpT_IDSF(pt,eta)[0]
    bcdef_weight_SystUp = lumi_BCDEF*getMulooseBCDEF_lowpT_IDSF(pt,eta)[1]
    bcdef_weight_SystDown = lumi_BCDEF*getMulooseBCDEF_lowpT_IDSF(pt,eta)[2]
    gh_weight = lumi_GH*getMuLooseGH_lowpT_IDSF(pt,eta)[0]
    gh_weight_SystUp = lumi_GH*getMuLooseGH_lowpT_IDSF(pt,eta)[1]
    gh_weight_SystDown = lumi_GH*getMuLooseGH_lowpT_IDSF(pt,eta)[2]
    weight = (bcdef_weight + gh_weight)/lumi_tot
    weight_SystUp = (bcdef_weight_SystUp + gh_weight_SystUp)/lumi_tot
    weight_SystDown = (bcdef_weight_SystDown + gh_weight_SystDown)/lumi_tot
    return weight,weight_SystUp,weight_SystDown


def getMulooseRunBCDEF_ISOSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIsoSFs_EfficienciesAndSF_BCDEF)
    matrix_SystUp = np.matrix(SfF_SystUp.muonLooseIsoSFs_EfficienciesAndSF_BCDEF_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonLooseIsoSFs_EfficienciesAndSF_BCDEF_SystDown)
    Eta_range =  SfF.muonLooseIsoSFs_EfficienciesAndSF_BCDEF_X_range
    pT_range =  SfF.muonLooseIsoSFs_EfficienciesAndSF_BCDEF_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if pt < pT_range[0]:pt = pT_range[0]
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getMulooseGH_ISOSF(pt,eta):
    matrix = np.matrix(SfF.muonLooseIsoSFs_EfficienciesAndSF_GH)
    matrix_SystUp = np.matrix(SfF_SystUp.muonLooseIsoSFs_EfficienciesAndSF_GH_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonLooseIsoSFs_EfficienciesAndSF_GH_SystDown)
    Eta_range =  SfF.muonLooseIsoSFs_EfficienciesAndSF_GH_X_range
    pT_range =  SfF.muonLooseIsoSFs_EfficienciesAndSF_GH_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if pt < pT_range[0]:pt = pT_range[0]
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getMuLoose_ISOSF(pt,eta):
    lumi_BCDEF=19.69;lumi_GH=16.22;lumi_tot=35.91
    bcdef_weight = lumi_BCDEF*getMulooseRunBCDEF_ISOSF(pt,eta)[0]
    bcdef_weight_SystUp = lumi_BCDEF*getMulooseRunBCDEF_ISOSF(pt,eta)[1]
    bcdef_weight_SystDown = lumi_BCDEF*getMulooseRunBCDEF_ISOSF(pt,eta)[2]
    gh_weight = lumi_GH*getMulooseGH_ISOSF(pt,eta)[0]
    gh_weight_SystUp = lumi_GH*getMulooseGH_ISOSF(pt,eta)[1]
    gh_weight_SystDown = lumi_GH*getMulooseGH_ISOSF(pt,eta)[2]
    weight = (bcdef_weight + gh_weight)/lumi_tot
    weight_SystUp = (bcdef_weight_SystUp + gh_weight_SystUp)/lumi_tot
    weight_SystDown = (bcdef_weight_SystDown + gh_weight_SystDown)/lumi_tot
    return weight,weight_SystUp,weight_SystDown


def getMuTightRunBCDEF_ISOSF(pt,eta):
    matrix = np.matrix(SfF.muonTightIsoSFs_EfficienciesAndSF_BCDEF)
    matrix_SystUp = np.matrix(SfF_SystUp.muonTightIsoSFs_EfficienciesAndSF_BCDEF_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonTightIsoSFs_EfficienciesAndSF_BCDEF_SystDown)
    Eta_range =  SfF.muonTightIsoSFs_EfficienciesAndSF_BCDEF_X_range
    pT_range =  SfF.muonTightIsoSFs_EfficienciesAndSF_BCDEF_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if pt < pT_range[0]:pt = pT_range[0]
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getMuTightGH_ISOSF(pt,eta):
    matrix = np.matrix(SfF.muonTightIsoSFs_EfficienciesAndSF_GH)
    matrix_SystUp = np.matrix(SfF_SystUp.muonTightIsoSFs_EfficienciesAndSF_GH_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonTightIsoSFs_EfficienciesAndSF_GH_SystDown)
    Eta_range =  SfF.muonTightIsoSFs_EfficienciesAndSF_GH_X_range
    pT_range =  SfF.muonTightIsoSFs_EfficienciesAndSF_GH_Y_range
    if pt > pT_range[-1]:pt = pT_range[-1]-1.0
    if pt < pT_range[0]:pt = pT_range[0]
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    # print ([j for i, j in enumerate(Eta_range) if j<=eta][-1])

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]

def getMuTight_ISOSF(pt,eta):
    lumi_BCDEF=19.69;lumi_GH=16.22;lumi_tot=35.91
    bcdef_weight = lumi_BCDEF*getMuTightRunBCDEF_ISOSF(pt,eta)[0]
    bcdef_weight_SystUp = lumi_BCDEF*getMuTightRunBCDEF_ISOSF(pt,eta)[1]
    bcdef_weight_SystDown = lumi_BCDEF*getMuTightRunBCDEF_ISOSF(pt,eta)[2]
    gh_weight = lumi_GH*getMuTightGH_ISOSF(pt,eta)[0]
    gh_weight_SystUp = lumi_GH*getMuTightGH_ISOSF(pt,eta)[1]
    gh_weight_SystDown = lumi_GH*getMuTightGH_ISOSF(pt,eta)[2]
    weight = (bcdef_weight + gh_weight)/lumi_tot
    weight_SystUp = (bcdef_weight_SystUp + gh_weight_SystUp)/lumi_tot
    weight_SystDown = (bcdef_weight_SystDown + gh_weight_SystDown)/lumi_tot
    return weight,weight_SystUp,weight_SystDown


def getMuTrackingSF(eta):
    eta = abs(eta)
    matrix = np.array(SfF.muonTrackingSFs_EfficienciesAndSF_BCDEFGH)
    matrix_SystUp = np.array(SfF_SystUp.muonTrackingSFs_EfficienciesAndSF_BCDEFGH_SystUp)
    matrix_SystDown = np.array(SfF_SystDown.muonTrackingSFs_EfficienciesAndSF_BCDEFGH_SystDown)
    Eta_range =  SfF.muonTrackingSFs_EfficienciesAndSF_BCDEFGH_X_range
    if eta >= Eta_range[-1]:eta = Eta_range[-2]
    if eta <= Eta_range[0]:eta = Eta_range[1]

    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj],matrix_SystUp[binyj],matrix_SystDown[binyj]


def puweight(pu):
    matrix = np.array(SfF.pileup2016histo)
    matrix_SystUp = np.array(SfF_SystUp.pileup2016histo_SystUp)
    matrix_SystDown = np.array(SfF_SystDown.pileup2016histo_SystDown)
    PU_range =  SfF.pileup2016histo_X_range
    if pu >= PU_range[-1]:pu = PU_range[-2]
    if pu <= PU_range[0]:pu = PU_range[1]

    binyj=sorted([i for i, j in enumerate(PU_range) if j<=pu])[-1]
    return matrix[binyj],matrix_SystUp[binyj],matrix_SystDown[binyj]


def getMETtrig_First(met):
    matrix = np.array(SfF.metTrig_firstmethod)
    matrix_SystUp = np.array(SfF_SystUp.metTrig_firstmethod_SystUp)
    matrix_SystDown = np.array(SfF_SystDown.metTrig_firstmethod_SystDown)
    met_range =  SfF.metTrig_firstmethod_X_range
    if met >= met_range[-1]:pu = met_range[-2]
    if met <= met_range[0]:pu = met_range[1]

    binyj=sorted([i for i, j in enumerate(met_range) if j<=met])[-1]
    return matrix[binyj],matrix_SystUp[binyj],matrix_SystDown[binyj]
