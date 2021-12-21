'''
    
    program4JT.py
    Jali Purcell
    10/12/21-10/17/21 v. 4
    For program 4 of Algorithms
    Implements Johnson-Trotter Algorithm

    CLASSES

    Element- an element has two parts
    attached to it, a value and
    a direction. The value is the
    number that it holds, and
    the direction shows where it
    wants to go. Right is represented
    by a 1 and left is represented
    by a -1. 

    Permutation- a permutation has
    a list of elements, and a variety
    of methods.

    METHODS

    changeDirection- method in the
    element class. Changes the
    direction of an element. This
    method is utilized after
    nextPermutation is made, because
    the last step in the Johnson-Trotter
    algorithm is to change the direction
    of all elements that are larger
    than the one that just changed
    positions.


    isMobile- checks to see
    from a given permutation
    and position if the element
    can move. An element is
    mobile if it points to
    an element that is smaller
    than it. First, the method
    takes into account if it's
    pointed at the edges. Then,
    it checks if the element it
    wants to go to is smaller than
    itself, and if it is returns
    True. If the element it
    points to is larger, the method
    returns False.

    anyMobile- given a permutation,
    the method looks at all the
    elements and checks if there
    is a mobile element. This is
    important for the nextPermutation
    method, because it there are no
    mobile elements, there is no
    more permutations to be found.

    largestMobile-given a permutation,
    the method finds mobile element
    with the largest element.

    MODIFICATION-used the anyMobile
    method instead of re-coding to find
    if there is a mobile element.

    MODIFICATION- at first, the method
    only located the last mobile element.
    So, I needed to find the first mobile
    element, temporarily call that the max
    element, and replaces the max with a
    mobile element that has a larger value.
    If none is encountered, then the first
    mobile element is the largest mobile
    element.

    nextPermutation- given a permutation,
    nextPermutation returns the next permutation,
    if there are more mobile elements. First,
    it finds the largest mobile element,
    then it moves the element.

    MODIFICATION- originally, my nextPermutation
    did not change the position of all elements
    larger than itself. This is a big part of the
    Johnson-Trotter algorithm, because it's the
    last step before finding the next permutation.
    

    TESTS

    Tests utilizes an array of expected values,
    and for loops to check the actual values.

    testElementInitializer- checks the value
    and direction of a created element. If the
    expected value is not the same as the actual
    values, then something is wrong with the
    element initializer.

    MODIFICATION-added more tests

    testChangeDirection-checks the direction
    of an element after changeDirection has
    been called.

    testPermInitializer- checks the elements
    value, direction, and order of a created
    permutation. Prints the elements values
    and direction in order. If there is an
    error, something is wrong with the
    permutation initializer.

    testIsMobile- checks the mobility of
    elements in a permutation. If a test
    fails, then something is wrong with the
    isMobile method.

    MODIFICATION- added two more tests, one
    with no mobile elements, and one with more
    elements.

    testAnyMobile- tests anyMobile method by
    checking if there is a mobile element
    in given permutations.

    testLargestMobile- checks to see if
    largestMobile returns the correct
    position if there is a mobile element. Prints
    value of largest mobile.

    Note: this is how I discovered something was
    wrong with the largestMobile method, because
    it was returning the position of the last mobile
    element and not the largest mobile element.

    testNextPermutation- tests the values
    and directions of the elements in a permutation
    after nextPermutation is called. If all
    tests pass, it prints out the next permutation
    of a given permutation.

    MODIFICATION- added two more test, one with
    more elements, and one with no mobile elements. 

    
    JOHNSON-TROTTER IMPLEMENTATION- Part B

    permute- given a number, permute initializes
    a permutation with the values in order, and
    directions initialized at -1. This first
    permutation is printed. While there are
    still mobile elements, nextPermutation
    is called, and the values of the
    permutation are printed.

    test- given values of 1-5 for n to
    test permute. If the print statements
    don't align with the Johnson-Trotter
    algorithm, there is a problem in the
    permute method.

    TIME- Part C

    permuteTime- uses given code to
    print the values of a permute(n)
    to see how long it takes to print
    all the permutations of n. Since
    it prints with every permutation,
    one can watch the method run in
    real time. Time will change
    based on computer capabilities.

'''

