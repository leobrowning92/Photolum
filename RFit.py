import Modules.SimpleFit as SimpleFit

def expfit(name):

    file=name
        
        
    data,x,y=SimpleFit.load_data("SampleData/"+file)
        
        
    fitfig=SimpleFit.fit1(x,y,title=file)
    
    
expfit("InfoTvR_LB00004.txt")