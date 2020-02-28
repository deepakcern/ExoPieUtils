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
pileup2018file = TFile('data_2018/PU_Reweight_2018.root')
pileup2018histo=pileup2018file.Get('puweight')
pileup2018histo_up=pileup2018file.Get('puweight_Up')
pileup2018histo_down=pileup2018file.Get('puweight_Down')

#Electron Trigger reweights
eleTrigReweightFile = TFile('data_2018/electron_Trigger_eleTrig_2018.root')
eleTrig_hEffEtaPt = eleTrigReweightFile.Get('EGamma_SF2D')

#Electron Reconstruction efficiency. Scale factors for 10X
eleRecoSFsFile = TFile('data_2018/electron_Reco_SFs_egammaEffi_txt_EGM2D_2018.root')
eleRecoSF_EGamma_SF2D = eleRecoSFsFile.Get('EGamma_SF2D')

# eleRecoSFsFile_ptlt_20 = TFile('data_2018/egammaEffitxt_EGM2D_runABCD_passingRECO_lowEt_2017.root')
# eleRecoSF_EGamma_SF2D_ptlt_20 = eleRecoSFsFile_ptlt_20.Get('EGamma_SF2D')

#Loose electron ID SFs
eleLooseIDSFsFile = TFile('data_2018/2018_ElectronLoose.root')
eleLooseIDSF_EGamma_SF2D = eleLooseIDSFsFile.Get('EGamma_SF2D')

#Tight Electron ID SFs
eleTightIDSFsFile = TFile('data_2018/2018_ElectronTight.root')
eleTightIDSF_EGamma_SF2D = eleTightIDSFsFile.Get('EGamma_SF2D')

#Tight photon ID SFs
phoTightIDSFsFile = TFile('data_2018/2018_PhotonsTight.root')
phoTightIDSF_EGamma_SF2D = phoTightIDSFsFile.Get('EGamma_SF2D')

#Loose photon ID SFs
phoLooseIDSFsFile = TFile('data_2018/2018_PhotonsLoose.root')
phoLooseIDSF_EGamma_SF2D = phoLooseIDSFsFile.Get('EGamma_SF2D')

#Muon Trigger SFs
#Before HLT update run< 316361
muonTrigSFsBeforeHLTupdateFile = TFile('data_2018/muon_EfficienciesStudies_trigger_EfficienciesAndSF_BeforeMuonHLTUpdate_2018.root')
muonTrigSFs_bHLTupdate = muonTrigSFsBeforeHLTupdateFile.Get('IsoMu24_PtEtaBins/abseta_pt_ratio')
#After HLT update run > 316361
muonTrigSFsaHLTupdateFile = TFile('data_2018/muon_EfficienciesStudies_trigger_EfficienciesAndSF_AfterMuonHLTUpdate_2018.root')
muonTrigSFs_aHLTupdate = muonTrigSFsaHLTupdateFile.Get('IsoMu24_PtEtaBins/abseta_pt_ratio')

#Muon ID SFs
muonIDSFsABCDFile = TFile('data_2018/muon_EfficienciesStudies_rootfiles_RunABCD_SF_ID_2018.root')
muonLooseIDSFs_EfficienciesAndSF_ABCD = muonIDSFsABCDFile.Get('NUM_LooseID_DEN_TrackerMuons_pt_abseta')
muonTightIDSFs_EfficienciesAndSF_ABCD = muonIDSFsABCDFile.Get('NUM_TightID_DEN_TrackerMuons_pt_abseta')

#for low pt muons
muonIDSFsABCDFile_lowpt = TFile('data_2018/muon_EfficienciesStudies_Jpsi_rootfiles_RunABCD_SF_ID_2018.root')
muonLooseIDSFs_EfficienciesAndSF_lowpt_ABCD = muonIDSFsABCDFile_lowpt.Get('NUM_LooseID_DEN_genTracks_pt_abseta')

#Muon Iso SFs
muonIsoSFsABCDFile = TFile('data_2018/muon_EfficienciesStudies_rootfiles_RunABCD_SF_ISO_2018.root')
muonLooseIsoSFs_EfficienciesAndSF_ABCD = muonIsoSFsABCDFile.Get('NUM_LooseRelIso_DEN_LooseID_pt_abseta')
muonTightIsoSFs_EfficienciesAndSF_ABCD = muonIsoSFsABCDFile.Get('NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta')

#Muon Tracking SFs
muonTrackingSFsFile = TFile('data_2018/muon_Tracking_SFs_Tracking_EfficienciesAndSF_BCDEF_2016.root')
muonTrackingSFs_EfficienciesAndSF_ABCD = muonTrackingSFsFile.Get('ratio_eff_aeta_dr030e030_corr')

#MET Trigger reweights
metTrigEff_zmmfile = TFile('data_2018/TriggerEff_MET2017.root')
metTrig_firstmethod = metTrigEff_zmmfile.Get('Wmunu')

