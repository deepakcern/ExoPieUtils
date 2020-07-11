#coded by Praveen
#Deepak
from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, TF1, AddressOf
import ROOT as ROOT
import os
import random
import sys, optparse
from array import array
import math

ROOT.gROOT.SetBatch(True)

#pileup reweights
pileup2017file = TFile('data_2017/PU_Reweight_2017.root')
pileup2017histo=pileup2017file.Get('puweight')
pileup2017histo_up=pileup2017file.Get('puweight_Up')
pileup2017histo_down=pileup2017file.Get('puweight_Down')

#Electron Trigger reweights
eleTrigReweightFile = TFile('data_2017/electron_Trigger_eleTrig_2017.root')
eleTrig_hEffEtaPt = eleTrigReweightFile.Get('EGamma_SF2D')


#Electron Reconstruction efficiency. Scale factors for 80X
eleRecoSFsFile_ptgt_20 = TFile('data_2017/electron_Reco_SFs_egammaEffi_txt_EGM2D_2017.root')
eleRecoSF_EGamma_SF2D_ptgt_20 = eleRecoSFsFile_ptgt_20.Get('EGamma_SF2D')

eleRecoSFsFile_ptlt_20 = TFile('data_2017/egammaEffitxt_EGM2D_runBCDEF_passingRECO_lowEt_2017.root')
eleRecoSF_EGamma_SF2D_ptlt_20 = eleRecoSFsFile_ptlt_20.Get('EGamma_SF2D')

#Loose electron ID SFs
eleLooseIDSFsFile = TFile('data_2017/2017_ElectronLoose.root')
eleLooseIDSF_EGamma_SF2D = eleLooseIDSFsFile.Get('EGamma_SF2D')

#Tight Electron ID SFs
eleTightIDSFsFile = TFile('data_2017/2017_ElectronTight.root')
eleTightIDSF_EGamma_SF2D = eleTightIDSFsFile.Get('EGamma_SF2D')

#Tight photon ID SFs
phoTightIDSFsFile = TFile('data_2017/photon_Tight_ID_SFs_egammaEffi_txt_EGM2D_2017.root')
phoTightIDSF_EGamma_SF2D = phoTightIDSFsFile.Get('EGamma_SF2D')

#Loose photon ID SFs
phoLooseIDSFsFile = TFile('data_2017/photon_Loose_ID_SFs_egammaEffi_txt_EGM2D_2017.root')
phoLooseIDSF_EGamma_SF2D = phoLooseIDSFsFile.Get('EGamma_SF2D')

#Muon Trigger SFs
muonTrigSFsRunBCDEFFile = TFile('data_2017/muon_single_lepton_trigger_EfficienciesAndSF_2017.root')
muonTrigSFs_EfficienciesAndSF_RunBtoF = muonTrigSFsRunBCDEFFile.Get('IsoMu27_PtEtaBins/abseta_pt_ratio')

#Muon ID SFs
muonIDSFsBCDEFFile = TFile('data_2017/muon_ID_SFs_EfficienciesAndSF_BCDEF_2017.root')
muonLooseIDSFs_EfficienciesAndSF_BCDEF = muonIDSFsBCDEFFile.Get('NUM_LooseID_DEN_genTracks_pt_abseta')
muonTightIDSFs_EfficienciesAndSF_BCDEF = muonIDSFsBCDEFFile.Get('NUM_TightID_DEN_genTracks_pt_abseta')

#for low pt muons
muonIDSFsBCDEFFile_lowpt = TFile('data_2017/Muon_low-pT_RunBCDEF_SF_ID_JPsi_2017.root')
muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF = muonIDSFsBCDEFFile_lowpt.Get('NUM_LooseID_DEN_genTracks_pt_abseta')

#Muon Iso SFs
muonIsoSFsBCDEFFile = TFile('data_2017/muon_Iso_SFs_EfficienciesAndSF_BCDEF_2017.root')
muonLooseIsoSFs_EfficienciesAndSF_BCDEF = muonIsoSFsBCDEFFile.Get('NUM_LooseRelIso_DEN_LooseID_pt_abseta')
muonTightIsoSFs_EfficienciesAndSF_BCDEF = muonIsoSFsBCDEFFile.Get('NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta')

