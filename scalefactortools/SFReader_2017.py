import numpy as np
import sys
import SFFactory_2017 as SfF
import SFFactorySystUp_2017 as SfF_SystUp
import SFFactorySystDown_2017 as SfF_SystDown

corr_fac=0.0001

def getEleTrigSF(pt,eta):
    matrix = np.matrix(SfF.eleTrig_hEffEtaPt)
    matrix_SystUp = np.matrix(SfF_SystUp.eleTrig_hEffEtaPt_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.eleTrig_hEffEtaPt_SystDown)
    Eta_range=SfF.eleTrig_hEffEtaPt_X_range
    pT_range=SfF.eleTrig_hEffEtaPt_Y_range
    if pt >= pT_range[-1]:pt = pT_range[-1]-corr_fac
    if pt <= pT_range[0]:pt = pT_range[0]+corr_fac
    if eta >= Eta_range[-1]:eta = Eta_range[-1]-corr_fac
    if eta <= Eta_range[0]:eta = Eta_range[0]+corr_fac

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]

def getElelooseIDSF(pt,eta):
    matrix = np.matrix(SfF.eleLooseIDSF_EGamma_SF2D)
    matrix_SystUp = np.matrix(SfF_SystUp.eleLooseIDSF_EGamma_SF2D_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.eleLooseIDSF_EGamma_SF2D_SystDown)
    Eta_range = SfF.eleLooseIDSF_EGamma_SF2D_X_range
    pT_range = SfF.eleLooseIDSF_EGamma_SF2D_Y_range
    if pt >= pT_range[-1]:pt = pT_range[-1]-corr_fac
    if pt <= pT_range[0]:pt = pT_range[0]+corr_fac
    if eta >= Eta_range[-1]:eta = Eta_range[-1]-corr_fac
    if eta <= Eta_range[0]:eta = Eta_range[0]+corr_fac

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getEleTightIDSF(pt,eta):
    matrix = np.matrix(SfF.eleTightIDSF_EGamma_SF2D)
    matrix_SystUp = np.matrix(SfF_SystUp.eleTightIDSF_EGamma_SF2D_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.eleTightIDSF_EGamma_SF2D_SystDown)
    Eta_range =  SfF.eleTightIDSF_EGamma_SF2D_X_range
    pT_range =  SfF.eleTightIDSF_EGamma_SF2D_Y_range
    if pt >= pT_range[-1]:pt = pT_range[-1]-corr_fac
    if pt <= pT_range[0]:pt = pT_range[0]+corr_fac
    if eta >= Eta_range[-1]:eta = Eta_range[-1]-corr_fac
    if eta <= Eta_range[0]:eta = Eta_range[0]+corr_fac

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getEleRecoLowSF(pt,eta):
    matrix = np.matrix(SfF.eleRecoSF_EGamma_SF2D_ptlt_20)
    matrix_SystUp = np.matrix(SfF_SystUp.eleRecoSF_EGamma_SF2D_ptlt_20_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.eleRecoSF_EGamma_SF2D_ptlt_20_SystDown)
    Eta_range =  SfF.eleRecoSF_EGamma_SF2D_ptlt_20_X_range
    pT_range =  SfF.eleRecoSF_EGamma_SF2D_ptlt_20_Y_range
    if pt >= pT_range[-1]:pt = pT_range[-1]-corr_fac
    if pt <= pT_range[0]:pt = pT_range[0]+corr_fac
    if eta >= Eta_range[-1]:eta = Eta_range[-1]-corr_fac
    if eta <= Eta_range[0]:eta = Eta_range[0]+corr_fac

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getEleRecoHighSF(pt,eta):
    matrix = np.matrix(SfF.eleRecoSF_EGamma_SF2D_ptgt_20)
    matrix_SystUp = np.matrix(SfF_SystUp.eleRecoSF_EGamma_SF2D_ptgt_20_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.eleRecoSF_EGamma_SF2D_ptgt_20_SystDown)
    Eta_range =  SfF.eleRecoSF_EGamma_SF2D_ptgt_20_X_range
    pT_range =  SfF.eleRecoSF_EGamma_SF2D_ptgt_20_Y_range
    if pt >= pT_range[-1]:pt = pT_range[-1]-corr_fac
    if pt <= pT_range[0]:pt = pT_range[0]+corr_fac
    if eta >= Eta_range[-1]:eta = Eta_range[-1]-corr_fac
    if eta <= Eta_range[0]:eta = Eta_range[0]+corr_fac

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getMuTrig_SF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonTrigSFs_EfficienciesAndSF_RunBtoF)
    matrix_SystUp = np.matrix(SfF_SystUp.muonTrigSFs_EfficienciesAndSF_RunBtoF_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonTrigSFs_EfficienciesAndSF_RunBtoF_SystDown)
    Eta_range =  SfF.muonTrigSFs_EfficienciesAndSF_RunBtoF_X_range
    pT_range =  SfF.muonTrigSFs_EfficienciesAndSF_RunBtoF_Y_range
    if pt >= pT_range[-1]:pt = pT_range[-1]-corr_fac
    if pt <= pT_range[0]:pt = pT_range[0]+corr_fac
    if eta >= Eta_range[-1]:eta = Eta_range[-1]-corr_fac
    if eta <= Eta_range[0]:eta = Eta_range[0]+corr_fac

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binyj,binxi],matrix_SystUp[binyj,binxi],matrix_SystDown[binyj,binxi]


