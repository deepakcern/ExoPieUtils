#coded by Praveen
from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, TF1, AddressOf
import ROOT as ROOT
import os
import random
import sys, optparse
from array import array
import math

ROOT.gROOT.SetBatch(True)

#pileup reweights
pileup2016file = TFile('data_2016/PU_Reweight_2016.root')
pileup2016histo=pileup2016file.Get('pileup')

#Electron Trigger reweights
eleTrigReweightFile = TFile('data_2016/electron_Trigger_eleTrig.root')
eleTrig_hEffEtaPt = eleTrigReweightFile.Get('hEffEtaPt')
eleTrig_hEffEtaPtUp = eleTrigReweightFile.Get('hErrhEtaPt')
eleTrig_hEffEtaPtDown = eleTrigReweightFile.Get('hErrlEtaPt')

#Electron Reconstruction efficiency. Scale factors for 80X
eleRecoSFsFile_ptgt_20 = TFile('data_2016/EGM2D_BtoH_GT20GeV_RecoSF_Legacy2016.root')
eleRecoSF_EGamma_SF2D_ptgt_20 = eleRecoSFsFile_ptgt_20.Get('EGamma_SF2D')

eleRecoSFsFile_ptlt_20 = TFile('data_2016/EGM2D_BtoH_low_RecoSF_Legacy2016.root')
eleRecoSF_EGamma_SF2D_ptlt_20 = eleRecoSFsFile_ptlt_20.Get('EGamma_SF2D')

#Loose electron ID SFs
eleLooseIDSFsFile = TFile('data_2016/2016LegacyReReco_ElectronLoose.root')
eleLooseIDSF_EGamma_SF2D = eleLooseIDSFsFile.Get('EGamma_SF2D')

#Tight Electron ID SFs
eleTightIDSFsFile = TFile('data_2016/2016LegacyReReco_ElectronTight.root')
eleTightIDSF_EGamma_SF2D = eleTightIDSFsFile.Get('EGamma_SF2D')

#Tight photon ID SFs
phoTightIDSFsFile = TFile('data_2016/80X_2016_Tight_photons.root')
phoTightIDSF_EGamma_SF2D = phoTightIDSFsFile.Get('EGamma_SF2D')

#Loose photon ID SFs
phoLooseIDSFsFile = TFile('data_2016/80X_2016_Loose_photons.root')
phoLooseIDSF_EGamma_SF2D = phoLooseIDSFsFile.Get('EGamma_SF2D')

#Muon Trigger SFs
#BCDEF
muonTrigSFsRunBCDEFFile = TFile('data_2016/muon_single_lepton_trigger_EfficienciesAndSF_RunBtoF.root')
muonTrigSFs_EfficienciesAndSF_RunBtoF = muonTrigSFsRunBCDEFFile.Get('IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio')
#GH
muonTrigSFsRunGHFile = TFile('data_2016/muon_single_lepton_trigger_EfficienciesAndSF_Period4.root')
muonTrigSFs_EfficienciesAndSF_Period4 = muonTrigSFsRunGHFile.Get('IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio')

#Muon ID SFs
#BCDEF
muonIDSFsBCDEFFile = TFile('data_2016/Muon_RunBCDEF_SF_ID.root')
muonLooseIDSFs_EfficienciesAndSF_BCDEF = muonIDSFsBCDEFFile.Get('NUM_LooseID_DEN_genTracks_eta_pt')
muonTightIDSFs_EfficienciesAndSF_BCDEF = muonIDSFsBCDEFFile.Get('NUM_TightID_DEN_genTracks_eta_pt')
#GH
muonIDSFsGHFile = TFile('data_2016/Muon_RunGH_SF_ID.root')
muonLooseIDSFs_EfficienciesAndSF_GH = muonIDSFsGHFile.Get('NUM_LooseID_DEN_genTracks_eta_pt')
muonTightIDSFs_EfficienciesAndSF_GH = muonIDSFsGHFile.Get('NUM_TightID_DEN_genTracks_eta_pt')

#for low pt muons
#BCDEF
muonIDSFsBCDEFFile_lowpt = TFile('data_2016/Muon_low-pT_RunBCDEF_SF_ID.root')
muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF = muonIDSFsBCDEFFile_lowpt.Get('NUM_LooseID_DEN_genTracks_pt_abseta')
#GH
muonIDSFsGHFile_lowpt = TFile('data_2016/Muon_low-pT_RunBCDEF_SF_ID.root')
muonLooseIDSFs_EfficienciesAndSF_lowpt_GH = muonIDSFsGHFile_lowpt.Get('NUM_LooseID_DEN_genTracks_pt_abseta')