#Muon Tracking SFs
muonTrackingSFsFile = TFile('data_2017/muon_Tracking_SFs_Tracking_EfficienciesAndSF_BCDEF_2016.root')
muonTrackingSFs_EfficienciesAndSF_BCDEFGH = muonTrackingSFsFile.Get('ratio_eff_aeta_dr030e030_corr')


#MET Trigger reweights
R_metTrigEff_zmmfile = TFile('data_2017/2017_MET_Trigger_SF_R.root')
R_metTrig_firstmethod = R_metTrigEff_zmmfile.Get('Wmunu')

R_metTrigEff_secondfile = TFile('data_2017/2017_MET_Trigger_SF_R.root')
R_metTrig_secondmethod = R_metTrigEff_secondfile.Get('Zmumu')


B_metTrigEff_zmmfile = TFile('data_2017/2017_MET_Trigger_SF_B.root')
B_metTrig_firstmethod = B_metTrigEff_zmmfile.Get('Wmunu')

B_metTrigEff_secondfile = TFile('data_2017/2017_MET_Trigger_SF_B.root')
B_metTrig_secondmethod = B_metTrigEff_secondfile.Get('Zmumu')



sf_list = [pileup2017histo,eleTrig_hEffEtaPt,eleRecoSF_EGamma_SF2D_ptgt_20,eleRecoSF_EGamma_SF2D_ptlt_20,eleLooseIDSF_EGamma_SF2D,eleTightIDSF_EGamma_SF2D,muonTrigSFs_EfficienciesAndSF_RunBtoF,muonLooseIDSFs_EfficienciesAndSF_BCDEF,muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF,muonTightIDSFs_EfficienciesAndSF_BCDEF,muonLooseIsoSFs_EfficienciesAndSF_BCDEF,muonTightIsoSFs_EfficienciesAndSF_BCDEF,muonTrackingSFs_EfficienciesAndSF_BCDEFGH,R_metTrig_firstmethod,B_metTrig_firstmethod]

sf_list_dict = {pileup2017histo:'pileup2017histo',eleTrig_hEffEtaPt:'eleTrig_hEffEtaPt',eleRecoSF_EGamma_SF2D_ptgt_20:'eleRecoSF_EGamma_SF2D_ptgt_20',eleRecoSF_EGamma_SF2D_ptlt_20:'eleRecoSF_EGamma_SF2D_ptlt_20',eleLooseIDSF_EGamma_SF2D:'eleLooseIDSF_EGamma_SF2D',eleTightIDSF_EGamma_SF2D:'eleTightIDSF_EGamma_SF2D',muonTrigSFs_EfficienciesAndSF_RunBtoF:'muonTrigSFs_EfficienciesAndSF_RunBtoF',muonLooseIDSFs_EfficienciesAndSF_BCDEF:'muonLooseIDSFs_EfficienciesAndSF_BCDEF',muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF:'muonLooseIDSFs_EfficienciesAndSF_lowpt_BCDEF',muonTightIDSFs_EfficienciesAndSF_BCDEF:'muonTightIDSFs_EfficienciesAndSF_BCDEF',muonLooseIsoSFs_EfficienciesAndSF_BCDEF:'muonLooseIsoSFs_EfficienciesAndSF_BCDEF',muonTightIsoSFs_EfficienciesAndSF_BCDEF:'muonTightIsoSFs_EfficienciesAndSF_BCDEF',muonTrackingSFs_EfficienciesAndSF_BCDEFGH:'muonTrackingSFs_EfficienciesAndSF_BCDEFGH',R_metTrig_firstmethod:'R_metTrig_firstmethod',B_metTrig_firstmethod:'B_metTrig_firstmethod'}


