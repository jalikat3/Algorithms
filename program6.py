'''
    
    program6.py
    Jali Purcell
    11/15/21-11/18/21
    For program 6 of Algorithms

    METHODS

    russianMultiply implements the
    russian peasant algorithm. Which says that:

    if n is even, n*m= (n/2) * 2m


    if n is odd, n*m= ((n-1)/2) * 2m + m

    MODIFICATIONS

    at first, I had the printing statements inside
    the while loop after n and m were changed, so the
    first two numbers didn't get printed, and the addend
    was printed in the wrong places

    I also resetted extra at the end of the while loop,
    but a reset is only needed in the else statement, so
    I moved it there

    testRussianMultiply-gives method to test russian multiply
    of two given integers and an expected solution, and addend
    count

    test-series of tests using testRussianMultiply
'''

def russianMultiply(intA, intB):

    # two integers are taken as an input
    # numberN is the multiplier
    numberN=int(intA)

    # numberM is the number that will become
    # addend if multiplier is odd
    numberM=int(intB)

    # at first, there are no addends
    # so extra is 0, and extracounter
    # is 0, as well as the array of addends
    extra=0
    extraCounter=0
    addends=[]

    # solution is not calculated
    solution=0

    # set up chart print statements
    print("__________")
    print("n  m    ")
    print("----------")

    # while loop until n is 0 or less
    while (numberN>0):

        # if multplier is not divisible by 2
        # also know as even
        if(numberN%2==0):

            # print the two, because there is no addend
            print(numberN, numberM)

            # as per the algorithm, numberN=numberN/2 for
            # the next loop
            numberN=int(numberN/2)

            # as per the algorithm, numberM=numberM*2 for
            # the next loop
            numberM=int(numberM*2)

        # if multiplier is odd
        else:

            # addend is numberM
            extra=numberM

            # print the current numberN, numberM, and extra
            print(numberN, numberM, extra)

            # add extra to the list of addends
            addends.append(extra)

            # iterate the addend counter
            extraCounter=extraCounter+1

            # as per the algorithm, numberN=(numberN-1)/2
            # for the next loop
            numberN=int((numberN-1)/2)

            # as per the algorithm, numberM=numberM*2
            # for the next loop
            numberM=int(numberM*2)

            # reinitialize extra to 0
            extra=0
            
    # end table     
    print("")
    print("Solution: ")

    # solution is equal to the sum of the addend list
    [solution:=solution+x for x in addends]

    # return the solution, and number of addends
    return [solution,extraCounter]


def testRussianMultiply(intA, intB, expectedSolution, expectedCount):
    solution, count= russianMultiply(intA, intB)

    # if solution is not expected solution
    if(expectedSolution!=solution):
        print("Test failed, expected " + str(expectedSolution) +
              " as solution but found "+str(solution) )
    # if expected addend count is not expected count
    elif(expectedCount!=count):
        print("Test failed, expected " +str(expectedCount)
              +" as number of addends but found "+str(count))
    # else everything is passed
    else:
        print("Test passed, solution: ")
        print([solution, count])

def test():

    # given test
    testRussianMultiply(50,65,3250,3)
    # all expected values are hand calculated to test code

    # test with variations between m and n
    # 4 addends expected, 85 is odd 4 times (85, 21, 5, 1)
    # 2 addends expected, 18 is odd twice (9, 1)
    testRussianMultiply(85, 18, 1530, 4) 
    testRussianMultiply(18, 85, 1530, 2)

    # test with variations of between m and n
    # 3 addends expected, since (13, 3, 1)
    # 3 addends for n=14, since (7,3,1)
    testRussianMultiply(13, 14, 182, 3)
    testRussianMultiply(14, 13, 182, 3)

    # test multiplying by 0, should be 0
    testRussianMultiply(0, 1, 0, 0)

    # anything with multiplier (n)=1 should be m
    # with 1 addend
    testRussianMultiply(1, 1, 1, 1)
    testRussianMultiply(1, 100000000000,100000000000,1)

    # more tests
    # 64 is only odd at 1, since it is a perfect square
    # whereas 61 is odd 5 times (61,15,7,3,1)
    testRussianMultiply(64, 61, 3904, 1)
    testRussianMultiply(61, 64, 3904, 5)

    # more
    # 90 is odd 4 times (45,11,5,1)
    # 99 is odd 4 times as well (99,49,3,1)
    testRussianMultiply(90, 99, 8910, 4)
    testRussianMultiply(99, 90, 8910, 4)

    # 1000 is odd 6 times (125,31,15,7,3,1)
    # 1001 is odd 7 times (1001,125,31,15,7,3,1)
    testRussianMultiply(1000,1001,1001000,6)
    testRussianMultiply(1001,1000,1001000,7)

    # 24 is odd at 3 and 1
    # 16 is odd at 1
    testRussianMultiply(24,16,384,2)
    testRussianMultiply(16,24,384,1)
    
    
            
        
