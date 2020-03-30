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
    import EWKfactory_2017 as ewk
else:
    print("Please tell me which year\'s scale factors you would like to apply (2016,2017 or 2018)? ")

def eletrig_weight(pt,eta):
    trig_w = 1.0; trig_w_UP = 1.0; trig_w_DOWN = 1.0
    if pt > 30. :
        trig_w = SFR.getEleTrigSF(pt,eta)[0]
        trig_w_UP = SFR.getEleTrigSF(pt,eta)[1]
        trig_w_DOWN = SFR.getEleTrigSF(pt,eta)[2]
    return trig_w,trig_w_UP,trig_w_DOWN

def ele_weight(pt,eta,ID='None'):
    ID_w = 1.0; Reco_w = 1.0
    ID_w_UP = 1.0; Reco_w_UP = 1.0
    ID_w_DOWN = 1.0; Reco_w_DOWN = 1.0
    if ID=="T" :
        ID_w = SFR.getEleTightIDSF(pt,eta)[0]
        ID_w_UP = SFR.getEleTightIDSF(pt,eta)[1]
        ID_w_DOWN = SFR.getEleTightIDSF(pt,eta)[2]
    if ID=="L" :
        ID_w = SFR.getElelooseIDSF(pt,eta)[0]
        ID_w_UP = SFR.getElelooseIDSF(pt,eta)[1]
        ID_w_DOWN = SFR.getElelooseIDSF(pt,eta)[2]
    if pt >= 20.0 :
        Reco_w = SFR.getEleRecoHighSF(pt,eta)[0]
        Reco_w_UP = SFR.getEleRecoHighSF(pt,eta)[1]
        Reco_w_DOWN = SFR.getEleRecoHighSF(pt,eta)[2]
    elif pt < 20.0 :
        if era=='2016' or era=='2017':
            Reco_w = SFR.getEleRecoLowSF(pt,eta)[0]
            Reco_w_UP = SFR.getEleRecoLowSF(pt,eta)[1]
            Reco_w_DOWN = SFR.getEleRecoLowSF(pt,eta)[2]
        elif era=='2018':
            Reco_w = SFR.getEleRecoHighSF(pt,eta)[0]
            Reco_w_UP = SFR.getEleRecoHighSF(pt,eta)[1]
            Reco_w_DOWN = SFR.getEleRecoHighSF(pt,eta)[2]
    elif ID =='None':
        print ('Please select which ID electron you want(L or T)')
    weight = ID_w*Reco_w
    weight_UP = ID_w_UP*Reco_w_UP
    weight_DOWN = ID_w_DOWN*Reco_w_DOWN
    return weight,weight_UP,weight_DOWN

def mutrig_weight(pt,eta):
    trig_w = 1.0; trig_w_UP = 1.0; trig_w_DOWN = 1.0
    if pt >30.0:
        trig_w = SFR.getMuTrig_SF(pt,eta)[0]
        trig_w_UP = SFR.getMuTrig_SF(pt,eta)[1]
        trig_w_DOWN = SFR.getMuTrig_SF(pt,eta)
    return trig_w,trig_w_UP,trig_w_DOWN

def mu_weight(pt,eta,ID='None'):
    ID_ISO_w=1.0; tracking_w = 1.0
    ID_ISO_w_UP=1.0; tracking_w_UP = 1.0
    ID_ISO_w_DOWN=1.0; tracking_w_DOWN   = 1.0
    if ID=="T" and pt>20.0:
        ID_ISO_w = SFR.getMuTight_ISOSF(pt,eta)[0]*SFR.getMuTight_IDSF(pt,eta)[0]
        ID_ISO_w_UP = SFR.getMuTight_ISOSF(pt,eta)[1]*SFR.getMuTight_IDSF(pt,eta)[1]
        ID_ISO_w_DOWN = SFR.getMuTight_ISOSF(pt,eta)[2]*SFR.getMuTight_IDSF(pt,eta)[2]
    if ID=="L" and pt>20.0:
        ID_ISO_w = SFR.getMuLoose_ISOSF(pt,eta)[0]*SFR.getMuloose_IDSF(pt,eta)[0]
        ID_ISO_w_UP = SFR.getMuLoose_ISOSF(pt,eta)[1]*SFR.getMuloose_IDSF(pt,eta)[1]
        ID_ISO_w_DOWN = SFR.getMuLoose_ISOSF(pt,eta)[2]*SFR.getMuloose_IDSF(pt,eta)[2]
    if pt<=20.0 and ID=="L":
        ID_ISO_w = SFR.getMuLoose_lowpT_IDSF(pt,eta)[0]*SFR.getMuLoose_ISOSF(pt,eta)[0]
        ID_ISO_w_UP = SFR.getMuLoose_lowpT_IDSF(pt,eta)[1]*SFR.getMuLoose_ISOSF(pt,eta)[1]
        ID_ISO_w_DOWN = SFR.getMuLoose_lowpT_IDSF(pt,eta)[2]*SFR.getMuLoose_ISOSF(pt,eta)[2]
    elif ID =='None':
        print ('Please select which ID muon you want(L or T)')
    if era=='2016':
        tracking_w,tracking_w_UP,tracking_w_DOWN = SFR.getMuTrackingSF(eta)
    weight = ID_ISO_w*tracking_w
    weight_UP = ID_ISO_w_UP*tracking_w_UP
    weight_DOWN = ID_ISO_w_DOWN*tracking_w_DOWN
    return weight,weight_UP,weight_DOWN

def getMETtrig_First(met,cat):
    if cat=='R' and (era=='2017' or era=='2018'):
        return SFR.R_getMETtrig_First(met)
    elif cat=='B' and (era=='2017' or era=='2018'):
        return SFR.B_getMETtrig_First(met)
    else:
        return SFR.getMETtrig_First(met)  # this is for 2016

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
    return k2,1.5*k2,0.5*k2

def getBTagSF(nJets,ptList,etalist,flavlist,depCSVlist,WP,index=False):
    return btagsf.btag_weight(nJets,ptList,etalist,flavlist,depCSVlist,WP,index)
