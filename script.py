# Define the location of the files
path_data1 = r'C:\...'
path_data2 = r'C:\...'
path_output = r'C:\...'

# Read Data_file_1 and store lines in a list
with open (path_data1, "r") as data_1:
    data_1_lines = data_1.read().splitlines()
	
	
# Read Data_file_2 and store lines in a list



# Create dictionaries to hold Serial ID (as key) and variable information


# Iterate through all lines of data_1_lines and build dictionary
for line in data_1_lines:
	# Split line into a list
	
	# Add records to the dictionary where the ID (position 1) is the key and the variable (position 2) is the value
	

# Iterate through all lines of data_2_lines and build dictionary


# Using the two dictionaries that have been created, build the list of lines 
list_output_lines = list()



# From the list of lines, build a file and write it to disk at the location 'path_output'