metTrigEff_secondfile = TFile('data_2018/TriggerEff_MET2017.root')
metTrig_secondmethod = metTrigEff_secondfile.Get('Zmumu')
sf_list = [pileup2018histo,eleTrig_hEffEtaPt,eleRecoSF_EGamma_SF2D,eleLooseIDSF_EGamma_SF2D,eleTightIDSF_EGamma_SF2D,muonTrigSFs_bHLTupdate,muonTrigSFs_aHLTupdate,muonLooseIDSFs_EfficienciesAndSF_ABCD,muonLooseIDSFs_EfficienciesAndSF_lowpt_ABCD,muonTightIDSFs_EfficienciesAndSF_ABCD,muonLooseIsoSFs_EfficienciesAndSF_ABCD,muonTightIsoSFs_EfficienciesAndSF_ABCD,muonTrackingSFs_EfficienciesAndSF_ABCD,metTrig_firstmethod]

sf_list_dict = {pileup2018histo:'pileup2018histo',eleTrig_hEffEtaPt:'eleTrig_hEffEtaPt',eleRecoSF_EGamma_SF2D:'eleRecoSF_EGamma_SF2D',eleLooseIDSF_EGamma_SF2D:'eleLooseIDSF_EGamma_SF2D',eleTightIDSF_EGamma_SF2D:'eleTightIDSF_EGamma_SF2D',muonTrigSFs_bHLTupdate:'muonTrigSFs_bHLTupdate',muonTrigSFs_aHLTupdate:'muonTrigSFs_aHLTupdate',muonLooseIDSFs_EfficienciesAndSF_ABCD:'muonLooseIDSFs_EfficienciesAndSF_ABCD',muonLooseIDSFs_EfficienciesAndSF_lowpt_ABCD:'muonLooseIDSFs_EfficienciesAndSF_lowpt_ABCD',muonTightIDSFs_EfficienciesAndSF_ABCD:'muonTightIDSFs_EfficienciesAndSF_ABCD',muonLooseIsoSFs_EfficienciesAndSF_ABCD:'muonLooseIsoSFs_EfficienciesAndSF_ABCD',muonTightIsoSFs_EfficienciesAndSF_ABCD:'muonTightIsoSFs_EfficienciesAndSF_ABCD',muonTrackingSFs_EfficienciesAndSF_ABCD:'muonTrackingSFs_EfficienciesAndSF_ABCD',metTrig_firstmethod:'metTrig_firstmethod'}


f= open("SFFactory_2018.py","w+")
for sf in sf_list:
    ptlist=[];ptlistUp=[];ptlistDown=[]
    Eta_range=[];pT_range=[]
    Eta_rangeDone=False;pT_rangeDone=False;X_rangeDone=False
    X_range =[];Efficiency =[]
    values=[]
    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_ABCD') or (sf_list_dict[sf]=='metTrig_firstmethod'):
        for point in range(sf.GetN()):
            x, y = ROOT.Double(0), ROOT.Double(0)
            sf.GetPoint(point,x,y)
            X_range.append(x)
            Efficiency.append(y)

    elif (sf_list_dict[sf]=='pileup2018histo'):
        Efficiency.append(0.0)
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            if not X_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xlow)))
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xhigh)))
                    X_range.append(xlow)
                    X_range.append(xhigh)
                    X_rangeDone=True
                else:
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xlow)))
                    X_range.append(xlow)
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
    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_ABCD') or (sf_list_dict[sf]=='pileup2018histo') or (sf_list_dict[sf]=='metTrig_firstmethod'):
        f.write(sf_list_dict[sf]+'_X_range = '+str(X_range)+'\n')
        f.write(str(sf_list_dict[sf])+"="+str(Efficiency)+'\n')
    else:
        f.write(sf_list_dict[sf]+'_X_range = '+str(Eta_range)+'\n')
        f.write(sf_list_dict[sf]+'_Y_range = '+str(pT_range)+'\n')
        f.write(str(sf_list_dict[sf])+"="+str(values)+'\n')
    f.write ('\n')
f.close()

