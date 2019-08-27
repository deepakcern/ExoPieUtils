from ROOT import TCanvas 
def EPCanvas(logx=0, logy=0, lm=0.12, rm=0.06, tm=0.10, bm=0.08 ):
    
    c = TCanvas("c","c",800, 800)
    
    c.SetTicks()
    
    c.SetLogy(logy)
    c.SetLogx(logx)
    
    c.SetLeftMargin(lm)
    c.SetRightMargin(rm)
    c.SetTopMargin(tm)
    c.SetBottomMargin(bm)
    
    return c
    
def EPCanvasRatio(logx=0, logy=0, lm=0.12, rm=0.06, tm=0.10, bm=0.08):
    ## modify it as per needs 
    c = TCanvas("c","c",800, 800)
    
    c.SetTicks()
    
    c.SetLogy(logy)
    c.SetLogx(logx)
    
    c.SetLeftMargin(lm)
    c.SetRightMargin(rm)
    c.SetTopMargin(tm)
    c.SetBottomMargin(bm)
    
    return c
    







