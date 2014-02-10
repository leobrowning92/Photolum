
import numpy as np
import matplotlib.pyplot as plt
import filefunctions as ff
import DataClass as dc
import DataFunctions as df
import os

class SSDataGroup(object):
    """ Initializes as a group of SSData objects from DataClass
    by reading all of the files 
    within a directory. That directory must only contain text files outputted by
    SpectraSuit, as well as an iformation directory beginning with 'Info' .
     
    This class contains functions that itterate and act apon all 
    of the files within the associated directory
    and also act apon variables inherent to the group."""
    
    
    def __init__(self,path):
        self.path=path #note this is the path of the directory containing the relevent files
        data_sets=[]
        
        for file in os.listdir(self.path+"/"):
            if file.startswith(".")==False and file.startswith("Info")==False:
                data_sets.append(dc.SSData(self.path+"/"+file))
        self.data_sets=data_sets       
        for data in self.data_sets:
            data.make_info()
            data.calc_R()
            data.save_info()
        if os.path.isfile(self.path+'/'+"InfoTimes.txt")==False:
            self.make_times()
        self.times=self.match_times()
        self.save_InfoRvt()
        D
                
        
        
    def plot_all(self,width=15,hight=40):
        """makes a figure with all of the graphs for the sample associated
        with that data set as sub figures"""
        
        size=len(self.data_sets)/2+1
        plt.figure(figsize=(width,size*5))
        i=1
        
        for data in self.data_sets:
                data.sub_plot(i,size)
                i+=1
        plt.savefig(self.path+"/"+"Info"+os.path.basename(self.path)+"/"+"plots",format='pdf')
        basenm=self.path+"/"+"Info"+os.path.basename(self.path)+"/"+"plots"
        os.rename(basenm,basenm+'.pdf')
        

        
    def make_times(self):
        """takes user inputs of times and places them in a file
         such that they are indexed from 0 in the order of the .txt files associated with them.
         """
         
        file_list= os.listdir(self.path)
        
        times=open(self.path+'/'+"InfoTimes.txt","w")

        i=0
        for file in file_list:
            if file.startswith(".")==False and file.startswith("Info")==False:
        
                times.write(str(i)+"    "+str(raw_input("input the time of exposure for file "+file+" : "))+'\n')
                i+=1
        
        times.close()
        
    def match_times(self):
        times=np.loadtxt(self.path+'/'+"InfoTimes.txt")
        
        r_values=np.empty([len(times),1])
        
        i=0
        for data in self.data_sets:
            r_values[i,0]=data.info["R"]
            i+=1
        
        times=np.append(times,r_values,axis=1)
        
        times=np.delete(times,0,1)
        
        return times
        
        
    def plot_Rvt(self):
        """makes a simple plot of R vs t"""
        t = np.array([row[0] for row in self.times])
        R = np.array([row[1] for row in self.times])
        
        
        plt.figure(figsize=(10,8))
        plt.subplot(1,1,1)
        plt.plot(t,R,'ro')
        plt.axis([min(t),max(t)*1.1,min(R),max(R)*1.1])
        plt.title(os.path.basename(self.path)+"R vs t \nExposure to 1.6kW X-Rays")
        plt.xlabel("Exposure time (s)")
        plt.ylabel("R (Arb. Units)")
        
        plt.show()
        
    def save_Rvt(self,name="RvTimePlot"):
        """saves a plot of R vs time in to the info folder within the directory of the Group as a pdf file"""
        t = np.array([row[0] for row in self.times])
        R = np.array([row[1] for row in self.times])
        
        
        plt.figure(figsize=(10,8))
        plt.subplot(1,1,1)
        plt.plot(t,R,'ro')
        plt.axis([min(t),max(t)*1.1,min(R),5])
        plt.title(os.path.basename(self.path)+"  "+name+"\nExposure to 1.6kW X-Rays")
        plt.xlabel("Exposure time (s)")
        plt.ylabel("R (Arb. Units)")
        plt.savefig(self.path+"/"+"Info"+os.path.basename(self.path)+"/"+name+os.path.basename(self.path),format='pdf')
        basenm=self.path+"/"+"Info"+os.path.basename(self.path)+"/"+name+os.path.basename(self.path)
        os.rename(basenm,basenm+'.pdf')
        
    def save_InfoRvt(self):
        file = open(self.path+"/InfoTvR_"+os.path.basename(self.path)+".txt","w")
        i=0
        for row in self.times:
            file.write(str(row[0])+"    "+str(row[1])+"\n")
            self.data_sets[i].info["Time"]=row[0]
            i+=1
            
        file.close()


   
        

    
       
        
        
    
        
        
        
        
        
        
    
    