import time
class Element():
    def __init__(self,value,direction):
            self.value=value
            self.direction=direction

    def changeDirection(self):
        self.direction=self.direction*-1

class Permutation():
    def __init__(self,array):
        self.array=array
        
    def isMobile(self, position):
        left=True
        right=True
        element=self.array[position]

        # if position is 0, there is no left element
        if position>0:
            elementLeft=self.array[position-1]
        else:
            left=False

        # if position is the length of the array-1,
        # there is no right position
        if position>=len(self.array)-1:
            right=False
        else:
            elementRight=self.array[position+1]
        
        # if there is an element to the right, the current element points right,
        # and the element's value is greater than the element on the right
        if (right==True and
           (element.direction==1 and element.value>elementRight.value)):
            return True

        # if there is an element to the left, the current element points left,
        # and the element's value is greater than the element on the left
        elif (left==True and
             (element.direction==-1 and element.value>elementLeft.value)):
            return True
        else:
            return False
        
    def anyMobile(self):
        
        for i in range(len(self.array)):
            if(self.isMobile(i)==True):

                # if mobile element is found, return true
                return True
            
        return False
    
    def largestMobile(self):

        # if none are mobile, nothing is largest
        if(self.anyMobile()==False):
            return False
        else:
            for i in range(len(self.array)):

                # set element to first mobile element
                if(self.isMobile(i)==True):
                    maxPosition=i
                    break
            # iterate through all elements
            # replace if mobile element is larger
            for i in range(len(self.array)):
                if (self.isMobile(i)
                and self.array[i].value>self.array[maxPosition].value):
                    maxPosition=i

            # return position of largset mobile element
            return maxPosition
            

    def nextPermutation(self):

        # if no mobile elements, return false
        if(self.anyMobile()):
            mobilePosition=self.largestMobile()
        
        else:
            return False

            
        # make an array with the largest mobile 
        returnArray=[]
        element=Element(self.array[mobilePosition].value,
                        self.array[mobilePosition].direction)
        
        # if direction is right
        if (element.direction==1):

            # switch current and right
            self.array[mobilePosition]=self.array[mobilePosition+1]
            self.array[mobilePosition+1]=element

        # if direction is left
        elif (element.direction==-1):

            # switch element and left
            self.array[mobilePosition]=self.array[mobilePosition-1]
            self.array[mobilePosition-1]=element

        # change direction of all elements that are larger        
        for i in range(len(self.array)):
            if (self.array[i].value>element.value):
                self.array[i].changeDirection()
            
            
        # return permutation
        return Permutation(self.array)
       
def testElementInitializer():
    print("Testing Element initializer")
    element=Element(1, -1)
    if (element.value!=1):
        print("Element value is not initialized correctly")
    if(element.direction!=-1):
        print("Element direction is not initialized correctly")
    else:
        print("Element is initialized correctly")
    print("Test 2 for Element Initializer: ")
    element=Element(2, 1)
    if (element.value!=2):
        print("Element value is not initialized correctly")
    if(element.direction!=1):
        print("Element direction is not initialized correctly")
    else:
        print("Element is initialized correctly")
        print("Test 3 for Element Initializer: ")
    element=Element(20, -1)
    if (element.value!=20):
        print("Element value is not initialized correctly")
    if(element.direction!=-1):
        print("Element direction is not initialized correctly")
    else:
        print("Element is initialized correctly")
        print("Test 3 for Element Initializer: ")
    element=Element(0, 1)
    if (element.value!=0):
        print("Element value is not initialized correctly")
    if(element.direction!=1):
        print("Element direction is not initialized correctly")
    else:
        print("Element is initialized correctly")
        

