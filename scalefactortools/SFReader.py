import os
import SFFactory as SfF

def getptetabin(pt,eta):
    iptbin=sorted([i for i, j in enumerate(SfF.pt_bins_eleTrig_hEffEtaPt) if j<=pt])[-1]
    ietabin=sorted([i for i, j in enumerate(SfF.eta_bins_eleTrig_hEffEtaPt) if j<=eta])[-1]
    return [iptbin,ietabin]

def getKey(iptbin,ietabin):
    ptetakey='pt_'+str(iptbin)+'_eta_'+str(ietabin)
    return ptetakey

def readEleTrigSF(pt, eta):
    iptetabin=getptetabin(pt,eta)
    iptbin = iptetabin[0]
    ietabin = iptetabin[1]
    return SfF.dict_eleTrig_hEffEtaPt.get(getKey(iptbin,ietabin))

eletrigSF = readEleTrigSF(40.,-1.5)
print(eletrigSF)
