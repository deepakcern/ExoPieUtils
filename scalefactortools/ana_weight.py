

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


def ele_weight(pt,eta,ID='None'):
    trig_w = SFR.getEleTrigSF(pt,eta)
    looseID_w = SFR.getElelooseIDSF(pt,eta)
    tightID_w = SFR.getEleTightIDSF(pt,eta)
    recolow_w = SFR.getEleRecoLowSF(pt,eta)
    recohigh_w = SFR.getEleRecoHighSF(pt,eta)
    if ID =='T':
        weight = trig_w*tightID_w*recohigh_w
    elif ID =='L':
        weight = looseID_w*recohigh_w
    elif  pt<20 and ID =='L':
        looseID_w*recolow_w
    elif ID =='None':
        print ('Please select which ID electron you want(L or T)')
    return weight

def mu_weight(pt,eta,ID='None'):
    trig_w = SFR.getMuTrig_SF(pt,eta)
    looseID_w = SFR.getMuloose_IDSF(pt,eta)
    tightID_w = SFR.getMuTight_IDSF(pt,eta)
    looseID_low_w = SFR.getMuLoose_lowpT_IDSF(pt,eta)
    looseISO_w = SFR.getMuLoose_ISOSF(pt,eta)
    tightISO_w = SFR.getMuTight_ISOSF(pt,eta)
    tracking_w = SFR.getMuTrackingSF(eta)
    if ID =='T':
        weight = trig_w*tightID_w*tightISO_w*tracking_w
    elif ID=='L':
        weight = looseID_w*looseISO_w*tracking_w
    elif pt<20 and ID=='L':
        looseID_low_w*looseISO_w*tracking_w
    elif ID =='None':
        print ('Please select which ID muon you want(L or T)')
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
    return ewk.getRenUpW(pt)

def getRenDownZ(pt):
    return ewk.getRenDownW(pt)

def getFacUpZ(pt):
    return ewk.getFacUpW(pt)

def getFacDownZ(pt):
    return ewk.getFacDownW(pt)

    