def testChangeDirection():
    print("Testing change direction method of Element")
    element=Element(1, -1)
    print("Given a direction of " + str(element.direction) +", switch direction.")
    element.changeDirection()
    print("Direction is now: "+ str(element.direction))
    element2=Element(2,1)
    print("Given a direction of " +str(element2.direction)+" switch direction.")
    element2.changeDirection()
    print("Direction is now: " +str(element2.direction))


def testPermInitializer():
    print("Testing permutation initializer")
    # first array: 1 (left) False 2 (right) False 3 (left) True 4(right) False
    array1=[Element(1, -1), Element(2, 1), Element(3, -1), Element(4, 1)]
    testArray=[1, 2, 3, 4]
    testArray2=[-1, 1, -1, 1]
    permutation=Permutation(array1)

    print("Permutation results: ")
    
    
    for i in range(len(permutation.array)):
        if(permutation.array[i].value!=testArray[i]):
            print("Value error found in position: "+str(i))
        if(permutation.array[i].direction!=testArray2[i]):
            print("Direction error found in position: "+str(i))
        else:
            print(str(permutation.array[i].value)+", "
                  +str(permutation.array[i].direction))
            
        

    # second array: 4 (right) 3(left) 1 (right) 2 (left)
    array2=[Element(4, 1), Element(3, -1), Element(1, 1), Element(2, -1)]
    permutation2=Permutation(array2)
    print("Permutation 2 result: ")
    testArray3=[4, 3, 1, 2]
    testArray4=[1, -1, 1, -1]
    

    for i in range(len(permutation2.array)):
        if(permutation2.array[i].value!=testArray3[i]):
            print("Value error found in position: "+str(i))
        if(permutation2.array[i].direction!=testArray4[i]):
            print("Direction error found in position: "+str(i))
        else:
            print(str(permutation2.array[i].value)+", "
                  +str(permutation2.array[i].direction))
            

def testIsMobile():
    print("Testing isMobile method")
    # first array: 1 (left) False 2 (right) False 3 (left) True 4(right) False
    array1=[Element(1, -1), Element(2, 1), Element(3, -1), Element(4, 1)]
    permutation=Permutation(array1)
    testArray=[False, False, True, False]

    print("Error message will be printed if IsMobile has error.")

    for i in range(len(permutation.array)):
        if(permutation.isMobile(i)!=testArray[i]):
            print("isMobile error found in position: "+str(i))
        else:
            print("Element at "+ str(i)+": " +str(permutation.isMobile(i)))
            

    # second array: 4 (right) 3(left) 1 (right) 2 (left)
    array2=[Element(4, 1), Element(3, -1), Element(1, 1), Element(2, -1)]
    permutation2=Permutation(array2)
    testArray2=[True, False, False, True]

    print("Results for permutation 2")

    for i in range(len(permutation2.array)):
        if(permutation2.isMobile(i)!=testArray2[i]):
            print("isMobile error found in position: "+str(i))
        else:
            print("Element at "+ str(i)+": " +str(permutation.isMobile(i)))

    # third array: 1 (left) False, 2(right) False, 3(right) False, 4(right) False
    print("Results for permutation 3")
    array3=[Element(1, -1), Element(2, 1), Element(3, 1), Element(4, 1)]
    permutation3=Permutation(array3)
    testArray3=[False, False, False, False]

    for i in range(len(permutation3.array)):
        if(permutation3.isMobile(i)!=testArray3[i]):
            print("isMobile error found in position: "+str(i))
        else:
            print("Element at "+ str(i)+": " +str(permutation3.isMobile(i)))

    # fourth array: 1(left) False, 2(left)True, 3(left)True,
    #4(left)True, 5(left)True, 6(rigt)False
    print("Results for permutation 4")
    array4=[Element(1, -1), Element(2, -1), Element(3, -1), Element(4, -1),
            Element(5, -1), Element(6, 1)]
    permutation4=Permutation(array4)
    testArray4=[False, True, True, True, True, False]

    for i in range(len(permutation4.array)):
        if(permutation4.isMobile(i)!=testArray4[i]):
            print("isMobile error found in position: "+str(i))
        else:
            print("Element at "+ str(i)+": " +str(permutation4.isMobile(i)))
    


    

