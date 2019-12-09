import sys
import ROOT as rt
import btag_SFMaker as btagsf
sys.path.append('../../ExoPieProducer/ExoPieAnalyzer/')

from Year import era

if era=='2016':
    import SFReader_2016 as SFR
    import EWKfactory_2016 as ewk
elif era=='2017':
    import SFReader_2017 as SFR
    import EWKfactory_2017 as ewk
elif era=='2018':
    import SFReader_2018 as SFR
    import EWKfactory_2018 as ewk
else:
    print("Please tell me which year\'s scale factors you would like to apply (2016,2017 or 2018)? ")

def eletrig_weight(pt,eta):
    trig_w = 1.0
    if pt > 30. :  trig_w = SFR.getEleTrigSF(pt,eta)
    return trig_w

def ele_weight(pt,eta,ID='None'):
    ID_w = 1.0; Reco_w = 1.0
    if ID=="T" :   ID_w = SFR.getEleTightIDSF(pt,eta)
    if ID=="L" :   ID_w = SFR.getElelooseIDSF(pt,eta)
    if pt >= 20.0 :  Reco_w = SFR.getEleRecoHighSF(pt,eta)
    elif pt < 20.0 : Reco_w = SFR.getEleRecoLowSF(pt,eta)
    elif ID =='None':
        print ('Please select which ID electron you want(L or T)')
    weight = ID_w*Reco_w
    return weight

def mutrig_weight(pt,eta):
    trig_w = 1.0;
    if pt >30.0: trig_w = SFR.getMuTrig_SF(pt,eta)
    return trig_w

def mu_weight(pt,eta,ID='None'):
    ID_ISO_w=1.0; tracking_w = 1.0
    if ID=="T" :          ID_ISO_w = SFR.getMuTight_ISOSF(pt,eta)*SFR.getMuTight_IDSF(pt,eta)
    if ID=="L" and pt>=20.0:          ID_ISO_w = SFR.getMuLoose_ISOSF(pt,eta)*SFR.getMuloose_IDSF(pt,eta)
    if pt<20.0 and ID=="L": ID_ISO_w = SFR.getMuLoose_lowpT_IDSF(pt,eta)*SFR.getMuLoose_ISOSF(pt,eta)
    elif ID =='None':
        print ('Please select which ID muon you want(L or T)')
    if era=='2016':
        tracking_w = SFR.getMuTrackingSF(eta)
    weight = ID_ISO_w*tracking_w
    return weight

def getMETtrig_First(met):
    return SFR.getMETtrig_First(met)

def getMETtrig_Second(met):
    return SFR.getMETtrig_Second(met)

def puweight(pu):
    return SFR.puweight(pu)

def getEWKW(pt):
    return ewk.getEWKW(pt)

def getQCDW(pt):
    return ewk.getQCDW(pt)

def getRenUpW(pt):
    return ewk.getRenUpW(pt)

def getRenDownW(pt):
    return ewk.getRenDownW(pt)

def getFacUpW(pt):
    return ewk.getFacUpW(pt)

def getFacDownW(pt):
    return ewk.getFacDownW(pt)

def getEWKZ(pt):
    return ewk.getEWKZ(pt)

def getQCDZ(pt):
    return ewk.getQCDZ(pt)

def getRenUpZ(pt):
    return ewk.getRenUpZ(pt)

def getRenDownZ(pt):
    return ewk.getRenDownZ(pt)

def getFacUpZ(pt):
    return ewk.getFacUpZ(pt)

def getFacDownZ(pt):
    return ewk.getFacDownZ(pt)

def getTopPtReWgt(pt1, pt2):
    w1 = rt.TMath.Exp(0.0615 - 0.0005*pt1);
    w2 = rt.TMath.Exp(0.0615 - 0.0005*pt2);
    k2 = rt.TMath.Sqrt(w1*w2)
    return k2

def getBTagSF(nJets,ptList,etalist,flavlist,depCSVlist):
    return btagsf.btag_weight(nJets,ptList,etalist,flavlist,depCSVlist)
