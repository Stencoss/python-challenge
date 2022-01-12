# Analyze the data set that includes election data
# TODO: Print to text file

import csv              # allows the import and export of csv files
import pathlib          # Pathing required to read and write files
import os               # Need to use OS for reading paths

# Paths for CSV and also to write results in
input_csv = os.path.join(pathlib.Path(__file__).parent.resolve(), 'Resources', 'election_data.csv')       # Read location 
output_file = os.path.join(pathlib.Path(__file__).parent.resolve(), "Analysis")                         # Write location

# Variables
vote_total = 0                  # Tally the total number of votes
k_total, c_total, l_total, o_total = 0,0,0,0
winner = ""
winner_list =[]

# Read CSV file in
with open(input_csv) as csv_file:                           # Open csv file
    csvreader = csv.reader(csv_file, delimiter=",")         # Put in reader and seperate the comma values
    next(csvreader)                                         # Skip the header line
    for line in csvreader:                                  # Start loop to run through the file
        vote_total = vote_total +  1                        # Find the vote_total by counting rows
        if line[2] == "Khan":                               # Find each vote count seperatly
            k_total = k_total + 1
        elif line[2] == "Correy":
            c_total = c_total + 1
        elif line[2] == "Li":
            l_total = l_total + 1
        elif line[2] == "O'Tooley":
            o_total = o_total + 1
            
    # Make a list and find the winner
    winner_list = [k_total, c_total, l_total, o_total]
    if max(winner_list) == k_total:
        winner = "Khan"
    elif max(winner_list) == c_total:
        winner = "Correy"
    elif max(winner_list) == l_total:
        winner = "Li"
    else:
        winner = "O'Tooley"
    # Start to show results
    print("Election Results")
    print("--------------------------")
    print("Total Votes: " + str(vote_total))
    print("--------------------------")
    print("Khan: " + str(round(k_total / vote_total *100, 4)) + "% (" + str(k_total) +")")
    print("Correy: " + str(round(c_total / vote_total *100, 4)) + "% (" + str(c_total) +")")
    print("Li: " + str(round(l_total / vote_total *100, 4)) + "% (" + str(l_total) +")")
    print("O'Tooley: " + str(round(o_total / vote_total *100, 4)) + "% (" + str(o_total) +")")
    print("-------------------------")
    #FIXME:
    print("Winner: " + winner)
    print("-------------------------")