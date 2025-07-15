# Python3 program to find the closest
# perfect power while taking the minimum steps
# to reach that power from a number
# could be modified to find other perfect powers (n^3, n^4, n^5, etc.)

from math import pow, log
from tabulate import tabulate
import pandas as pd
#import numpy as np

# Function to find the closest perfect power & taking the minimum steps to reach it from a number
def getClosestPerfectPower(n:int, k:int) -> dict:
    # find the log
    lg = log(n) // log(k)

	# Variables to store the first perfect powers above and below N
    aboveN = int(pow(k, lg + 1))
    belowN = int(pow(k, lg))

	# Variables to store the difference between N and each perfect power
    aboveDiff = aboveN - n
    belowDiff = n - belowN

	# Variables to store the kth log of each perfect power
    aboveRoot = int(lg + 1)
    belowRoot = int(lg)

    return {
        'belowRoot': belowRoot,
        'belowN': belowN,
        'belowDiff': belowDiff,
        'aboveRoot': aboveRoot,
        'aboveN': aboveN,
        'aboveDiff': aboveDiff
    }

# Driver code
if __name__ == '__main__':
    desiredNumList = [155] # 31282 = 8 ^ 5 - 1486, 1486 = 11 ^ 3 + 155, 155 = 12 ^ 2 + 11
    desiredMaxBase = 19
    columnNames = [
        'Desired number N',
        'Desired base K',
        'Required exponent X',
        'Closest perfect power',
        'Difference between N & perfect power'
    ]

    belowNTable, below_numbers_tabulated, belowNDataFrame = [], '', pd.DataFrame()
    aboveNTable, above_numbers_tabulated, aboveNDataFrame = [], '', pd.DataFrame()

    for n in desiredNumList:
        for i in range(2, desiredMaxBase + 1):
            row = getClosestPerfectPower(n, i)
        
            belowNRow = [n, i, row['belowRoot'], row['belowN'], row['belowDiff']]
            belowNTable.append(belowNRow)

            aboveNRow = [n, i, row['aboveRoot'], row['aboveN'], row['aboveDiff']]
            aboveNTable.append(aboveNRow)
        
        # Convert the belowNTable & aboveNTable lists to pandas Dataframes
        belowNDataFrame = pd.DataFrame(belowNTable, columns = columnNames)
        aboveNDataFrame = pd.DataFrame(aboveNTable, columns = columnNames)

        #print(f'Perfect powers less than {n}:\n{belowNDataFrame}\n')
        #print(f'Perfect powers greater than {n}:\n{aboveNDataFrame}\n')

        # Tabulate the data using the tabulate library
        below_numbers_tabulated = tabulate(belowNTable, headers = columnNames, tablefmt = 'psql')
        above_numbers_tabulated = tabulate(aboveNTable, headers = columnNames, tablefmt = 'psql')

        # Display the data that was tabulated using the tabulate library
        print(f'Perfect powers less than {n}:\n{below_numbers_tabulated}\n')
        print(f'Perfect powers greater than {n}:\n{above_numbers_tabulated}\n')

        # reset the DataFrame, table & tabulation variables for use in next loop iteration
        belowNTable, below_numbers_tabulated, belowNDataFrame = [], '', pd.DataFrame()
        aboveNTable, above_numbers_tabulated, aboveNDataFrame = [], '', pd.DataFrame()