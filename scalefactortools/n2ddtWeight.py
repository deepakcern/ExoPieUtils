import ROOT as ROOT
import os,sys
# sys.path.append('../../ExoPieProducer/ExoPieAnalyzer/')
# from Year import era

f = ROOT.TFile(os.path.dirname(__file__)+'/data_2017/TH3_n2.root')
# f = ROOT.TFile('TH3_n2.root')
trans_h2ddt = f.Get("h_pt_rho")

def getN2bkgEff(fjetPt,fjetrho):
    cur_rho_index = trans_h2ddt.GetXaxis().FindBin(fjetrho);
    cur_pt_index  = trans_h2ddt.GetYaxis().FindBin(fjetPt);
    if fjetrho > trans_h2ddt.GetXaxis().GetBinUpEdge( trans_h2ddt.GetXaxis().GetNbins() ): cur_rho_index = trans_h2ddt.GetXaxis().GetNbins();
    if fjetrho < trans_h2ddt.GetXaxis().GetBinLowEdge( 1 ): cur_rho_index = 1;
    if fjetPt > trans_h2ddt.GetYaxis().GetBinUpEdge( trans_h2ddt.GetYaxis().GetNbins() ): cur_pt_index = trans_h2ddt.GetYaxis().GetNbins();
    if fjetPt < trans_h2ddt.GetYaxis().GetBinLowEdge( 1 ): cur_pt_index = 1;
    #print "N2 26%",trans_h2ddt.GetBinContent(cur_rho_index,cur_pt_index)
    return trans_h2ddt.GetBinContent(cur_rho_index,cur_pt_index);
