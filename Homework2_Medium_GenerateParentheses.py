# number of pairs of parentheses

n = 8
columns = n*2
rows = (2**(columns-2)) # first and last column are always going to be A and B respectively, so you can subtract 2 columsn for combinations
print(f'The number of rows is {rows} and the number of columns is {columns}')

# contains generations of all possible combinations, and then whittles down based on criteria
# '(' is an "A" for ease of eyesight, while a ')' is a B for the same reason

# Rules 
# You cannot have a 1 before 0 for the starting position
# There must be the same number of 0 and 1


# establishing matrix for all combinations possible (regardless of if they meet criteria for parentheses) 
combinationsMatrix = [[0 for x in range(columns)] for y in range(rows)] 

# establishing matrix for all INTERIOR combinations possible (easier to do in binary)
binaryInteriorMatrix = [[0 for x in range(1)] for y in range(rows)] 

for j in range(rows):
    binaryInteriorMatrix[j] = format(j, '0' + str(columns-2) + 'b') # filling the matrix for the INTERIOR values with all combinations
    
# making a list with the concatenated values that we had separated from before
concatenatedCombinationsList = [[0 for x in range(1)] for y in range(rows)] 

# Loop to input all the combinations
# Establishing that the first cell is always A and last cell is always B for each row
for i in range(rows):
    combinationsMatrix[i][0], combinationsMatrix[i][-1] = '0','1'
    # inputting every value in the row in the binary matrix into the same position in the combinations matrix
    for j in range(1, columns-1):
        tempStringVar = binaryInteriorMatrix[i] # a placeholder variable for the string to make life easier for substringing
        combinationsMatrix[i][j] = tempStringVar[j-1:j]
    # adding to new concat list made above this for loop
    concatenatedCombinationsList[i] = ''.join(combinationsMatrix[i][0:(columns)])

validAnswersList = []
    
#only gathering the valid answers based on conditions
for i in range(rows):
    # if the number of '0' and '1' match, then the result is possible
    if concatenatedCombinationsList[i].count('0') == concatenatedCombinationsList[i].count('1'):
        # if the last three are NOT 001, then the result is possible
        tempStringVar = concatenatedCombinationsList[i] # a placeholder variable for the string to make life easier for substrings
        # for loop here for more 1s than 0s reading from left to right
        runningZeroTotal = 0
        runningOneTotal = 0
        oneGreaterThanZero = False
        for j in range(len(tempStringVar)):
            if tempStringVar[j] == '0':
                runningZeroTotal += 1
            elif tempStringVar[j] == '1':
                runningOneTotal += 1
                   
            if runningZeroTotal < runningOneTotal:
                oneGreaterThanZero = True
            else: 
                continue
            
        if runningZeroTotal == runningOneTotal and oneGreaterThanZero == False:
            validAnswersList.append(concatenatedCombinationsList[i])
    else:
        continue

# changing the 0 and 1 values to '(' and ')' respectively
validAnswersList = [ans.replace('0','(') for ans in validAnswersList]
validAnswersList = [ans.replace('1',')') for ans in validAnswersList]
    
print(validAnswersList)
print(f'The # of valid answers is: {len(validAnswersList)}')


