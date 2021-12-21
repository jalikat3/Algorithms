'''
    prog2.py
    Jali Purcell
    09/16/21
    For program 2 of Algorithms

    numberOfGrains:
        input: dimension of chess board, function
        to find number of grains per square
        return: number of grains
        
        MODIFICATION: added code to compute
        number of total grains

    testCount:
        series of tests for numberOfGrains
        returned: failed or pass per each test
        
        MODIFICATION: added my own tests with
        different functions

    timeToCount:
        input: function to find number of
        grains per square, and dimension
        of chessboard
        returned: time to count each grain
        given one second per grain
        
        MODIFICATION: code to find how long
        it takes, with if statements

    testTime:
        series of tests on timeToCount
        return: failed or passed statement
        for each test
        
        MODIFICATION: added my own tests,
        as well as answers for part C
        question 10 in the book (functions
        2**(k-1) and (2*k)-1

    NOTE: I changed myfun to k, to be
        able to put in the tests as they were
        given to me


'''
def numberOfGrains(k, dimension):

    # get total number of squares
    squares=dimension*dimension
    # total grains starts as 0
    total=0
    for x in range(0, squares+1):
        # update total with given function for each square
        total=total+k(x)
    # return total number of grains
    return total

def testCount():

    # returned passed if true
    if numberOfGrains(lambda k:k,10)==5050:
        print("Test 1 passed. Number of grains with identity function")

    # return failed if false 
    else:
        print("Test 1 failed. Number of grains with identity function")
        
    if numberOfGrains(lambda k: k * k, 2) == 30:
        print("Test 2 passed. Number of grains with square function")
    else:
        print("Test 2 failed. Number of grains with square function")
        
    if numberOfGrains(lambda k: 2*k+1, 4) == 289:
        print("Test 3 passed. Number of grains with double plus one")
    else:
        print("Test 3 failed. Number of grains with double plus one")
        
    if numberOfGrains(lambda k: k*k*k, 8)==4326400:
        print("Test 4 passed. Number of grains with cube function")
    else:
        print("Test 4 passed. Number of grains with cube function")
        
    if numberOfGrains(lambda k: 3*k, 3) == 135:
        print("Test 5 passed. Number of grains with triple function.")
    else:
        print("Test 5 failed. Number of grains with triple function.")



def timeToCount(k, dimension):

    # find total number of grains
    total=numberOfGrains(k, dimension)

    # initialize time
    seconds=0
    minutes=0
    hours=0
    days=0
    years=0


    for x in range(0, total):
        seconds=seconds+1
        # reset when minute is reached
        if seconds==60:
            seconds=0
            minutes=minutes+1
        # reset when hour is reached
        if minutes==60:
            minutes=0
            hours=hours+1
        # reset when day is reached
        if hours==24:
            hours=0
            days=days+1
        # reset when year is reached
        if days==365:
            days=0
            years=years+1
    # return results
    return([seconds, minutes, hours, days, years])

def testTime():

    # return pass if true
    if timeToCount(lambda k:k,10)==[10,24,1,0,0]:
         print ("Test 3 passed.  Time to count with identity function.")
         
    # return failed if false
    else:
         print ("Test 3 failed.  Time to count with identity function.")
         
    if timeToCount(lambda k:k*k,10)==[10,59,21,3,0]:
         print ("Test 4 passed.  Time to count with square function.")
    else:
         print ("Test 4 failed.  Time to count with square function.")
         
    if timeToCount(lambda k:2*k+1, 3)==[40, 1, 0, 0, 0]:
         print("Test 5 passed. Time to count with double plus one")
    else:
         print("Test 5 failed. Time to count with double plus one")
         
    if timeToCount(lambda k:4*k, 15)==[0, 15, 4, 1, 0]:
         print("Test 6 passed. Time to count with quadruple function.")
    else:
         print("Test 6 failed. Time to count with quadruple function.")
         
    if timeToCount(lambda k: k*k*k, 4)==[16, 8, 5, 0, 0]:
         print("Test 7 passed. Time to count with cube function.")
    else:
         print("Test 7 failed. Time to count with cube function.")
    
    # PART C, functions 2**(k-1) and (2*k)-1
    # can function as additional tests on timeToCount
    
    if timeToCount(lambda k:int(2**(k-1)), 2)==[15, 0, 0, 0, 0]:
        print("Test 1 for 10a passed. Time to count with 2^(k-1).")
    else:
        print("Test 1 for 10a failed. Time to count with 2^(k-1).")
        
    if timeToCount(lambda k: int(2**(k - 1)), 3) == [31, 8, 0, 0, 0]:
        print("Test 2 for 10a passed. Time to count with 2^(k-1).")
    else:
        print("Test 2 for 10a failed. Time to count with 2^(k-1).")
    
    if timeToCount(lambda k:2*(k-1), 4)==[58, 3, 0, 0, 0]:
        print("Test 1 for 10b passed. Time to count with 2*(k-1).")
    else:
        print("Test 1 for 10b failed. Time to count with 2*(k-1).")
        
    if timeToCount(lambda k: 2*(k - 1), 3) == [10, 1, 0, 0, 0]:
        print("Test 2 for 10b passed. Time to count with 2*(k-1).")
    else:
        print("Test 2 for 10b failed. Time to count with 2*(k-1).")
        
    # ANSWERS for question 10
    # can serve as additional tests on timeToCount
    
    if timeToCount(lambda k:int((2*k)-1), 8)==[15, 8, 1, 0, 0]:
        print("Answer for 10b passed. Time to count with 2^(k-1).")
    else:
        print("Answer for 10b failed. Time to count with 2^(k-1).")



        
      

    

