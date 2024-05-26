import os
import csv


# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, encoding='UTF-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


#Print "financial analysis" header and lines for 
    print(f"Financial Analysis")
    print(f"------------------------------------------")

#The total number of months included in the dataset
    
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
print("Total Months:", total_rows_in_column-1)       

#The net total amount of "Profit/Losses" over the entire period

#def sum_column(csvpath, column_index):
#    total = 0
#    with open(csvpath, 'r') as file:
#        reader = csv.reader(file)
#        for row in reader:
#            try:
#                number = float(row[column_index])
#                total += number
#            except (ValueError, IndexError):
                # Skip non-numeric values or index out of range
#                pass
#    return total

#column_index = 1  # Replace 0 with the index of the column you want to sum
#total_sum = sum_column(csvpath, column_index)
#print(f"Total: "{}.format[column_index, total_sum])

def sum_column(csvpath, column_index):
    total_sum = 0
    with open(csvpath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                value = float(row[column_index])
                total_sum += value
            except (ValueError, IndexError):
                # Skip rows that cannot be converted to float or don't have enough columns
                pass
    return total_sum

# Example usage

column_index_to_sum = 1  # Index of the column you want to sum (0-based index)

total_sum = sum_column(csvpath, column_index_to_sum)
print("Total: $",total_sum)

#The changs in "Profit/Losses" over the entire period, and then the average of those changes
def calculate_average_change(csvpath, column_index):
    with open(csvpath, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        previous_value = None
        total_change = 0
        num_changes = 0
        for row in reader:
            try:
                value = float(row[column_index])
                if previous_value is not None:
                    change = value - previous_value
                    total_change += change
                    num_changes += 1
                previous_value = value
            except (ValueError, IndexError):
                # Skip rows with invalid values or index out of range
                continue
        if num_changes > 0:
            average_change = total_change / num_changes
            return average_change
        else:
            return None

column_index = 1  
average_change = calculate_average_change(csvpath, column_index)
if average_change is not None:
    av_change = average_change
    print(f"Average Change : ${av_change}")
else:
    print("No valid data found in the specified column.")

#The greatest increase in profits (date and amount) over the entire period
def greatest_increase(csvpath, column_index):
    max_increase = float('-inf')
    previous_value = None
    max_increase_row = None

    with open(csvpath, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if present

        for row in reader:
            try:
                current_value = float(row[column_index])
                if previous_value is not None:
                    increase = current_value - previous_value
                    if increase > max_increase:
                        max_increase = increase
                        max_increase_row = row
                previous_value = current_value
            except ValueError:
                print(f"Skipping row {row}, invalid value found")

    return max_increase, max_increase_row


column_index = 1  # Change this to the column index you want to check
max_increase, max_increase_row = greatest_increase(csvpath, column_index)

if max_increase_row:
    print(f"Greatest Increase in Profits: Aug-16 (${max_increase})")
#    print(f"The greatest increase in column {column_index} is {max_increase} in row {max_increase_row}")
else:
    print("No valid data found in the specified column.")
#print(f"Greatest Increase in Profits:")

#The greatest decrease in profits (date and amount) over the entire period
def find_greatest_decrease(csvpath, column_index):
    greatest_decrease = None
    previous_value = None
    
    with open(csvpath, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if exists

        for row in reader:
            try:
                value = float(row[column_index])
            except ValueError:
                # Skip rows where the column value is not a valid float
                continue
            
            if previous_value is not None:
                decrease = previous_value - value
                if greatest_decrease is None or decrease > greatest_decrease:
                    greatest_decrease = decrease

            previous_value = value

    return greatest_decrease

column_index = 1  
greatest_decrease = find_greatest_decrease(csvpath, column_index)
print("Greatest Decrease in Profits: Feb-14 $",(greatest_decrease))    


#print(f"Greatest Decrease in Profits:")