def getMuloose_IDSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_BCDEF)
    matrix_SystUp = np.matrix(SfF_SystUp.muonLooseIDSFs_EfficienciesAndSF_BCDEF_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonLooseIDSFs_EfficienciesAndSF_BCDEF_SystDown)
    Eta_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_BCDEF_Y_range
    pT_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_BCDEF_X_range
    if pt >= pT_range[-1]:pt = pT_range[-1]-corr_fac
    if pt <= pT_range[0]:pt = pT_range[0]+corr_fac
    if eta >= Eta_range[-1]:eta = Eta_range[-1]-corr_fac
    if eta <= Eta_range[0]:eta = Eta_range[0]+corr_fac

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj],matrix_SystUp[binxi,binyj],matrix_SystDown[binxi,binyj]


def getMuTight_IDSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonTightIDSFs_EfficienciesAndSF_BCDEF)
    matrix_SystUp = np.matrix(SfF_SystUp.muonTightIDSFs_EfficienciesAndSF_BCDEF_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonTightIDSFs_EfficienciesAndSF_BCDEF_SystDown)
    Eta_range =  SfF.muonTightIDSFs_EfficienciesAndSF_BCDEF_Y_range
    pT_range =  SfF.muonTightIDSFs_EfficienciesAndSF_BCDEF_X_range
    if pt >= pT_range[-1]:pt = pT_range[-1]-corr_fac
    if pt <= pT_range[0]:pt = pT_range[0]+corr_fac
    if eta >= Eta_range[-1]:eta = Eta_range[-1]-corr_fac
    if eta <= Eta_range[0]:eta = Eta_range[0]+corr_fac

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj],matrix_SystUp[binxi,binyj],matrix_SystDown[binxi,binyj]


def getMuLoose_lowpT_IDSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF)
    matrix_SystUp = np.matrix(SfF_SystUp.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF_SystDown)
    Eta_range = SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF_Y_range
    pT_range =  SfF.muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF_X_range
    if pt >= pT_range[-1]:pt = pT_range[-1]-corr_fac
    if pt <= pT_range[0]:pt = pT_range[0]+corr_fac
    if eta >= Eta_range[-1]:eta = Eta_range[-1]-corr_fac
    if eta <= Eta_range[0]:eta = Eta_range[0]+corr_fac

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj],matrix_SystUp[binxi,binyj],matrix_SystDown[binxi,binyj]


def getMuLoose_ISOSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonLooseIsoSFs_EfficienciesAndSF_BCDEF)
    matrix_SystUp = np.matrix(SfF_SystUp.muonLooseIsoSFs_EfficienciesAndSF_BCDEF_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonLooseIsoSFs_EfficienciesAndSF_BCDEF_SystDown)
    Eta_range =  SfF.muonLooseIsoSFs_EfficienciesAndSF_BCDEF_Y_range
    pT_range =  SfF.muonLooseIsoSFs_EfficienciesAndSF_BCDEF_X_range
    if pt >= pT_range[-1]:pt = pT_range[-1]-corr_fac
    if pt <= pT_range[0]:pt = pT_range[0]+corr_fac
    if eta >= Eta_range[-1]:eta = Eta_range[-1]-corr_fac
    if eta <= Eta_range[0]:eta = Eta_range[0]+corr_fac

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj], matrix_SystUp[binxi,binyj], matrix_SystDown[binxi,binyj]


