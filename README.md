# ABAQUS
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

odb file is also attached for version convinence
This project is executed on abaqus 2018 version 

Note:

if you want to use ABAQUS PDE environment
invoke it by typing "abaqus pde" in the command promt

for GUI/Kernel/Local 
select "Local" and lookout for output results in the command promt
"""
