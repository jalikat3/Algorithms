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
        

def testChangeDirection():
    element=Element(1, -1)
    print("Given a direction of " + str(element.direction) +", switch direction.")
    element.changeDirection()
    print("Direction is now: "+ str(element.direction))
    element2=Element(2,1)
    print("Given a direction of " +str(element2.direction)+" switch direction.")
    element2.changeDirection()
    print("Direction is now: " +str(element2.direction))


def testPermInitializer():

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
    # first array: 1 (left) False 2 (right) False 3 (left) True 4(right) False
    array1=[Element(1, -1), Element(2, 1), Element(3, -1), Element(4, 1)]
    permutation=Permutation(array1)
    testArray=[False, False, True, False]

    print("Testing mobility of elements")
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
    
def testCompiled():
    testElementInitializer()
    testChangeDirection()
    testPermInitializer()
    testIsMobile()
    testAnyMobile()
    testLargestMobile()
    testNextPermutation()
    
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