#Muon Iso SFs
#BCDEF
muonIsoSFsBCDEFFile = TFile('data_2016/Muon_RunBCDEF_SF_ISO.root')
muonLooseIsoSFs_EfficienciesAndSF_BCDEF = muonIsoSFsBCDEFFile.Get('NUM_LooseRelIso_DEN_LooseID_eta_pt')
muonTightIsoSFs_EfficienciesAndSF_BCDEF = muonIsoSFsBCDEFFile.Get('NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt')
#GH
muonIsoSFsGHFile = TFile('data_2016/Muon_RunGH_SF_ISO.root')
muonLooseIsoSFs_EfficienciesAndSF_GH = muonIsoSFsGHFile.Get('NUM_LooseRelIso_DEN_LooseID_eta_pt')
muonTightIsoSFs_EfficienciesAndSF_GH = muonIsoSFsGHFile.Get('NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt')

#Muon Tracking SFs
muonTrackingSFsFile = TFile('data_2016/muon_Tracking_SFs_Tracking_EfficienciesAndSF_BCDEFGH.root')
muonTrackingSFs_EfficienciesAndSF_BCDEFGH = muonTrackingSFsFile.Get('ratio_eff_aeta_dr030e030_corr')


#MET Trigger reweights
metTrigEff_zmmfile = TFile('data_2016/metTriggerEfficiency_zmm_recoil_monojet_TH1F.root')
metTrig_firstmethod = metTrigEff_zmmfile.Get('hden_monojet_recoil_clone_passed')

metTrigEff_secondfile = TFile('data_2016/metTriggerEfficiency_recoil_monojet_TH1F.root')
metTrig_secondmethod = metTrigEff_secondfile.Get('hden_monojet_recoil_clone_passed')


sf_list = [pileup2016histo,eleTrig_hEffEtaPt,eleRecoSF_EGamma_SF2D_ptgt_20,eleRecoSF_EGamma_SF2D_ptlt_20,eleLooseIDSF_EGamma_SF2D,eleTightIDSF_EGamma_SF2D,muonTrigSFs_EfficienciesAndSF_RunBtoF,muonTrigSFs_EfficienciesAndSF_Period4,muonLooseIDSFs_EfficienciesAndSF_BCDEF,muonLooseIDSFs_EfficienciesAndSF_GH,muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF,muonLooseIDSFs_EfficienciesAndSF_lowpt_GH,muonTightIDSFs_EfficienciesAndSF_BCDEF,muonTightIDSFs_EfficienciesAndSF_GH,muonLooseIsoSFs_EfficienciesAndSF_BCDEF,muonLooseIsoSFs_EfficienciesAndSF_GH,muonTightIsoSFs_EfficienciesAndSF_BCDEF,muonTightIsoSFs_EfficienciesAndSF_GH,muonTrackingSFs_EfficienciesAndSF_BCDEFGH,metTrig_firstmethod]

sf_list_dict = {pileup2016histo:'pileup2016histo',eleTrig_hEffEtaPt:'eleTrig_hEffEtaPt',eleRecoSF_EGamma_SF2D_ptgt_20:'eleRecoSF_EGamma_SF2D_ptgt_20',eleRecoSF_EGamma_SF2D_ptlt_20:'eleRecoSF_EGamma_SF2D_ptlt_20',eleLooseIDSF_EGamma_SF2D:'eleLooseIDSF_EGamma_SF2D',eleTightIDSF_EGamma_SF2D:'eleTightIDSF_EGamma_SF2D',muonTrigSFs_EfficienciesAndSF_RunBtoF:'muonTrigSFs_EfficienciesAndSF_RunBtoF',muonTrigSFs_EfficienciesAndSF_Period4:'muonTrigSFs_EfficienciesAndSF_Period4',muonLooseIDSFs_EfficienciesAndSF_BCDEF:'muonLooseIDSFs_EfficienciesAndSF_BCDEF',muonLooseIDSFs_EfficienciesAndSF_GH:'muonLooseIDSFs_EfficienciesAndSF_GH',muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF:'muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF',muonLooseIDSFs_EfficienciesAndSF_lowpt_GH:'muonLooseIDSFs_EfficienciesAndSF_lowpt_GH',muonTightIDSFs_EfficienciesAndSF_BCDEF:'muonTightIDSFs_EfficienciesAndSF_BCDEF',muonTightIDSFs_EfficienciesAndSF_GH:'muonTightIDSFs_EfficienciesAndSF_GH',muonLooseIsoSFs_EfficienciesAndSF_BCDEF:'muonLooseIsoSFs_EfficienciesAndSF_BCDEF',muonLooseIsoSFs_EfficienciesAndSF_GH:'muonLooseIsoSFs_EfficienciesAndSF_GH',muonTightIsoSFs_EfficienciesAndSF_BCDEF:'muonTightIsoSFs_EfficienciesAndSF_BCDEF',muonTightIsoSFs_EfficienciesAndSF_GH:'muonTightIsoSFs_EfficienciesAndSF_GH',muonTrackingSFs_EfficienciesAndSF_BCDEFGH:'muonTrackingSFs_EfficienciesAndSF_BCDEFGH',metTrig_firstmethod:'metTrig_firstmethod'}