f_Up= open("SFFactorySystUp_2018.py","w+")
for sf in sf_list:
    ptlist=[];ptlistUp=[];ptlistDown=[]
    Eta_range=[];pT_range=[]
    Eta_rangeDone=False;pT_rangeDone=False;X_rangeDone=False
    X_range =[];Efficiency =[]
    values=[]
    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_ABCD'):
        for point in range(sf.GetN()):
            x, y = ROOT.Double(0), ROOT.Double(0)
            sf.GetPoint(point,x,y)
            X_range.append(x)
            Efficiency.append(y+sf.GetErrorYhigh(point))

    elif (sf_list_dict[sf]=='metTrig_firstmethod'):
        for point in range(sf.GetN()):
            x, y = ROOT.Double(0), ROOT.Double(0)
            x1, y1 = ROOT.Double(0), ROOT.Double(0)
            sf.GetPoint(point,x,y); metTrig_secondmethod.GetPoint(point,x1,y1)
            X_range.append(x)
            Efficiency.append(y+abs(y-y1))

    elif (sf_list_dict[sf]=='pileup2018histo'):
        Efficiency.append(0.0)
        for binx in range(1,pileup2018histo_up.GetXaxis().GetNbins()+1):
            xlow  = pileup2018histo_up.GetXaxis().GetBinLowEdge(binx)
            xhigh = pileup2018histo_up.GetXaxis().GetBinUpEdge(binx)
            if not X_rangeDone:
                if binx == pileup2018histo_up.GetXaxis().GetNbins():
                    Efficiency.append(pileup2018histo_up.GetBinContent(pileup2018histo_up.FindBin(xlow)))
                    Efficiency.append(pileup2018histo_up.GetBinContent(pileup2018histo_up.FindBin(xhigh)))
                    X_range.append(xlow)
                    X_range.append(xhigh)
                    X_rangeDone=True
                else:
                    Efficiency.append(pileup2018histo_up.GetBinContent(pileup2018histo_up.FindBin(xlow)))
                    X_range.append(xlow)
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
    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_ABCD')or (sf_list_dict[sf]=='pileup2018histo') or (sf_list_dict[sf]=='metTrig_firstmethod'):
        f_Up.write(sf_list_dict[sf]+'_X_range = '+str(X_range)+'\n')
        f_Up.write(str(sf_list_dict[sf])+"_SystUp="+str(Efficiency)+'\n')
    else:
        f_Up.write(sf_list_dict[sf]+'_X_range = '+str(Eta_range)+'\n')
        f_Up.write(sf_list_dict[sf]+'_Y_range = '+str(pT_range)+'\n')
        f_Up.write(str(sf_list_dict[sf])+"_SystUp="+str(values)+'\n')
    f_Up.write ('\n')
f_Up.close()

f_Down= open("SFFactorySystDown_2018.py","w+")
for sf in sf_list:
    ptlist=[];ptlistUp=[];ptlistDown=[]
    Eta_range=[];pT_range=[]
    Eta_rangeDone=False;pT_rangeDone=False;X_rangeDone=False
    X_range =[];Efficiency =[]
    values=[]
    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_ABCD'):
        for point in range(sf.GetN()):
            x, y = ROOT.Double(0), ROOT.Double(0)
            sf.GetPoint(point,x,y)
            X_range.append(x)
            Efficiency.append(y-sf.GetErrorYlow(point))

    elif (sf_list_dict[sf]=='metTrig_firstmethod'):
        for point in range(sf.GetN()):
            x, y = ROOT.Double(0), ROOT.Double(0)
            x1, y1 = ROOT.Double(0), ROOT.Double(0)
            sf.GetPoint(point,x,y); metTrig_secondmethod.GetPoint(point,x1,y1)
            X_range.append(x)
            Efficiency.append(y-abs(y-y1))

    elif (sf_list_dict[sf]=='pileup2018histo'):
        Efficiency.append(0.0)
        for binx in range(1,pileup2018histo_down.GetXaxis().GetNbins()+1):
            xlow  = pileup2018histo_down.GetXaxis().GetBinLowEdge(binx)
            xhigh = pileup2018histo_down.GetXaxis().GetBinUpEdge(binx)
            if not X_rangeDone:
                if binx == pileup2018histo_down.GetXaxis().GetNbins():
                    Efficiency.append(pileup2018histo_down.GetBinContent(pileup2018histo_down.FindBin(xlow)))
                    Efficiency.append(pileup2018histo_down.GetBinContent(pileup2018histo_down.FindBin(xhigh)))
                    X_range.append(xlow)
                    X_range.append(xhigh)
                    X_rangeDone=True
                else:
                    Efficiency.append(pileup2018histo_down.GetBinContent(pileup2018histo_down.FindBin(xlow)))
                    X_range.append(xlow)
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
    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_ABCD')or (sf_list_dict[sf]=='pileup2018histo') or (sf_list_dict[sf]=='metTrig_firstmethod'):
        f_Down.write(sf_list_dict[sf]+'_X_range = '+str(X_range)+'\n')
        f_Down.write(str(sf_list_dict[sf])+"_SystDown="+str(Efficiency)+'\n')
    else:
        f_Down.write(sf_list_dict[sf]+'_X_range = '+str(Eta_range)+'\n')
        f_Down.write(sf_list_dict[sf]+'_Y_range = '+str(pT_range)+'\n')
        f_Down.write(str(sf_list_dict[sf])+"_SystDown="+str(values)+'\n')
    f_Down.write ('\n')
f_Down.close()
