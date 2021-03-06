# Main file for PyBank
# TODO: Refactor into functions to be called


import os           # Used for pathing
import csv          # Used to read / write csv files
import pathlib      # Used for file pathing

# Variables
month_counter = 0           # Initalize month_counter to 0
total_over_period = 0       # Initalize total_over_period to 0
pre_change_list = []        # Store the changes from month to month
average_change = []         # The differences of month to month list
max_num = 0                 # store the highest number
min_num = 0                 # store the lowest number
max_month = ""              # Collect the month that the max happened in
min_month = ""              # Collect the month that the min happened in

# File paths for input and output
input_csv = os.path.join(pathlib.Path(__file__).parent.resolve(), "Resources", "budget_data.csv")       # Read location 
output_file = os.path.join(pathlib.Path(__file__).parent.resolve(), "Analysis", "analysis.txt")         # Write location


# Read file in and keep open until with statement ends
with open(input_csv) as csv_file:                                       # Open csv file
    csvreader = csv.reader(csv_file, delimiter=",")                     # Put in reader and seperate the comma values
    next(csvreader)                                                     # Skip the header line
    for line in csvreader:                                              # Start loop to run through the file
        pre_change_list.append(int(line[1]))                            # Create a list
        month_counter += 1                                              # Count months which counts lines
        total_over_period = int(line[1]) + total_over_period            # Find the total profit losses
        
        
        # Find the largest value - If larger replace 
        # Once found collect month also
        if max_num < int(line[1]):
            max_num = int(line[1])
            max_month = line[0]
        
        # Find the smallest value - If smaller replace
        # Once found collect month also                
        if min_num > int(line[1]):
            min_num = int(line[1])
            min_month = line[0]
    

    # Finding the change between first and next value        
    for counter in range(len(pre_change_list)):                 # Run the full list
        if counter == len(pre_change_list) - 1:                 # Don't run out of bounds
            break                                               # If your going to break for loop
        average_change.append(pre_change_list[counter + 1] - pre_change_list[counter])  # Find the average of change
    

# Output to terminal
    print("Financial Analysis")
    print("----------------------------")    
    print(f"Total Months: {month_counter}")
    print(f"Total: {total_over_period}")
    print(f"Average Change: {sum(average_change) / len(average_change)}")
    print(f"Greatest Increase in Profits: {max_month} {max_num}")
    print(f"Greatest Decrease in Profits: {min_month} {min_num}")
    
# Write to a txt file in Analysis dir
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")   
    file.write(f"Total Months: {month_counter}\n")
    file.write(f"Total: {total_over_period}\n")
    file.write(f"Average Change: {sum(average_change) / len(average_change)}\n")
    file.write(f"Greatest Increase in Profits: {max_month} {max_num}\n")
    file.write(f"Greatest Decrease in Profits: {min_month} {min_num}\n")
    