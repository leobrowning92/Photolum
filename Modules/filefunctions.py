
import os

"""These functions performs functions on files of the type AE01068_00000.txt 
which are output by the SpectraSuit Data collection program.

These functions are used by DataClass to initialize and perform actions
 on the Data sets and their source files that comprise the DataClass 
 objects.

"""

def get_info(path,number=16):
    """reads the first 'number' of lines of a file and saves 
    them to a list which is returned."""
    
    file=open(path,"r")
    info=["The sample data is from"+path]
    i=0
    #print "enter"
    for r in file:
        info.append(r)
        if i>=number-1:
            break
        i+=1
        #print "step"
    #print "enter"
    file.close()
    return info


def trim_lines(path,string=">>>"):
    """takes any lines beginning with 'string' and deletes them"""        
    
    file=open(path,"r")
    lines =file.readlines()
    file.close()
    file=open(path,"w")
    for line in lines:
        if line.startswith(string)==False:
            file.write(line)
    file.close()

def get_name(path):
    """returns the file name without .txt on the end"""
    
    list_name=list(os.path.basename(path))
    
      
    list_name=list_name[0:len(list_name)-4]
    name="".join(list_name)
    return name
    
def get_int_time(path,string="Integration"):
    """returns the integration time of a spectra suit run as an intiger"""
    info=get_info(path)
    
    for item in info:
        if item.startswith(string):
            line=item
            
    l_line=list(line)
    
    l_time = l_line[25:31:1]
    
    time = "".join(l_time)
    
    return int(time)
    
    
    
    
    
    
    
        
        
                  
       