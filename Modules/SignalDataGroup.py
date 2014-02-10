import DataGroupClass as dgc

import DataFunctions as df

import numpy as np

import os



class SignalDataGroup(dgc.SSDataGroup):
    """is an case of the SSDataGroup class that has SSData objects grouped according to their 
    exposure time."""
    
    
    def __init__(self,path):
        super(SignalDataGroup,self).__init__(path)
        


    def calc_deltaSm3(self):
        data0=self.data_sets[0].data
        left=530
        right=680
        
        deltaSm3_values=np.empty([len(self.times),1])
        deltaSm3_values[0,0]=0
        
        for i in range(1,len(self.data_sets)):
            data=self.data_sets[i].data
            
            change=np.abs(df.integrate(data,left,right)-df.integrate(data0,left,right))
            
            self.data_sets[i].info["deltaSm3"]=change
            deltaSm3_values[i,0]=change
        
        self.times=np.append(self.times,deltaSm3_values,axis=1)
        
        
            
    def save_Sm3vt(self,name="DeltaSm3vTimePlot"):
        """saves a plot of Delta Sm3 signal vs time in to the info folder within the directory of the Group as a pdf file"""
        t = np.array([row[0] for row in self.times])
        delta = np.array([row[2] for row in self.times])
        
        
        plt.figure(figsize=(10,8))
        plt.subplot(1,1,1)
        plt.plot(t,delta,'ro')
        plt.axis([min(t),max(t)*1.1,min(delta),max(delta)*1.1])
        plt.title(os.path.basename(self.path)+"  "+name+"\nExposure to 1.6kW X-Rays")
        plt.xlabel("Exposure time (s)")
        plt.ylabel("$\Delta$Sm3 signal (Arb. Units)")
        plt.savefig(self.path+"/"+"Info"+os.path.basename(self.path)+"/"+name+os.path.basename(self.path),format='pdf')
        basenm=self.path+"/"+"Info"+os.path.basename(self.path)+"/"+name+os.path.basename(self.path)
        os.rename(basenm,basenm+'.pdf')
    
    
    
    
    def save_InfoSm3vt(self):
        file = open(self.path+"/InfoSm3vR_"+os.path.basename(self.path)+".txt","w")
        
        for row in self.times:
            file.write(str(row[0])+"    "+str(row[2])+"\n")
           
        file.close()
        
        
        
   
    
    