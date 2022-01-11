# Main file for PyBank
# TODO: Refactor into functions to be called
# TODO: Calaculate the changes in Profit/Losses over entire period, then the average change - Not sure on this one



import os           # Used for pathing
import csv          # Used to read / write csv files
import pathlib      # Used for file pathing

# Variables
month_counter = 0           # Initalize month_counter to 0
total_over_period = 0       # Initalize total_over_period to 0
pre_change_list = []            # Store the changes from month to month
change = 0                  # Change to be added to list.
change2 = 0
average_change = []         # The differences of month to month list
max_num = 0                 # store the highest number
min_num = 0                 # store the lowest number
max_month = ""              # Collect the month that the max happened in
min_month = ""              # Collect the month that the min happened in

# File paths for input and output
input_csv = os.path.join(pathlib.Path(__file__).parent.resolve(), 'Resources', 'budget_data.csv')       # Read location 
output_file = os.path.join(pathlib.Path(__file__).parent.resolve(), "Analysis")                         # Write location


# Read file in and keep open until with statement ends
with open(input_csv) as csv_file:                                       # Open csv file
    csvreader = csv.reader(csv_file, delimiter=",")                     # Put in reader and seperate the comma values
    next(csvreader)                                                     # Skip the header line
    for line in csvreader:                                              # Start loop to run through the file
        pre_change_list.append(int(line[1]))                                    # Create a list
        month_counter += 1                                              # Count months which counts lines
        total_over_period = int(line[1]) + total_over_period            # Find the total profit losses
        
        # Average change - Find the difference from one month to 
        # the next, store the data and then find average
        # change = int(line[1]) - next(line[1])
        # print(change)
        # change_list.append(line[1])
        
        
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
        
    # for loop that collects all column 2    
    for i in pre_change_list :
        if i == len(pre_change_list) -1:
            break
        change = i - (i + 1)         # Find the difference between each month    
        average_change.append(int(change))               # Add to a list - then take average
    
    print(average_change)    
    print("Sum is: " + str(sum(average_change)) + " Length: " + str(len(average_change)))
    print(sum(average_change) / len(average_change))
   
    # print("Total Months: " + str(month_counter))
    # print("Total: " + str(total_over_period))
    # print("Average Change: ")
    # print("Greatest Increase in Profits: " + max_month + " " + str(max_num))
    # print("Greatest Decrease in Profits: " + min_month + " " + str(min_num))
    
