import SFReader as SFR

def ele_weight(pt,eta):
    trig_w = SFR.getEleTrigSF(pt,eta)
    looseID_w = SFR.getElelooseIDSF(pt,eta)
    tightID_w = SFR.getEleTightIDSF(pt,eta)
    recolow_w = SFR.getEleRecoLowSF(pt,eta)
    recohigh_w = SFR.getEleRecoHighSF(pt,eta)
    if pt > 30:
        weight = trig_w*tightID_w*recohigh_w
    elif pt > 20:
        weight = looseID_w*recohigh_w
    else:
        looseID_w*recolow_w
    return weight

def mu_weight(pt,eta):
    trig_w = SFR.getMuTrig_SF(pt,eta)
    looseID_w = SFR.getMuloose_IDSF(pt,eta)
    tightID_w = SFR.getMuTight_IDSF(pt,eta)
    looseID_low_w = SFR.getMuLoose_lowpT_IDSF(pt,eta)
    looseISO_w = SFR.getMuLoose_ISOSF(pt,eta)
    tightISO_w = SFR.getMuTight_ISOSF(pt,eta)
    tracking_w = SFR.getMuTrackingSF(eta)
    if pt > 30:
        weight = trig_w*tightID_w*tightISO_w*tracking_w
    elif pt > 20:
        weight = looseID_w*looseISO_w*tracking_w
    else:
        looseID_low_w*looseISO_w*tracking_w
    return weight
