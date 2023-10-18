# William Eng
# weng2@oakland.edu
# print table nicely

import copy

def pretty_table(table):
    # find the largest string for each column
    col_widths = []
    num_rows = 0
    num_col = 0
    for i in range(len(table)):
        largest = 0
        num_col = i + 1
        for j in range(len(table[i])):
            if largest < len(table[i][j]):
                largest = len(table[i][j])
            num_rows = j + 1
        col_widths.append(largest)
    
    
    # Want to transpose the data such that each row of data is in one list instead each column of data is in one list
    # working off of provided data 
    sortedTable=[]
    for i in range(num_rows):
        sortedTable.append([])
        for j in range(num_col):
           sortedTable[i].append(table[j][i])
    # create string for each row 
    for i in range(num_rows):
        toPrint = '|'
        for j in range(num_col):
            # Double the longest string size in each column
            toPrint += sortedTable[i][j].center(col_widths[j]*2) + "|"
        print(toPrint)
    
tableData=[
    ['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin'],
    ['scarlet and gold', 'yellow and black', 'blue and bronze', 'green and silver'],
    ['lion', 'badger', 'eagle', 'snake']
    ]
pretty_table(tableData)