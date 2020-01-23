import ROOT as ROOT
import os,sys
sys.path.append('../../ExoPieProducer/ExoPieAnalyzer/')
from Year import era

def weightbtag(reader, flav, pt, eta, era):
    if era=='2016' and abs(eta) >= 2.4: eta = 2.3999999
    if (era=='2017' or era=='2018')  and abs(eta) >= 2.5: eta = 2.4999999
    sf_c = reader.eval_auto_bounds('central', flav, eta, pt)
    sf_low = reader.eval_auto_bounds('down', flav, eta, pt)
    sf_up  = reader.eval_auto_bounds('up', flav, eta, pt)
    btagsf = [sf_c, sf_low, sf_up]
    return btagsf

def jetflav(flav):
    if flav == 5:
        flavor = 0
    elif flav == 4:
        flavor = 1
    else:
        flavor = 2
    return flavor

def getBeff(pt,eta,flav):
    if flav == 5:
        xbin = b_med_eff.GetXaxis().FindBin(eta)
        ybin = b_med_eff.GetYaxis().FindBin(pt)
        btag_eff = b_med_eff.GetBinContent(xbin,ybin)
        return btag_eff
    elif flav == 4:
        xbin = c_med_eff.GetXaxis().FindBin(eta)
        ybin = c_med_eff.GetYaxis().FindBin(pt)
        ctag_eff = c_med_eff.GetBinContent(xbin,ybin)
        return ctag_eff
    elif flav!=4 and flav!=5:
        xbin = udsg_med_eff.GetXaxis().FindBin(eta)
        ybin = udsg_med_eff.GetYaxis().FindBin(pt)
        lighttag_eff = udsg_med_eff.GetBinContent(xbin,ybin)
        return lighttag_eff


ROOT.gROOT.ProcessLine('.L '+os.path.dirname(__file__)+'/btagSF_Files/BTagCalibrationStandalone.cpp+')
if era=='2016':
    calib1 = ROOT.BTagCalibrationStandalone('deepcsv', os.path.dirname(__file__)+'/btagSF_Files/DeepCSV_Moriond17_B_H.csv')
    tag_eff_file = ROOT.TFile(os.path.dirname(__file__)+'/btagSF_Files/bTagEffs_2016.root')
    deepCSVLWP = 0.2217
    deepCSVMWP = 0.6321
    deepCSVTWP = 0.8953
elif era=='2017':
    calib1 = ROOT.BTagCalibrationStandalone('deepcsv', os.path.dirname(__file__)+'/btagSF_Files/DeepCSV_94XSF_V4_B_F.csv')
    tag_eff_file = ROOT.TFile(os.path.dirname(__file__)+'/btagSF_Files/bTagEffs_2017.root')
    deepCSVLWP = 0.1522
    deepCSVMWP = 0.4941
    deepCSVTWP = 0.8001
elif era=='2018':
    calib1 = ROOT.BTagCalibrationStandalone('deepcsv', os.path.dirname(__file__)+'/btagSF_Files/DeepCSV_102XSF_V1.csv')
    tag_eff_file = ROOT.TFile(os.path.dirname(__file__)+'/btagSF_Files/bTagEffs_2018.root')
    deepCSVLWP = 0.1241
    deepCSVMWP = 0.4184
    deepCSVTWP = 0.7527

b_med_eff = tag_eff_file.Get('efficiency_b_pass')
c_med_eff = tag_eff_file.Get('efficiency_c_pass')
udsg_med_eff = tag_eff_file.Get('efficiency_light_pass')

non_b_med_eff = tag_eff_file.Get('efficiency_b_fail')
non_c_med_eff = tag_eff_file.Get('efficiency_c_fail')
non_udsg_med_eff = tag_eff_file.Get('efficiency_light_fail')

othersys = ROOT.std.vector('string')()
othersys.push_back('down')
othersys.push_back('up')
reader1 = ROOT.BTagCalibrationStandaloneReader( 0, "central", othersys)
reader1.load(calib1, 0,  "comb" )
reader1.load(calib1, 1,  "comb" )
reader1.load(calib1, 2,  "incl" )

def btag_weight(nJets,ptList,etalist,flavlist,depCSVlist):
    P_MC = 1.0;
    P_Data = 1.0; P_Data_up = 1.0; P_Data_down = 1.0
    btagweight = 1.0;btagweight_up=1.0;btagweight_down=1.0
    for i in range(nJets):
        tag_eff    = getBeff(ptList[i],etalist[i],flavlist[i])
        if depCSVlist[i] >deepCSVMWP:
            P_MC *= tag_eff
        else:
            P_MC *= (1-tag_eff)
        SF_jet = []
        SF_jet=weightbtag(reader1, jetflav(flavlist[i]), ptList[i], etalist[i],era)
        if depCSVlist[i] > deepCSVMWP:
            P_Data *= (SF_jet[0] *tag_eff)
            P_Data_down *= (SF_jet[1] *tag_eff)
            P_Data_up *= (SF_jet[2] *tag_eff)
        else:
            P_Data *= (1 - SF_jet[0] * tag_eff)
            P_Data_down *= (1 - SF_jet[1] * tag_eff)
            P_Data_up *= (1 - SF_jet[2] * tag_eff)
    if P_MC > 0:
        btagweight = P_Data/P_MC
        btagweight_up = P_Data_up/P_MC
        btagweight_down = P_Data_down/P_MC
    return btagweight,btagweight_up,btagweight_down
