# -*- coding: utf-8 -*-
import glob
import os
import csv
import sys

"""
This Function get_indexes taken in the first row of the data (index) as input and gives out
the indexes pertaining to name,cost,last name and first name.
"""
def get_indexes(index):   
    index = index.strip().split(',')
    nm_ind = 0;
    cost_ind = 0;
    for ind,name in enumerate(index):
        if name == "drug_name": # Check for Name of the Drug index
            nm_ind = ind
        if name == "drug_cost": # Check for Cost of the Drug index
            cost_ind = ind
        if name == "prescriber_last_name": # Check for Last Name index
            last_ind = ind
        if name == "prescriber_first_name": # Check for First Name index
            first_ind = ind
    return nm_ind,cost_ind,last_ind,first_ind

"""
 This Function get_Dict creates a dictionary drug_name with Prescriptors and the Drugs they prescribed.
 The Second Dict drug_Cost is a sorted dictionoary(Just like a nested list), which contains 
 details about the Drugs and total cost in descending order.
 Inputs for this function are the indexes of name, cost, last name and first name of the given data. 
 """ 
def get_Dict(data,nm_ind,cost_ind,last_ind,first_ind):
    drug_name = {};
    drug_cost = {};
    for i in range(1,len(data)):
        data_loc = data[i].strip().split(',') 
        name = data_loc[nm_ind] # Name of the Drug is selected
        pres_name = data_loc[first_ind]+data_loc[last_ind] # Creating prescribers full name
        drug_name[pres_name] = name # Creating a Dict with Prescribers Name and Drug Name
        if(name in drug_cost.keys()):
            drug_cost[name] += int(data_loc[cost_ind]) # Creating total cost cumulatively
        else:
            drug_cost[name] = int(data_loc[cost_ind]) # Creating first instance of the prescribers name if not existing
    drug_Cost = sorted(drug_cost.items(),key=lambda x: x[1],reverse = True) # Create a sorted Dict w.r.t cost
    return drug_name,drug_Cost

"""
This Function create_csv taken in the dictionary with prescribers name and drug name as well as
the sorted dictionary of the drug name and cost to create a csv file in the selected folder.
"""
def create_csv(drug_name,drug_dict):
    index_out = ['drug_name','num_prescriber','total_cost']  # First line of the output csv file
    out = csv.writer(open(output_folder,"w"), delimiter=',',quoting=csv.QUOTE_NONE) # Setting up the Output Directory with no quotes
    out.writerow(index_out)
    for drug in drug_dict:
        row_out = [drug[0],list(drug_name.values()).count(drug[0]),drug[1]] # Create a row for each drug in the datafile
        out.writerow(row_out)
    
input_folder = str(sys.argv[1]); # Take the First input as Input_Folder
output_folder = str(sys.argv[2]);# Take the Secong input as Output_Folder

# Checking if path exists for the input folder
file = glob.glob(input_folder)
if(file):
    with open(file[0],'r') as fin:
        data = fin.readlines()
else:
    sys.exit('Given Input Folder Does not Exist')
index = data[0]

name_index,cost_index,firstname_index,lastname_index = get_indexes(index)
drug_name,drug_cost = get_Dict(data,name_index,cost_index,lastname_index,firstname_index)
create_csv(drug_name,drug_cost)

print('Successfully Executed')