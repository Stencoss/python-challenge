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


# File paths for input and output
input_csv = os.path.join(pathlib.Path(__file__).parent.resolve(), 'Resources', 'budget_data.csv')
output_file = os.path.join(pathlib.Path(__file__).parent.resolve(), "..", "Analysis")

print("************" + input_csv)

# Read file in
with open(input_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    for line in csvreader:
        print(line)