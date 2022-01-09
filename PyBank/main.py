# Main file for PyBank
# TODO: Refactor into functions to be called
# TODO: Calaculate the changes in Profit/Losses over entire period, then the average change - Not sure on this one



import os           # Used for pathing
import csv          # Used to read / write csv files
import pathlib      # Used for file pathing

# Variables
month_counter = 0           # Initalize month_counter to 0
total_over_period = 0       # Initalize total_over_period to 0
profits_list = []           # Makes a list of just profits
num_temp = 0                # temp num to test vs max num
max_num = 0                 # store the highest number
min_num = 0                 # store the lowest number

# File paths for input and output
input_csv = os.path.join(pathlib.Path(__file__).parent.resolve(), 'Resources', 'budget_data.csv')
output_file = os.path.join(pathlib.Path(__file__).parent.resolve(), "..", "Analysis")

# print("************" + input_csv)                                     # test File path

# Read file in
with open(input_csv) as csv_file:                                       # Open csv file
    csvreader = csv.reader(csv_file, delimiter=",")                     # Put in reader and seperate the comma values
    next(csvreader)                                                     # Skip the header line
    for line in csvreader:                                              # Start loop to run through the file
        # print(line)                                                   # Show data
        profits_list.append(line[1])                                    # Create a list
        month_counter += 1                                              # Count months which counts lines
        total_over_period = int(line[1]) + total_over_period            # Find the total profit losses
        
        # Find the highest and lowest number
        if max_num < int(line[1]):
            max_num = int(line[1])
            
        if min_num > int(line[1]):
            min_num = int(line[1])
        
        

    # Subtract 1 so it does not incle
    print("Total Months: " + str(month_counter))
    print("Total: " + str(total_over_period))
    print("Average Change: ")
    print("Greatest Increase in Profits: " + " month place holder " + str(max_num))
    print("Greatest Decrease in Profits: " + " month place holder " + str(min_num))
    
#print(profits_list)
