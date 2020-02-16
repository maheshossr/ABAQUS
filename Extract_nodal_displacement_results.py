# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:06:31 2020
@author: maheshvenk@gmail.com

This script is to extract the nodal dispacement results from the abaqus output database(odb file)
with out opening the abaqus GUI ie., CAE or viewer

copy this py file in the working directory 
and 
create a batch file with below commands
##
abaqus viewer noGUI=Extract_nodal_displacement_results.py
##

make sure to update the odb file location in the "path" below

double click on the batch file and look for abaqus.rpy file in the working directory for the output data

sample input file is also attached in the GIT repository 
"Sample_abaqus_input_file.inp"

Note:

if you want to use ABAQUS PDE environment
invoke it by typing "abaqus pde" in the command promt

for GUI/Kernel/Local 
select "Local" and lookout for output results in the command promt
"""

from odbAccess import openOdb

#update the location of the odb file in the path
odb = openOdb(path='C:\\\\\\\\Sample_abaqus_input_file.odb')

lastframe = odb.steps['Step-1'].frames[-1]
lastframenumber=lastframe.frameId

partinstance_=odb.rootAssembly
for partinstance in partinstance_.instances.keys():
    print (partinstance)
    
for nodeset_ in partinstance_.instances.values():
    #print nodeset_
    for nodeset in nodeset_.nodeSets.keys():
        print (nodeset)
        
nodaldispacement_data = lastframe.fieldOutputs['U']        

loc = odb.rootAssembly.instances['PART-1-1'].nodeSets['NODES_RESULTS_OUT']
nodaldisplacement_ = nodaldispacement_data.getSubset(region=loc)
for nodalDISP_ in nodaldisplacement_.values:
    #print nadalDISP
    nodalDISP=nodalDISP_.data
    print (nodalDISP)
    
odb.close() 