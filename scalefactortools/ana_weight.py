import SFReader as SFR

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
