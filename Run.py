import os

import Modules.DataGroupClass as dgc

path=raw_input("Directory path : ")

datagroup=dgc.SSDataGroup(path)#initializes the Group. Prompts for exposure time of each file if not preasent.

datagroup.plot_all()#plots the spectrum of every file in the group

datagroup.save_Rvt(name='RvTimePlot_scale2') #saves an R plot for the group