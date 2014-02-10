import os
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def load_data(path):
    data=np.loadtxt(path,skiprows=0)
    x=np.array([row[0]for row in data])
    y=np.array([row[1]for row in data])
    
    return data,x,y
    
def plot_data(x,y,title='x vs y',xlabel='x',ylabel='y'):
    """takes the input data as a numpy array and plots a simple graph"""
    
    

    fig=plt.figure(figsize=(10,8))
    sub=plt.subplot(1,1,1)
    
    sub.plot(x,y,"bo")
    
    
    sub.axis([min(x),max(x),min(y),max(y)])
    
    
    sub.set_title(title)
    
    sub.set_xlabel(xlabel)
    sub.set_ylabel(ylabel)

    
    return fig
    
def fit1(x,y,title="Sample"):
    
    """fits to the data in an x,y format, a curve of the form b*(1-np.exp(a*x)) and plots that curve against the data.
    Also plots the plus sigma and minus sigma curves for that data,
    as well as all the plotted curves equations.
    """
    
    def functn(x,a,b):
        return b*(1-np.exp(a*x))
       
    
        
    
        
    par,covar=curve_fit(functn,x,y,p0=[-.1,5]) #par(ameters) and covar(iance) matrix
    stdeva=np.sqrt(covar[0,0])
    stdevb=np.sqrt(covar[1,1])
    tconst=np.abs(1.0/par[0])
    tconstplus=np.abs(1.0/(par[0]-stdeva))
    tconstmin=np.abs(1.0/(par[0]+stdeva))
    stdevtconst=np.abs(stdeva/par[0]*tconst)
    #standard deviations of parameters and the associated time constants=1/par
    

    x_range=np.arange(min(x),max(x)*1.2,1)
        
    yfit=functn(x_range,par[0],par[1])
    yfitplus=(par[1]-stdevb)*(1-np.exp((par[0]+stdeva)*x_range))
    yfitmin=(par[1]+stdevb)*(1-np.exp((par[0]-stdeva)*x_range))
    #y values for the fitted function curve and sigma plus/minus curves
    
    eqstrmin = r"$y= "+str(round(par[1]+stdeva,3))+"(1-e^{-x/("+str(round(tconstmin))+")})$"
    eqstrplus= r"$y= "+str(round(par[1]-stdeva,3))+"(1-e^{-x/("+str(round(tconstplus))+")})$"
    eqstr  =   r"$y= "+str(round(par[1],3))+"(1-e^{(-x/"+str(round(tconst))+")})$"    
    #raw strings in a LaTeX format for the equations of the fit and sigma plus/minus curves
    
    fig=plt.figure(figsize=(10,8))

    sub=plt.subplot(1,1,1)

    
   
    sub.plot(x,y,"bo",x_range,yfit,"b-",x_range,yfitplus,"g--",x_range,yfitmin,"r--")
    sub.axis([min(x),max(x)*1.2,min(y),max(y)*1.2])
    
    sub.text(.3, .4,eqstrmin,color="red",size=18, horizontalalignment='left',\
         verticalalignment='center',transform=sub.transAxes)
    sub.text(.3, .35,eqstr,color="blue",size=18, horizontalalignment='left',\
         verticalalignment='center',transform=sub.transAxes)
    sub.text(.3, .3,eqstrplus,color="green",size=18, horizontalalignment='left',\
         verticalalignment='center',transform=sub.transAxes)
    sub.text(.02, .9,"time constant = "+str(int(tconst))+r"  $\pm$  "+str(int(stdevtconst))+" seconds",size=14, horizontalalignment='left',\
            verticalalignment='center',transform=sub.transAxes)

    sub.set_title(title)
    
    sub.set_xlabel("Irradiation time (s)")
    sub.set_ylabel("R")
    
    print "curve fit to equation  :   "+"b*(1-exp(a*x))"
    print "the value of a is :  "+str(par[0])+"   pm   "+str(stdeva)
    print "the value of b is :  "+str(par[1])+"   pm   "+str(stdevb)
    print "the time constant is :  "+str(tconst)+"   pm   "+str(stdevtconst)
    #above are for debugging, or where very accurate values are required
    
    
    if os.path.isdir("plots")==False:
        os.system("mkdir plots")
    
    
    name=title+".pdf"
    fig.savefig("plots/"+name,format="pdf")
        
    




def fit2(x,y,title="Sample"):
    
    
    def functn(x,a,b,c,d):
        return a*np.exp(b(-x+c))+d
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       

    





