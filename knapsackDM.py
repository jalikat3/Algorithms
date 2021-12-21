'''
    knapsackDM.py
    12/09/21-12/13/21
    Alex Johns, Jali Purcell,and Richard Zhou
    For Final Project of Algorithms CSCI 262

    METHODS

    knapsackDM- implements the dynamic programming method
    knapsack algorithm to determine what items from a
    packing list we should bring to maximize the total
    value. An output csv file will be created, detailing
    the items we should pack, what items we will need
    to buy, and how much money we will need to spend

    MODIFICATION-added outputfile name to be an input
    so that the user can run multiple times, and save
    the output files of each

    -changed variable names to be more descriptive


    testKnapsack- can be used to test any csv file, given
    that an expectedValue for the knapsack (suitcase) is given

    testKnapsackCollection- compilation of our tests, extra
    tests include a large file, and an empty file. Our example
    we used to reflext the problem is suitcaseTest with capactiy
    of 35. (Airline requirement 50 lbs-15 lbs suitcase)

'''

import csv

# inputs: max capacity (airline total-suitcase weight)
#         input file name, and output file name
def knapsackDM(capacity, inputFileName, outputFileName):
    file=str(inputFileName)+".csv"
    datafile = open(file, 'r')

    # List of values
    values=[]

    # List of weights
    weights=[]

    # packing list
    packing=[]

    # packable capacity
    Max=capacity
    
    # append lists with values in the data files
    for line in datafile:
        # current line, split at comma, remove \n
        curLine=line.strip().split(",")

        # add item name to packing list
        packing.append(str(curLine[0]))
        # add weight to weights
        weights.append(float(curLine[1]))

        # add value to values
        values.append(float(curLine[2]))

        
    # datafile 
    datafile.close()

    # numberVals=number of values
    numberVals=len(values)

    # make our 2D array (matrix M), initialized with 0s
    # the columns are the allowed capacity
    # the rows are the allowed items
    Matrix = [[0 for weight in range(Max + 1)] for value in range(numberVals + 1)]

    # operation counter
    count=0
    # for length of the items list
    for i in range(numberVals + 1):
        # for each capacity up to max capacity
        for w in range(Max + 1):
            # if either is 0, M[i][w]=0
            if i == 0 or w == 0:
                Matrix[i][w] = 0
            # if the weight does not exceed the capacity level
            elif weights[i - 1] <= w:

                # determine if the item is brought or not
                # depending on their value
                Matrix[i][w] = max(values[int(i - 1)]
                              +Matrix[int(i - 1)][int(w - weights[int((i - 1))])],
                               Matrix[int(i - 1)][w])
                # iterate count for most expensive operation
                count=count+1
            # if weight of item is too big,
            #take the value from the last weight
            else:
                Matrix[i][w] = Matrix[i - 1][w]

    ### BACK TRACKING ###
    # initialize lists for output

    # list of shop list costs
    shopListCost=[]
    
    # total for shoplist cost
    totalShopCost=0

    # shop list item names
    shopListNames=[]

    # pack list names, weights, and values
    packListNames=[]
    packListWeight=[]
    packListVals=[]

    # total weight in knapsack
    totalPack=0

    # total value of packed
    totalValue=0
    
    # backtracking
    # will iterate until all items are into lists
    while (numberVals>0):
        # if the value of M[n][W]>M[n-1][W], then the item
        # was included in the optimal solution, and is
        # added to the pack list
        if(Matrix[int(numberVals)][int(Max)]>Matrix[int(numberVals-1)][int(Max)]):
            packListVals.append(values[numberVals-1])
            # subtract the weight of the item brought
            # for next iterations
            packListWeight.append(weights[numberVals-1])
            Max=Max-weights[numberVals-1]
            # add item to the pack list
            packListNames.append(packing[numberVals-1])
        else:
            # if it wasn't included in the optimal solution,
            # add to the shopList 
            shopListCost.append(values[numberVals-1])
            # add to shopListNames
            shopListNames.append(packing[numberVals-1])
            # update the total
            totalShopCost=totalShopCost+values[numberVals-1]
        numberVals=numberVals-1


    ### OUTPUTS ###
    for x in range(len(packListWeight)):
        # total weight packed
        totalPack=totalPack+packListWeight[x]
        # total value packed
        totalValue=totalValue+packListVals[x]

    # make output file
    outputFile=str(outputFileName)+".csv"
    output=open(outputFile, 'w')
    
    output.write('Pack List: '+','+'Lbs'+','+'\n')

    # generate pack list with weights
    for x in range(len(packListNames)):

        # space, item weight, item name
        packListNames.append(packing[x])
        
        output.write(','+str(packListWeight[x])+','+str(packListNames[x])+'\n')

    # total weight
    output.write('Total Weight: ' + ',' + str(totalPack)+'\n')

    # shop list 
    output.write('Shop List: '+','+'AUD'+','+'\n')

    # generate shop list with values
    for x in range(len(shopListNames)):

        # space, item cost, item name
        shopListNames.append(packing[x])
        output.write(','+str(shopListCost[x])+','+str(shopListNames[x])+'\n')

    # total cost needed to buy shopping list
    output.write('Total: '+','+str(totalValue)+'\n')

    # return total value and operations
    print("Total operations: ")
    print(count)
    print("Value: ") 
    return totalValue

def testKnapsack(Max, inputName, outputName, expectedVal):
    value=knapsackDM(Max, inputName, outputName)
    print(value)

    # if actual is not the same as expected
    # test failed
    if(value!=expectedVal):
        print("Test failed, expected "+str(expectedVal)
              +" but found "+str(value))
    else:
        print("Test passed!")

def testKnapsackCollection():
    # series of tests

    # problem test
    testKnapsack(35, 'suitcaseTest','outputTest1', 1297.8)

    # other tests
    testKnapsack(10, 'suitcaseTest', 'outputTest1B', 1099)
    testKnapsack(60, 'suitcaseBig', 'outputBigTest', 178.5)
    testKnapsack(10, 'suitcaseTest1','outputTest2', 1079.4)
    testKnapsack(2, 'suitcaseTest2','outputTest3', 39.2)
    testKnapsack(10, 'suitcaseTest3', 'outputTest4', 98)
    testKnapsack(10, 'suitcaseTest4', 'outputTest5', 0)
    testKnapsack(0, 'suitcaseTest', 'outputTest6', 0)


    
    

    
    

    

    
