import numpy as np

import matplotlib.pyplot as plt

import os


def plot(path,skip=0,title='x vs y',xlabel='x',ylabel='y'):
    """Takes data from a space delimited file of the format x,y"""
    

    data=np.loadtxt(path,skiprows=skip,delimiter=" ",dtype=float)
    

    x=np.array([row[0]for row in data])
    y=np.array([row[1]for row in data])

    fig=plt.figure(figsize=(10,8))
    sub=plt.subplot(1,1,1)
    
    sub.plot(x,y,"b-")
    
    
    sub.axis([min(x),max(x),min(y),max(y)])
    
    
    sub.set_title(title)
    
    sub.set_xlabel(xlabel)
    sub.set_ylabel(ylabel)

    fig.show()
    return fig


def plot_save(path,skip=0,title='x vs y',xlabel='x',ylabel='y'):
    if os.path.isdir("plots")==False:
        os.system("mkdir plots")
    fig=plot(path,skip,title,xlabel,ylabel)
    name=os.path.basename(path).replace(".txt","plt.pdf")
    fig.savefig("plots/"+name,format="pdf")
    
        
        
        



