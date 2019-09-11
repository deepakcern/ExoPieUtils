import os
import sys 
sys.path.append('../commonutils/')
import MathUtils as mathutil
#from MathUtils import *
import BooleanUtils as boolutil


debug_ = False

def CheckFilter(filterName, filterResult,filtercompare):
    ifilter_=0
    filter1 = False
    for ifilter in filterName:
        filter1 = (ifilter.find(filtercompare) != -1)  & (bool(filterResult[ifilter_]) == True)
        if filter1: break
        ifilter_ = ifilter_ + 1
    return filter1

def jetcleaning(ak4_pt30_eta4p5_IDT, lep_looseID, ak4eta, lepeta, ak4phi, lepphi, DRCut):
    ## usage: (obj_to_clean, obj_cleaned_against, so on
    if debug_: print "njet, nlep", len(ak4_pt30_eta4p5_IDT), len(lep_looseID)
    jetCleanAgainstLep = []
    pass_jet_index_cleaned = []
    if len(ak4_pt30_eta4p5_IDT) > 0:
        for ijet in range(len(ak4_pt30_eta4p5_IDT)):
            pass_ijet_ilep_ = True
            if (len(lep_looseID)>0):
                for ilep in range(len(lep_looseID)):
                    pass_ijet_ilep_ = (ak4_pt30_eta4p5_IDT[ijet] and lep_looseID[ilep] and (mathutil.Delta_R(ak4eta[ijet], lepeta[ilep], ak4phi[ijet], lepphi[ilep]) > 0.4))
                    if not pass_ijet_ilep_ : break
            if debug_: print "-------- pass_ijet_ilep_ = ",pass_ijet_ilep_
            jetCleanAgainstLep.append(pass_ijet_ilep_)
            if debug_: print "inside function pass_ijet_ilep_ = ", pass_ijet_ilep_
            if debug_: print "inside function jetCleanAgainstLep = ", jetCleanAgainstLep

    return jetCleanAgainstLep



def getGenPt(sample,nGenPar, genParId, genMomParId, genParSt,genParP4):
    pt=0.0
    #################
    # WJets
    #################
    if sample=="WJETS":
    #if True:
        goodLepID = []
        for ig in range(nGenPar):
            PID    = genParId[ig]
            momPID = genMomParId[ig]
            status = genParSt[ig]
            if ( (abs(PID) != 11) & (abs(PID) != 12) &  (abs(PID) != 13) & (abs(PID) != 14) &  (abs(PID) != 15) &  (abs(PID) != 16) ): continue
            if ( ( (status != 1) & (abs(PID) != 15)) | ( (status != 2) & (abs(PID) == 15)) ): continue
            if ( (abs(momPID) != 24) & (momPID != PID) ): continue
            goodLepID.append(ig)

        if len(goodLepID) == 2 :
            l4_thisLep = genParP4[goodLepID[0]]
            l4_thatLep = genParP4[goodLepID[1]]
            l4_z = l4_thisLep + l4_thatLep
            pt = l4_z.Pt()

    #################
    #ZJets
    #################
    if sample == "ZJETS":
    #if True:
        goodLepID = []
        for ig in range(nGenPar):
            PID    = genParId[ig]
            momPID = genMomParId[ig]
            status = genParSt[ig]


            if ( (abs(PID) != 12) &  (abs(PID) != 14) &  (abs(PID) != 16) ) : continue
            if ( status != 1 ) : continue
            if ( (momPID != 23) & (momPID != PID) ) : continue
            goodLepID.append(ig)

        if len(goodLepID) == 2 :
            l4_thisLep = genParP4[goodLepID[0]]
            l4_thatLep = genParP4[goodLepID[1]]
            l4_z = l4_thisLep + l4_thatLep
            pt = l4_z.Pt()

    return pt


def GetTTPt(sample, nGenPar, genParId, genMomParId, genParSt, genParP4):
    #################
    #TTBar
    #################
    ptList=[]
    if (sample=="TT"):
        goodLepID = []
        for ig in range(nGenPar):
            PID    = genParId[ig]
            momPID = genMomParId[ig]
            status = genParSt[ig]
            if ( abs(PID) == 6) :
                goodLepID.append(ig)
        if(len(goodLepID)==2):
            l4_thisLep = genParP4[goodLepID[0]]
            l4_thatLep = genParP4[goodLepID[1]]
            ptList =  [l4_thisLep.Pt(), l4_thatLep.Pt()]
            
    return ptList