def getMuTight_ISOSF(pt,eta):
    eta = abs(eta)
    matrix = np.matrix(SfF.muonTightIsoSFs_EfficienciesAndSF_BCDEF)
    matrix_SystUp = np.matrix(SfF_SystUp.muonTightIsoSFs_EfficienciesAndSF_BCDEF_SystUp)
    matrix_SystDown = np.matrix(SfF_SystDown.muonTightIsoSFs_EfficienciesAndSF_BCDEF_SystDown)
    Eta_range =  SfF.muonTightIsoSFs_EfficienciesAndSF_BCDEF_Y_range
    pT_range =  SfF.muonTightIsoSFs_EfficienciesAndSF_BCDEF_X_range
    if pt >= pT_range[-1]:pt = pT_range[-1]-corr_fac
    if pt <= pT_range[0]:pt = pT_range[0]+corr_fac
    if eta >= Eta_range[-1]:eta = Eta_range[-1]-corr_fac
    if eta <= Eta_range[0]:eta = Eta_range[1]+corr_fac

    binxi=sorted([i for i, j in enumerate(pT_range) if j<=pt])[-1]
    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]

    return matrix[binxi,binyj], matrix_SystUp[binxi,binyj], matrix_SystDown[binxi,binyj]


def getMuTrackingSF(eta):
    eta = abs(eta)
    matrix = np.array(SfF.muonTrackingSFs_EfficienciesAndSF_BCDEFGH)
    matrix_SystUp = np.array(SfF_SystUp.muonTrackingSFs_EfficienciesAndSF_BCDEFGH_SystUp)
    matrix_SystDown = np.array(SfF_SystDown.muonTrackingSFs_EfficienciesAndSF_BCDEFGH_SystDown)
    Eta_range =  SfF.muonTrackingSFs_EfficienciesAndSF_BCDEFGH_X_range
    if eta >= Eta_range[-1]:eta = Eta_range[-1]
    if eta <= Eta_range[0]:eta = Eta_range[0]

    binyj=sorted([i for i, j in enumerate(Eta_range) if j<=eta])[-1]
    return matrix[binyj],matrix_SystUp[binyj],matrix_SystDown[binyj]


def puweight(pu):
    matrix = np.array(SfF.pileup2017histo)
    matrix_SystUp = np.array(SfF_SystUp.pileup2017histo_SystUp)
    matrix_SystDown = np.array(SfF_SystDown.pileup2017histo_SystDown)
    PU_range =  SfF.pileup2017histo_X_range
    if pu >= PU_range[-1]:pu = PU_range[-1]
    if pu <= PU_range[0]:pu = PU_range[0]

    # binyj=sorted([i for i, j in enumerate(PU_range) if j<=pu])[-1]
    binyj = int(pu)
    return matrix[binyj],matrix_SystUp[binyj],matrix_SystDown[binyj]


def R_getMETtrig_First(met):
    matrix = np.array(SfF.R_metTrig_firstmethod)
    matrix_SystUp = np.array(SfF_SystUp.R_metTrig_firstmethod_SystUp)
    matrix_SystDown = np.array(SfF_SystDown.R_metTrig_firstmethod_SystDown)
    met_range =  SfF.R_metTrig_firstmethod_X_range
    if met >= met_range[-1]:pu = met_range[-1]
    if met <= met_range[0]:pu = met_range[0]

    binyj=sorted([i for i, j in enumerate(met_range) if j<=met])[-1]
    return matrix[binyj],matrix_SystUp[binyj],matrix_SystDown[binyj]

def B_getMETtrig_First(met):
    matrix = np.array(SfF.B_metTrig_firstmethod)
    matrix_SystUp = np.array(SfF_SystUp.B_metTrig_firstmethod_SystUp)
    matrix_SystDown = np.array(SfF_SystDown.B_metTrig_firstmethod_SystDown)
    met_range =  SfF.B_metTrig_firstmethod_X_range
    if met >= met_range[-1]:pu = met_range[-1]
    if met <= met_range[0]:pu = met_range[0]

    binyj=sorted([i for i, j in enumerate(met_range) if j<=met])[-1]
    return matrix[binyj],matrix_SystUp[binyj],matrix_SystDown[binyj]
