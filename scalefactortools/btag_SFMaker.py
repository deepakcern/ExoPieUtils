import ROOT as ROOT
import os

def getBeff(P4,flav):
    if flav == 5:
        ybin = b_med_eff.GetXaxis().FindBin(P4.Eta())
        xbin = b_med_eff.GetYaxis().FindBin(P4.Pt())
        btag_eff = b_med_eff.GetBinContent(xbin,ybin)
        return btag_eff
    elif flav == 4:
        ybin = c_med_eff.GetXaxis().FindBin(P4.Eta())
        xbin = c_med_eff.GetYaxis().FindBin(P4.Pt())
        ctag_eff = c_med_eff.GetBinContent(xbin,ybin)
        return ctag_eff
    elif flav!=4 and flav!=5:
        ybin = udsg_med_eff.GetXaxis().FindBin(P4.Eta())
        xbin = udsg_med_eff.GetYaxis().FindBin(P4.Pt())
        lighttag_eff = udsg_med_eff.GetBinContent(xbin,ybin)
        return lighttag_eff

ROOT.gROOT.ProcessLine('.L BTagCalibrationStandalone.cpp+')


## ThinJets
calib1 = ROOT.BTagCalibrationStandalone('deepcsv', 'DeepCSV_Moriond17_B_H.csv')

reader1 = ROOT.BTagCalibrationStandaloneReader( 0, "central", othersys)
reader1.load(calib1, 0,  "comb" )
reader1.load(calib1, 1,  "comb" )
reader1.load(calib1, 2,  "incl" )


P_MC = 1.0
P_Data = 1.0
btagweight = 1.0
for i in range(nJets):
    tag_eff = getBeff(myJetP4[i],myJetHadronFlavor[i])
    P_MC *= (1-tag_eff)
    reader1.eval_auto_bounds('central', 0, 2.4, 30.)
    SF_jet = []
    SF_jet=weightbtag(reader1, jetflav(myJetHadronFlavor[jet]), myJetP4[jet].Pt(), myJetP4[jet].Eta())
    P_Data *= (1 - SF_jet[0] *tag_eff)
    #print 'eff: ',getBeff(myJetP4[i])
if P_MC > 0:
    btagweight = P_Data/P_MC
allweights = allweights * btagweight