def testAnyMobile():
    # first array: 1 (left) False 2 (right) False 3 (left) True 4(right) False
    array1=[Element(1, -1), Element(2, 1), Element(3, -1), Element(4, 1)]
    permutation=Permutation(array1)

    # second array: 4 (right) 3(left) 1 (right) 2 (left)
    array2=[Element(4, 1), Element(3, -1), Element(1, 1), Element(2, -1)]
    permutation2=Permutation(array2)

    # third array: 4(left), 3(left), 1(right), 2(right) no mobile elements
    array3=[Element(4, -1), Element(3, -1), Element(1, 1), Element(2, 1)]
    permutation3=Permutation(array3)

    print("Testing for any mobile element in permutation")
    print("Error is found if expected and actual are not the same")

    
    print("Perm 1 expected: true Actual: "+str(permutation.anyMobile()))
    print("Perm 2 expected: true Actual: "+str(permutation2.anyMobile()))
    print("Perm 3 expected: false Actual: "+str(permutation3.anyMobile()))
    

def testLargestMobile():

    print("Testing largestMobile method")
    # first array: 1 (left) False 2 (right) False 3 (left) True 4(right) False
    array1=[Element(1, -1), Element(2, 1), Element(3, -1), Element(4, 1)]
    permutation=Permutation(array1)
    position=permutation.largestMobile()
    
    print("Testing permutation 1: ")
    if(position!=2):
        print("Error in largest mobile, expected 2 but found: "
              +str(position))
    else:
        print("Largest mobile element is at position: "+str(position))
        print("Value of largest mobile element: "
              +str(permutation.array[permutation.largestMobile()].value))

    # second array: 4 (right) 3(left) 1 (right) 2 (left)
    array2=[Element(4, 1), Element(3, -1), Element(1, 1), Element(2, -1)]
    permutation2=Permutation(array2)

    position2=permutation2.largestMobile()
    
    print("Testing permutation 2: ")
    if(position2!=0):
        print("Error in largest mobile, expected 0 but found: "
              +str(position2))
    else:
        print("Largest mobile element is at position: "+str(position2))
        print("Value of largest mobile element: "
              +str(permutation2.array[permutation2.largestMobile()].value))

    print("Results for permutation 3")

    # no mobile element
    array3=[Element(1, -1), Element(2, 1), Element(3, 1), Element(4, 1)]
    permutation3=Permutation(array3)
    position3=permutation3.largestMobile()
    if(position3!=False):
        print("Error in largest mobile, expected none but found: "
              +str(position3))
    else:
        print("Largest mobile does not exist")