f= open("SFFactory_2017.py","w+")
for sf in sf_list:
    ptlist=[];ptlistUp=[];ptlistDown=[]
    Eta_range=[];pT_range=[]
    Eta_rangeDone=False;pT_rangeDone=False;X_rangeDone=False
    X_range =[];Efficiency =[]
    values=[]

    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_BCDEFGH'):
        for point in range(sf.GetN()):
            x, y = ROOT.Double(0), ROOT.Double(0)
            sf.GetPoint(point,x,y)
            X_range.append(x)
            Efficiency.append(y)

    elif (sf_list_dict[sf]=='pileup2017histo') or (sf_list_dict[sf]=='R_metTrig_firstmethod') or (sf_list_dict[sf]=='B_metTrig_firstmethod'):
        if (sf_list_dict[sf]=='pileup2017histo'):Efficiency.append(0.0)
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


    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_BCDEFGH') or (sf_list_dict[sf]=='pileup2017histo') or (sf_list_dict[sf]=='R_metTrig_firstmethod') or (sf_list_dict[sf]=='B_metTrig_firstmethod'):
        f.write(sf_list_dict[sf]+'_X_range = '+str(X_range)+'\n')
        f.write(str(sf_list_dict[sf])+"="+str(Efficiency)+'\n')
    else:
        f.write(sf_list_dict[sf]+'_X_range = '+str(Eta_range)+'\n')
        f.write(sf_list_dict[sf]+'_Y_range = '+str(pT_range)+'\n')
        f.write(str(sf_list_dict[sf])+"="+str(values)+'\n')
    f.write ('\n')
f.close()