f= open("SFFactory_2016.py","w+")
for sf in sf_list:
    ptlist=[];ptlistUp=[];ptlistDown=[]
    Eta_range=[];pT_range=[]
    Eta_rangeDone=False;pT_rangeDone=False
    values=[]
    if sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_BCDEFGH':
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            if not Eta_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    ptlist.append(sf.Eval(xlow))
                    ptlist.append(sf.Eval(xhigh))
                    Eta_range.append(xlow)
                    Eta_range.append(xhigh)
                    Eta_rangeDone=True
                else:
                    ptlist.append(sf.Eval(xlow))
                    Eta_range.append(xlow)
    elif (sf_list_dict[sf]=='pileup2016histo') or (sf_list_dict[sf]=='metTrig_firstmethod'):
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            if not Eta_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    ptlist.append(sf.GetBinContent(sf.FindBin(xlow)))
                    ptlist.append(sf.GetBinContent(sf.FindBin(xhigh)))
                    Eta_range.append(xlow)
                    Eta_range.append(xhigh)
                    Eta_rangeDone=True
                else:
                    ptlist.append(sf.GetBinContent(sf.FindBin(xlow)))
                    Eta_range.append(xlow)
    else:
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            value=[]
            if not Eta_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    Eta_range.append(xlow)
                    Eta_range.append(xhigh)
                    Eta_rangeDone=True
                else:Eta_range.append(xlow)
            for biny in range(1,sf.GetYaxis().GetNbins()+1):
                ylow  = sf.GetYaxis().GetBinLowEdge(biny)#+yShift
                yhigh = sf.GetYaxis().GetBinUpEdge(biny)#-yShift
                if not pT_rangeDone:
                    if biny == sf.GetYaxis().GetNbins():
                        pT_range.append(ylow)
                        pT_range.append(yhigh)
                        pT_rangeDone=True
                    else:pT_range.append(ylow)
                value.append(sf.GetBinContent(binx,biny))
            values.append(value)
    print (sf_list_dict[sf]+'_X_range = ', Eta_range)
    print (sf_list_dict[sf]+'_Y_range = ', pT_range)
    print (sf_list_dict[sf])
    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_BCDEFGH')or (sf_list_dict[sf]=='pileup2016histo') or (sf_list_dict[sf]=='metTrig_firstmethod') or (sf_list_dict[sf]=='metTrig_secondmethod'):
        f.write(sf_list_dict[sf]+'_X_range = '+str(Eta_range)+'\n')
        f.write(str(sf_list_dict[sf])+"="+str(ptlist)+'\n')
    else:
        f.write(sf_list_dict[sf]+'_X_range = '+str(Eta_range)+'\n')
        f.write(sf_list_dict[sf]+'_Y_range = '+str(pT_range)+'\n')
        f.write(str(sf_list_dict[sf])+"="+str(values)+'\n')
    f.write ('\n')
    print ('\n')
f.close()

