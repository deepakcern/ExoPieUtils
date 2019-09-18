from ROOT import TLatex

def EPLatex(latex_text="", x1=0.13, y1=0.92, ):
    latex2 =  TLatex();
    latex2.SetNDC();
    latex2.SetTextSize(0.04);
    latex2.SetTextAlign(31);
    latex2.SetTextAlign(11);
    latex2.SetTextFont(42);
    
    latex2.DrawLatex(x1, y1, latex_text);
    return latex2
    