f_Up= open("SFFactorySystUp_2017.py","w+")
for sf in sf_list:
    ptlist=[];ptlistUp=[];ptlistDown=[]
    Eta_range=[];pT_range=[]
    Eta_rangeDone=False;pT_rangeDone=False;X_rangeDone=False
    X_range =[];Efficiency =[]
    values=[]
    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_BCDEFGH'):
        for point in range(sf.GetN()):
            x, y = ROOT.Double(0), ROOT.Double(0)
            sf.GetPoint(point,x,y)
            X_range.append(x)
            Efficiency.append(y+sf.GetErrorYhigh(point))

    elif (sf_list_dict[sf]=='R_metTrig_firstmethod'):
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            if not X_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xlow))+abs(sf.GetBinContent(sf.FindBin(xlow))-R_metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xhigh))+abs(sf.GetBinContent(sf.FindBin(xlow))-R_metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    X_range.append(xlow)
                    X_range.append(xhigh)
                    X_rangeDone=True
                else:
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xlow))+abs(sf.GetBinContent(sf.FindBin(xlow))-R_metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    X_range.append(xlow)

    elif (sf_list_dict[sf]=='B_metTrig_firstmethod'):
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            if not X_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xlow))+abs(sf.GetBinContent(sf.FindBin(xlow))-B_metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xhigh))+abs(sf.GetBinContent(sf.FindBin(xlow))-B_metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    X_range.append(xlow)
                    X_range.append(xhigh)
                    X_rangeDone=True
                else:
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xlow))+abs(sf.GetBinContent(sf.FindBin(xlow))-B_metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    X_range.append(xlow)


    elif (sf_list_dict[sf]=='pileup2017histo'):
        Efficiency.append(0.0)
        for binx in range(1,pileup2017histo_up.GetXaxis().GetNbins()+1):
            xlow  = pileup2017histo_up.GetXaxis().GetBinLowEdge(binx)
            xhigh = pileup2017histo_up.GetXaxis().GetBinUpEdge(binx)
            if not X_rangeDone:
                if binx == pileup2017histo_up.GetXaxis().GetNbins():
                    Efficiency.append(pileup2017histo_up.GetBinContent(pileup2017histo_up.FindBin(xlow)))
                    Efficiency.append(pileup2017histo_up.GetBinContent(pileup2017histo_up.FindBin(xhigh)))
                    X_range.append(xlow)
                    X_range.append(xhigh)
                    X_rangeDone=True
                else:
                    Efficiency.append(pileup2017histo_up.GetBinContent(sf.FindBin(xlow)))
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

    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_BCDEFGH')or (sf_list_dict[sf]=='pileup2017histo') or (sf_list_dict[sf]=='R_metTrig_firstmethod') or (sf_list_dict[sf]=='B_metTrig_firstmethod'):
        f_Up.write(sf_list_dict[sf]+'_X_range = '+str(X_range)+'\n')
        f_Up.write(str(sf_list_dict[sf])+"_SystUp="+str(Efficiency)+'\n')
    else:
        f_Up.write(sf_list_dict[sf]+'_X_range = '+str(Eta_range)+'\n')
        f_Up.write(sf_list_dict[sf]+'_Y_range = '+str(pT_range)+'\n')
        f_Up.write(str(sf_list_dict[sf])+"_SystUp="+str(values)+'\n')
    f_Up.write ('\n')
f_Up.close()

f_Down= open("SFFactorySystDown_2017.py","w+")
for sf in sf_list:
    ptlist=[];ptlistUp=[];ptlistDown=[]
    Eta_range=[];pT_range=[]
    Eta_rangeDone=False;pT_rangeDone=False;X_rangeDone=False
    X_range =[];Efficiency =[]
    values=[]

    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_BCDEFGH'):
        for point in range(sf.GetN()):
            x, y = ROOT.Double(0), ROOT.Double(0)
            sf.GetPoint(point,x,y)
            X_range.append(x)
            Efficiency.append(y-sf.GetErrorYlow(point))

    elif (sf_list_dict[sf]=='R_metTrig_firstmethod'):
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            if not X_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xlow))-abs(sf.GetBinContent(sf.FindBin(xlow))-R_metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xhigh))-abs(sf.GetBinContent(sf.FindBin(xlow))-R_metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    X_range.append(xlow)
                    X_range.append(xhigh)
                    X_rangeDone=True
                else:
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xlow))-abs(sf.GetBinContent(sf.FindBin(xlow))-R_metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    X_range.append(xlow)

    elif (sf_list_dict[sf]=='B_metTrig_firstmethod'):
        for binx in range(1,sf.GetXaxis().GetNbins()+1):
            xlow  = sf.GetXaxis().GetBinLowEdge(binx)
            xhigh = sf.GetXaxis().GetBinUpEdge(binx)
            if not X_rangeDone:
                if binx == sf.GetXaxis().GetNbins():
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xlow))-abs(sf.GetBinContent(sf.FindBin(xlow))-B_metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xhigh))-abs(sf.GetBinContent(sf.FindBin(xlow))-B_metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    X_range.append(xlow)
                    X_range.append(xhigh)
                    X_rangeDone=True
                else:
                    Efficiency.append(sf.GetBinContent(sf.FindBin(xlow))-abs(sf.GetBinContent(sf.FindBin(xlow))-B_metTrig_secondmethod.GetBinContent(sf.FindBin(xlow))))
                    X_range.append(xlow)

    elif (sf_list_dict[sf]=='pileup2017histo'):
        Efficiency.append(0.0)
        for binx in range(1,pileup2017histo_down.GetXaxis().GetNbins()+1):
            xlow  = pileup2017histo_down.GetXaxis().GetBinLowEdge(binx)
            xhigh = pileup2017histo_down.GetXaxis().GetBinUpEdge(binx)
            if not X_rangeDone:
                if binx == pileup2017histo_down.GetXaxis().GetNbins():
                    Efficiency.append(pileup2017histo_down.GetBinContent(pileup2017histo_down.FindBin(xlow)))
                    Efficiency.append(pileup2017histo_down.GetBinContent(pileup2017histo_down.FindBin(xhigh)))
                    X_range.append(xlow)
                    X_range.append(xhigh)
                    X_rangeDone=True
                else:
                    Efficiency.append(pileup2017histo_down.GetBinContent(pileup2017histo_down.FindBin(xlow)))
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

    if (sf_list_dict[sf]=='muonTrackingSFs_EfficienciesAndSF_BCDEFGH')or (sf_list_dict[sf]=='pileup2017histo') or (sf_list_dict[sf]=='R_metTrig_firstmethod') or (sf_list_dict[sf]=='B_metTrig_firstmethod'):
        f_Down.write(sf_list_dict[sf]+'_X_range = '+str(X_range)+'\n')
        f_Down.write(str(sf_list_dict[sf])+"_SystDown="+str(Efficiency)+'\n')
    else:
        f_Down.write(sf_list_dict[sf]+'_X_range = '+str(Eta_range)+'\n')
        f_Down.write(sf_list_dict[sf]+'_Y_range = '+str(pT_range)+'\n')
        f_Down.write(str(sf_list_dict[sf])+"_SystDown="+str(values)+'\n')
    f_Down.write ('\n')
f_Down.close()