f_Up= open("SFFactorySystUp_2016.py","w+")
for sf in sf_list:
    ptlist=[];ptlistUp=[];ptlistDown=[]
    Eta_range=[];pT_range=[]
    Eta_rangeDone=False;pT_rangeDone=False
    values=[]
    if sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_BCDEFGH':
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            if not Eta_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    ptlist.append(sf.Eval(xlow)+sf.GetErrorYhigh(sf.GetYaxis().FindBin(xlow)))
                    ptlist.append(sf.Eval(xhigh)+sf.GetErrorYhigh(sf.GetYaxis().FindBin(xhigh)))
                    Eta_range.append(xlow)
                    Eta_range.append(xhigh)
                    Eta_rangeDone=True
                else:
                    ptlist.append(sf.Eval(xlow)+sf.GetErrorYhigh(sf.GetYaxis().FindBin(xlow)))
                    Eta_range.append(xlow)
    elif (sf_list_dict[sf]=='metTrig_firstmethod'):
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            if not Eta_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    ptlist.append(sf.GetBinContent(sf.FindBin(xlow))+(sf.GetBinContent(sf.FindBin(xlow))-metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    ptlist.append(sf.GetBinContent(sf.FindBin(xhigh))+(sf.GetBinContent(sf.FindBin(xlow))-metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    Eta_range.append(xlow)
                    Eta_range.append(xhigh)
                    Eta_rangeDone=True
                else:
                    ptlist.append(sf.GetBinContent(sf.FindBin(xlow))+(sf.GetBinContent(sf.FindBin(xlow))-metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    Eta_range.append(xlow)
    elif (sf_list_dict[sf]=='pileup2016histo'):
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            if not Eta_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    ptlist.append(sf.GetBinContent(sf.FindBin(xlow)))
                    ptlist.append(sf.GetBinContent(sf.FindBin(xhigh)))
                    Eta_range.append(xlow)
                    Eta_range.append(xhigh)
                    Eta_rangeDone=True
                else:
                    ptlist.append(sf.GetBinContent(sf.FindBin(xlow)))
                    Eta_range.append(xlow)
    elif (sf_list_dict[sf]=='eleTrig_hEffEtaPt'):
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            value=[]
            if not Eta_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    Eta_range.append(xlow)
                    Eta_range.append(xhigh)
                    Eta_rangeDone=True
                else:Eta_range.append(xlow)
            for biny in range(1,sf.GetYaxis().GetNbins()+1):
                ylow  = sf.GetYaxis().GetBinLowEdge(biny)#+yShift
                yhigh = sf.GetYaxis().GetBinUpEdge(biny)#-yShift
                if not pT_rangeDone:
                    if biny == sf.GetYaxis().GetNbins():
                        pT_range.append(ylow)
                        pT_range.append(yhigh)
                        pT_rangeDone=True
                    else:pT_range.append(ylow)
                value.append(sf.GetBinContent(binx,biny)+eleTrig_hEffEtaPtUp.GetBinContent(binx,biny))
            values.append(value)
    else:
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            value=[]
            if not Eta_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    Eta_range.append(xlow)
                    Eta_range.append(xhigh)
                    Eta_rangeDone=True
                else:Eta_range.append(xlow)
            for biny in range(1,sf.GetYaxis().GetNbins()+1):
                ylow  = sf.GetYaxis().GetBinLowEdge(biny)#+yShift
                yhigh = sf.GetYaxis().GetBinUpEdge(biny)#-yShift
                if not pT_rangeDone:
                    if biny == sf.GetYaxis().GetNbins():
                        pT_range.append(ylow)
                        pT_range.append(yhigh)
                        pT_rangeDone=True
                    else:pT_range.append(ylow)
                value.append(sf.GetBinContent(binx,biny)+sf.GetBinErrorUp(binx,biny))
            values.append(value)
    print (sf_list_dict[sf]+'_X_range = ', Eta_range)
    print (sf_list_dict[sf]+'_Y_range = ', pT_range)
    print (sf_list_dict[sf])
    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_BCDEFGH')or (sf_list_dict[sf]=='pileup2016histo') or (sf_list_dict[sf]=='metTrig_firstmethod'):
        f_Up.write(sf_list_dict[sf]+'_X_range = '+str(Eta_range)+'\n')
        f_Up.write(str(sf_list_dict[sf])+"_SystUp="+str(ptlist)+'\n')
    else:
        f_Up.write(sf_list_dict[sf]+'_X_range = '+str(Eta_range)+'\n')
        f_Up.write(sf_list_dict[sf]+'_Y_range = '+str(pT_range)+'\n')
        f_Up.write(str(sf_list_dict[sf])+"_SystUp="+str(values)+'\n')
    f_Up.write ('\n')
    print ('\n')
f_Up.close()

f_Down= open("SFFactorySystDown_2016.py","w+")
for sf in sf_list:
    ptlist=[];ptlistUp=[];ptlistDown=[]
    Eta_range=[];pT_range=[]
    Eta_rangeDone=False;pT_rangeDone=False
    values=[]
    if sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_BCDEFGH':
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            if not Eta_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    ptlist.append(sf.Eval(xlow)-sf.GetErrorYlow(sf.GetYaxis().FindBin(xlow)))
                    ptlist.append(sf.Eval(xhigh)-sf.GetErrorYlow(sf.GetYaxis().FindBin(xhigh)))
                    Eta_range.append(xlow)
                    Eta_range.append(xhigh)
                    Eta_rangeDone=True
                else:
                    ptlist.append(sf.Eval(xlow)-sf.GetErrorYlow(sf.GetYaxis().FindBin(xlow)))
                    Eta_range.append(xlow)
    elif (sf_list_dict[sf]=='metTrig_firstmethod'):
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            if not Eta_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    ptlist.append(sf.GetBinContent(sf.FindBin(xlow))-(sf.GetBinContent(sf.FindBin(xlow))-metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    ptlist.append(sf.GetBinContent(sf.FindBin(xhigh))-(sf.GetBinContent(sf.FindBin(xlow))-metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    Eta_range.append(xlow)
                    Eta_range.append(xhigh)
                    Eta_rangeDone=True
                else:
                    ptlist.append(sf.GetBinContent(sf.FindBin(xlow))-(sf.GetBinContent(sf.FindBin(xlow))-metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    Eta_range.append(xlow)
    elif (sf_list_dict[sf]=='pileup2016histo'):
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            if not Eta_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    ptlist.append(sf.GetBinContent(sf.FindBin(xlow)))
                    ptlist.append(sf.GetBinContent(sf.FindBin(xhigh)))
                    Eta_range.append(xlow)
                    Eta_range.append(xhigh)
                    Eta_rangeDone=True
                else:
                    ptlist.append(sf.GetBinContent(sf.FindBin(xlow)))
                    Eta_range.append(xlow)
    elif (sf_list_dict[sf]=='eleTrig_hEffEtaPt'):
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            value=[]
            if not Eta_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    Eta_range.append(xlow)
                    Eta_range.append(xhigh)
                    Eta_rangeDone=True
                else:Eta_range.append(xlow)
            for biny in range(1,sf.GetYaxis().GetNbins()+1):
                ylow  = sf.GetYaxis().GetBinLowEdge(biny)#+yShift
                yhigh = sf.GetYaxis().GetBinUpEdge(biny)#-yShift
                if not pT_rangeDone:
                    if biny == sf.GetYaxis().GetNbins():
                        pT_range.append(ylow)
                        pT_range.append(yhigh)
                        pT_rangeDone=True
                    else:pT_range.append(ylow)
                value.append(sf.GetBinContent(binx,biny)-eleTrig_hEffEtaPtDown.GetBinContent(binx,biny))
            values.append(value)
    else:
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            value=[]
            if not Eta_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    Eta_range.append(xlow)
                    Eta_range.append(xhigh)
                    Eta_rangeDone=True
                else:Eta_range.append(xlow)
            for biny in range(1,sf.GetYaxis().GetNbins()+1):
                ylow  = sf.GetYaxis().GetBinLowEdge(biny)#+yShift
                yhigh = sf.GetYaxis().GetBinUpEdge(biny)#-yShift
                if not pT_rangeDone:
                    if biny == sf.GetYaxis().GetNbins():
                        pT_range.append(ylow)
                        pT_range.append(yhigh)
                        pT_rangeDone=True
                    else:pT_range.append(ylow)
                value.append(sf.GetBinContent(binx,biny)-sf.GetBinErrorLow(binx,biny))
            values.append(value)
    print (sf_list_dict[sf]+'_X_range = ', Eta_range)
    print (sf_list_dict[sf]+'_Y_range = ', pT_range)
    print (sf_list_dict[sf])
    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_BCDEFGH')or (sf_list_dict[sf]=='pileup2016histo') or (sf_list_dict[sf]=='metTrig_firstmethod'):
        f_Down.write(sf_list_dict[sf]+'_X_range = '+str(Eta_range)+'\n')
        f_Down.write(str(sf_list_dict[sf])+"_SystDown="+str(ptlist)+'\n')
    else:
        f_Down.write(sf_list_dict[sf]+'_X_range = '+str(Eta_range)+'\n')
        f_Down.write(sf_list_dict[sf]+'_Y_range = '+str(pT_range)+'\n')
        f_Down.write(str(sf_list_dict[sf])+"_SystDown="+str(values)+'\n')
    f_Down.write ('\n')
    print ('\n')
f_Down.close()
