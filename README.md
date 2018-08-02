# Problem
In this project, the problem statement was to parse the given csv file and create a separate csv file which is sorted w.r.t cost of the drugs.
The input file has details about drugs, people who prescribed it, cost of the drug. 
The output file contains only the name of drug, number of prescribers and cost of the drug.

# Libraries Used
To solve this problem, I have used the libraries sys, glob and csv.
I have used sys library to exit the program if the path doesn't exist, take arguments with file, glob to check if file exists, and csv library to create a new csv file.

# Logic used:
* I read the input file using builtin function open. 
* I have parsed the data using strip and split functions, using comma as delimiter.
* Then, I have selected the indices of the drug name, cost and prescriber name. (get_indices Function)
* I created a dict for storing names of presribers with drug name and another dict for adding all the cost associated (get_Dict Function)
* Using a dict automatically eliminated duplicates in the data and hence I need not worry about it.
* For generating final output file, I used the csv library and create one line for each drug (create_csv Function)
* I checked the file in the input trajectory using glob function and exited if path doesn't exist.
