import filefunctions as ff

import DataFunctions as df

import numpy as np

import matplotlib.pyplot as plt

import os


class SSData(object):
    """SSData's are objects which have associated with them a name, 
    a numpy array of data, and a plot. 
    They are specifically for those files which are produced from the 
    SpectraSuite software package of the form AE01068_00000.txt . 
    They also have an information list(dictionary?) which can be 
    filled with relevant information. 
    
    
    """
    
    def __init__(self,path):
        
        ff.trim_lines(path)
        
        
        
        
        self.name=ff.get_name(path)
        self.data=np.loadtxt(path,skiprows= 16)
        self.info={}
        self.path=path
        
    def make_info(self):
        self.info["Name"]=ff.get_name(self.path)
        self.info["Int. time (us)"]=ff.get_int_time(self.path)
        
        
    def simple_plot(self):
        
        x = np.array([row[0] for row in self.data])
        y = np.array([row[1] for row in self.data])

        #print x   #for debugging
        #print y
        plt.figure(figsize=(10,8))
        plt.subplot(1,1,1)
        plt.plot(x,y,'r-')
        plt.axis([min(x),max(x),min(y),max(y)+500])
        plt.title(self.name)
        plt.xlabel("Wavelength (nm)")
        plt.ylabel("Channel Count")
        
        plt.show()
       
    def sub_plot(self,number=1,size=8):
        """plots but does not show a subplot of the data in the object"""
        x = np.array([row[0] for row in self.data])
        y = np.array([row[1] for row in self.data])

        #print x  #for debugging
        #print y
        plt.subplot(size,2,number)
        plt.plot(x,y,"r-")
        plt.axis([min(x),max(x),min(y),max(y)+500])
        plt.title(self.name)
        plt.xlabel("Wavelength (nm)")
        plt.ylabel("Channel Count")
        
        
        
    
        
    def save_info(self):
        """saves the information from from info as well as that
         from the beginning of the spectrasuit output file to a 'name'.nfo 
         file in the same directory as the source file
        
        note l_ prefixes denote a list form of a string
        
        """
        
        name=ff.get_name(self.path)
        l_name=list(name)
        l_sample_name=l_name[0:7]
        sample_name="".join(l_sample_name)
        dirname="Info"+sample_name
        name+=".nfo"
        self.info[".nfo file"]=name
        
        if os.path.isdir(os.path.dirname(self.path)+"/"+dirname)==False:
            os.mkdir(os.path.dirname(self.path)+"/"+dirname)
    
        file=open(os.path.dirname(self.path)+"/"+dirname+"/"+name,"w")
        
        
        for item in sorted(self.info.iterkeys()):
            file.write(item+"  :  "+str(self.info[item])+"\n")
            
            
        file.write("------Information from SpectraSuit Outport file------\n")
        file.write("Run information from : "+ os.path.basename(self.path)+"\n" )
        for item in ff.get_info(self.path):
            file.write(item)
        file.write("------End Information from SpectraSuit Outport file------\n")
        
        file.close()
        
    def open_info(self):
        """Opens the .nfo file associated with this object in text edit"""
        os.system("open "+os.path.dirname(self.path)+"/"+self.info[".nfo file"])
        
    
        
    def calc_R(self,point1=645,point2=680):
        R=df.position_average(self.data,point2)/df.position_average(self.data, point1)
        self.info["R"]=R
    
    
        
    
        
                
        
        
        

              
        
       

        