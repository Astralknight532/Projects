import csv

# read a CSV file
with open("orders.csv", "r") as f:
    reader = csv.reader(f)

    # print each row 1 by 1 as they are read from the CSV file
    for row in reader:
        print(row)