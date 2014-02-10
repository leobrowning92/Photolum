import numpy as np


def integrate(data,left,right):
    """sums the channel counts for values y(x) st. left <= x <righ. takes data of the form of np array
    with each row being [x,y] """
    total=0.0
    for row in data:
        if row[0]>=left and row[0]<right:
            total+=row[1]
            
    return total
    
    
def position_average(data,point,pm=2):
    """returns the average y value and std devn of that value within
     pm 2 of an x value
    
    """
    #NOTE: row[0] denotes an x value, while row[1]denotes a y
    peak=[]
    for row in data:
        if row[0]>=point-pm and row[0]<=point+pm:
            peak.append(row[1])
    mean = np.mean(peak)
    stdevn=np.std(peak)      
    return mean
    

    import numpy as np


def integrate(data,left,right):
    """sums the channel counts for values y(x) st. left <= x <righ. takes data of the form of np array
    with each row being [x,y] """
    total=0.0
    for row in data:
        if row[0]>=left and row[0]<right:
            total+=row[1]
            
    return total
    
    
def position_average(data,point,pm=2):
    """returns the average y value and std devn of that value within
     pm 2 of an x value
    
    """
    #NOTE: row[0] denotes an x value, while row[1]denotes a y
    peak=[]
    for row in data:
        if row[0]>=point-pm and row[0]<=point+pm:
            peak.append(row[1])
    mean = np.mean(peak)
    stdevn=np.std(peak)      
    return mean
    

    
def average_data(data_list):
    """averages the second column of a list of SSdata sets which all have the same first collumn""" 
    sumdata=sum_columns(data_list,1)
    ave=data_list[0].data
    ave[:,1]=sumdata[:,1]/float(len(data_list))
    return ave
    
def sum_columns(SSdata_list,num):
    """sums all of a single collumn from a group of Data Class objects. the collumn indices is given by num
    """
    combined_data=SSdata_list[0].data
    for n in range(1,len(SSdata_list)-1):
        data=SSdata_list[n].data
        
        if len(combined_data)==len(data):#checks to ensure that the x values are the same for both sets
        
            combined_data[:,num]+=data[:,num]
                   
        else: 
            print "Error : Cannot sum data sets of different lengths."            
            break
    return combined_data         


def process_1(data1,data2,divider=680):
    """Andys method of determining a processed signal. 
    models the physical system of a ccd camera where, for each pixel, only the intensity can be measured.
    s1 and s2 describe regions in the spectrum to iether side of a divider wavelength in data1, 
    similarly s3 and s4 correspond to the same regions in data2.
     """
     
    s1,s2,s3,s4=0,0,0,0
    
    
    for row in data1:
        if   row[0] <  divider:
            s1+=row[1]
        elif row[0] >= divider:
            s2+=row[1]
    
    for row in data2:
        if   row[0] <  divider:
            s3+=row[1]
        elif row[0] >= divider:
            s4+=row[1]
    
    signal = s1-s2+s4-s3
    noise  = np.sqrt(s1+s2+s3+s4)

    
    return signal,noise
    
    
def process_Sm3(data1,data2,divider=680):
    """simple Sm3+ region signal decrease"""
    
    s1,s2,s3,s4=0,0,0,0
    
    
    for row in data1:
        if   row[0] <  divider:
            s1+=row[1]
        elif row[0] >= divider:
            s2+=row[1]
    
    for row in data2:
        if   row[0] <  divider:
            s3+=row[1]
        elif row[0] >= divider:
            s4+=row[1]
            
    signal=s1-s3
    noise  = np.sqrt(s1+s3)
    return signal,noise
    
def process_3(data1,data2,divider=680):
    """simple Sm2+ region signal increase"""
    
    s1,s2,s3,s4=0,0,0,0
    
    
    for row in data1:
        if   row[0] <  divider:
            s1+=row[1]
        elif row[0] >= divider:
            s2+=row[1]
    
    for row in data2:
        if   row[0] <  divider:
            s3+=row[1]
        elif row[0] >= divider:
            s4+=row[1]
            
    signal=s4-s2
    noise  = np.sqrt(s2+s4)
    return signal,noise
    
     
    
def average_data(data_list):
    """averages the second column of a list of SSdata sets which all have the same first collumn""" 
    sumdata=sum_columns(data_list,1)
    ave=data_list[0].data
    ave[:,1]=sumdata[:,1]/float(len(data_list))
    return ave
    
def sum_columns(SSdata_list,num):
    """sums all of a single collumn from a group of Data Class objects. the collumn indices is given by num
    """
    combined_data=SSdata_list[0].data
    for n in range(1,len(SSdata_list)-1):
        data=SSdata_list[n].data
        
        if len(combined_data)==len(data):#checks to ensure that the x values are the same for both sets
        
            combined_data[:,num]+=data[:,num]
                   
        else: 
            print "Error : Cannot sum data sets of different lengths."            
            break
    return combined_data         


def process_1(data1,data2,divider=680):
    """Andys method of determining a processed signal. 
    models the physical system of a ccd camera where, for each pixel, only the intensity can be measured.
    s1 and s2 describe regions in the spectrum to iether side of a divider wavelength in data1, 
    similarly s3 and s4 correspond to the same regions in data2.
     """
     
    s1,s2,s3,s4=0,0,0,0
    
    
    for row in data1:
        if   row[0] <  divider:
            s1+=row[1]
        elif row[0] >= divider:
            s2+=row[1]
    
    for row in data2:
        if   row[0] <  divider:
            s3+=row[1]
        elif row[0] >= divider:
            s4+=row[1]
    
    signal = s1-s2+s4-s3
    noise  = np.sqrt(s1+s2+s3+s4)

    
    return signal,noise
    
    
def process_2(data1,data2,divider=680):
    """simple Sm3+ region signal decrease"""
    
    s1,s2,s3,s4=0,0,0,0
    
    
    for row in data1:
        if   row[0] <  divider:
            s1+=row[1]
        elif row[0] >= divider:
            s2+=row[1]
    
    for row in data2:
        if   row[0] <  divider:
            s3+=row[1]
        elif row[0] >= divider:
            s4+=row[1]
            
    signal=s1-s3
    noise  = np.sqrt(s1+s3)
    return signal,noise
    
def process_3(data1,data2,divider=680):
    """simple Sm2+ region signal increase"""
    
    s1,s2,s3,s4=0,0,0,0
    
    
    for row in data1:
        if   row[0] <  divider:
            s1+=row[1]
        elif row[0] >= divider:
            s2+=row[1]
    
    for row in data2:
        if   row[0] <  divider:
            s3+=row[1]
        elif row[0] >= divider:
            s4+=row[1]
            
    signal=s4-s2
    noise  = np.sqrt(s2+s4)
    return signal,noise
    
     
    