def testNextPermutation():

    print("Testing nextPermutation method")
    print("Results for permutation 1")

    # first array: 1 (left) False 2 (right) False 3 (left) True 4(right) False
    array1=[Element(1, -1), Element(2, 1), Element(3, -1), Element(4, 1)]
    permutation=Permutation(array1)
    permutationArray=[]
    for i in range(len(permutation.array)):
        permutationArray.append(permutation.array[i].value)

    # expected values
    testArray=[1, 3, 2, 4]

    # expected directions
    testArray1=[-1, -1, 1, -1]
    
    nextPerm=permutation.nextPermutation()

    for i in range(len(nextPerm.array)):
        if (nextPerm.array[i].value!=testArray[i]):
            print("Value error found in position: "+ str(i))
            testPassed=False
        if (nextPerm.array[i].direction!=testArray1[i]):
            print("Direction error found in position: "+str(i))
            testPassed=False
        else:
            print("Test for element at " +str(i)+ " passed.")
            testPassed=True
    if (testPassed==True):
                
        print("Next Permutation of "+str(permutationArray)+ " is: " + str(testArray))

    #TEST 2
    print("Results for permutation 2")


    # reset to true for new tests
    testPassed=True

    # second array: 4 (right) 3(left) 1 (right) 2 (left)
    array2=[Element(4, 1), Element(3, -1), Element(1, 1), Element(2, -1)]
    permutation2=Permutation(array2)
    permutationArray2=[]
    for i in range(len(permutation2.array)):
        permutationArray2.append(permutation2.array[i].value)

    # expected values
    testArray2=[3, 4, 1, 2]

    # expected directions
    testArray3=[-1, 1, 1, -1]
    
    nextPerm2=permutation2.nextPermutation()


    # if either a value or a direction is not as expected, test failed
    for i in range(len(nextPerm2.array)):
        if (nextPerm2.array[i].value!=testArray2[i]):
            print("Value error found in position: "+ str(i))
            print(nextPerm2.array[i].value)
            testPassed=False
        if (nextPerm2.array[i].direction!=testArray3[i]):
            print("Direction error found in position: "+str(i))
            testPassed=False
        else:
            print("Test for element at " +str(i)+ " passed.")
            testPassed=True
            
    if (testPassed==True):
                
        print("Next Permutation of "+str(permutationArray2)+" is: " + str(testArray2))


    testPassed=True

    #TEST 3

    print("Results for permutation 3")
    array3=[Element(1, -1), Element(2, -1), Element(3, -1), Element(4, -1),
            Element(5, -1), Element(6, 1)]
    permutation3=Permutation(array3)
    nextPerm3=permutation3.nextPermutation()

    permutationArray3=[1, 2, 3, 4, 5, 6]
    testArray4=[1, 2, 3, 5, 4, 6]
    testArray5=[-1, -1, -1, -1, -1, -1]


    for i in range(len(nextPerm3.array)):
        if (nextPerm3.array[i].value!=testArray4[i]):
            print("Value error found in position: "+ str(i))
            print(nextPerm3.array[i].value)
            testPassed=False
        if (nextPerm3.array[i].direction!=testArray5[i]):
            print("Direction error found in position: "+str(i))
            testPassed=False
        else:
            print("Test for element at " +str(i)+ " passed.")
            testPassed=True
            
    if (testPassed==True):
                
        print("Next Permutation of "+str(permutationArray3)+" is: " + str(testArray4))

    # TEST 4

    print("Results for permutation 4")
    array4=[Element(2, -1), Element(1, -1), Element(3, 1)]
    permutation4=Permutation(array4)
    nextPerm4=permutation4.nextPermutation()

    permutationArray4=[]
    for i in range(len(permutation4.array)):
        permutationArray4.append(permutation4.array[i].value)
        
    if(nextPerm4!=False):
        print("Error in permutation with no next permutation.")
    else:
        print("Permutation "+str(permutationArray4)+ " has no next permutation")

    
def permute(n):
    
    # generate array
    permuteArray=[]
    permutationArray=[]

    # makes array of values
    for i in range (1, n+1):
        permuteArray.append(i)

    # makes array of elements
    for element in permuteArray:
        el=Element(element,-1)
        permutationArray.append(el)

    # print the first permutation  
    permutation=Permutation(permutationArray)
    firstArray=[]
    for i in range(len(permutation.array)):
            firstArray.append(permutation.array[i].value)
    print(firstArray)

    # while there is still a mobile element        
    while permutation.anyMobile():
        returnArray=[]

        # call next permutation
        permutation=permutation.nextPermutation()
        for i in range(len(permutation.array)):
            returnArray.append(permutation.array[i].value)

        # print new permutation
        print(returnArray)
        
# extra clarifying test
def mytest():
    perm=Permutation([Element(3,-1),Element(1,-1),Element(2,-1)])
    print(perm.isMobile(2))
    print(perm.anyMobile())
    print(perm.largestMobile()) 

def test():
    permute(1)
    permute(2)
    permute(3)
    permute(4)
    permute(5)

# accounts for time to make all of the permutations
def permuteTime(n):
    startTime=time.time()
    permute(n)
    endTime= time.time()
    print ("Printing the permutations of ",n,
           " elements takes ",endTime-startTime, " seconds")

test()

