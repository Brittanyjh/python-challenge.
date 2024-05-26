import os
import csv


# Set path for file
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, encoding='UTF-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

#Print "Election Results" header and lines for 
    print(f"Election Results")
    print(f"---------------------------------")

#The total number of votes cast
    
def count_rows_in_column(csvpath, column_index):
    total_rows = 0

    with open(csvpath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > column_index:
                    total_rows += 1

    return total_rows

column_index_to_count = 0  # Change this to the index of the column you want to count rows for
total_rows_in_column = count_rows_in_column(csvpath, column_index_to_count)
print("Total Votes:", total_rows_in_column-1)    
        
print(f"---------------------------------")
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won

from collections import defaultdict

def identify_unique_values_with_count_and_percentage(csvpath, column_index):
    unique_values_count = defaultdict(int)  # Using defaultdict to count unique values
    total_lines = 0
    
    with open(csvpath, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            # Check if column index is within range of the row length
            if column_index < len(row):
                value = row[column_index]
                unique_values_count[value] += 1
                total_lines += 1
    
    # Calculate percentage for each unique value
    unique_values_percentage = {value: (count / total_lines) * 100 for value, count in unique_values_count.items()}
    
    # Find unique value with the highest percentage
    max_percentage_value = max(unique_values_percentage, key=unique_values_percentage.get)
    
    return unique_values_count, unique_values_percentage, max_percentage_value



column_index = 2  
unique_values_count, unique_values_percentage, max_percentage_value = identify_unique_values_with_count_and_percentage(csvpath, column_index)


for value, count in unique_values_count.items():
    percentage = unique_values_percentage[value]
    print("{}: {:.3f}% ({})".format(value, percentage, count))
#The winner of the election based on popular vote
print(f"---------------------------------")
print("Winner: {}".format(max_percentage_value, unique_values_percentage[max_percentage_value]))
print(f"---------------------------------")

       



 
