# Main file for PyBank
# TODO: Read in CSV data
# TODO: Calculate the total number of months in the data set
# TODO: Net total amount of Profit/Losses over entire period
# TODO: Calaculate the changes in Profit/Losses over entire period, then the average change - Not sure on this one
# TODO: Greatest increase in profits - Date and amount
# TODO: Greatest Decrease in profits - Date and amount


import os           # Used for pathing
import csv          # Used to read / write csv files
import pathlib      # Used for file pathing

# Variables
month_counter = 0           # Initalize month_counter to 0
total_over_period = 0       # Initalize total_over_period to 0


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
        month_counter += 1                                              # Count months which counts lines
        total_over_period = int(line[1]) + total_over_period            # Find the total profit losses

    # Subtract 1 so it does not incle
    print(month_counter)
    print(total_over_period)