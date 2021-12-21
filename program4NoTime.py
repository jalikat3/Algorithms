class Element():
    def __init__(self,value,direction):
        self.value=value
        self.direction=direction

    # note: I have not tested this yet, I saw that I had in
    # wrong place in office hours
    def changeDirection(self):
        self.direction=self.direction*-1

class Permutation():
    def __init__(self,array):
        self.array=array
        
    def isMobile(self, position):
        left=True
        right=True
        element=self.array[position]

##        value=self.array[position].value
##        direction=self.array[position].direction
##
##        if((position+direction)<0 or (position+direction)>=len(self.array)):
##            return False
##        
##        nextElementVal=self.array[position+direction].value
##
##        if (value>nextElementVal):
            

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
        if (right==True and (element.direction==1 and element.value>elementRight.value)):
            return True

        # if there is an element to the left, the current element points left,
        # and the element's value is greater than the element on the left
        elif (left==True and (element.direction==-1 and element.value>elementLeft.value)):
            return True
        else:
            return False
        
    def anyMobile(self):
        
        for i in range(len(self.array)):
            if(self.isMobile(i)==True):
                
                return True
        return False
    
    def largestMobile(self):

        if(self.anyMobile()==False):
            return False
        else:
            for i in range(len(self.array)):

                # set element to first mobile element
                if(self.isMobile(i)==True):
                    maxPosition=i
                    break
            for i in range(len(self.array)):
                if self.isMobile(i) and self.array[i].value>self.array[maxPosition].value :
                    maxPosition=i

            

            return maxPosition
            

    def nextPermutation(self):
        if(self.anyMobile()):
            mobilePosition=self.largestMobile()
        
        else:
            return False

            
         
        returnArray=[]
        element=Element(self.array[mobilePosition].value, self.array[mobilePosition].direction)
        
        
        if (element.direction==1):

            self.array[mobilePosition]=self.array[mobilePosition+1]
            self.array[mobilePosition+1]=element
            
        elif (element.direction==-1):

            self.array[mobilePosition]=self.array[mobilePosition-1]
            self.array[mobilePosition-1]=element
            

        
            
        for i in range(len(self.array)):
            if (self.array[i].value>element.value):
                self.array[i].changeDirection()
            
            
        
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
            print(str(permutation.array[i].value)+", " +str(permutation.array[i].direction))
            
        

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
            print(str(permutation2.array[i].value)+", " +str(permutation2.array[i].direction))
            

def testIsMobile():
    # first array: 1 (left) False 2 (right) False 3 (left) True 4(right) False
    array1=[Element(1, -1), Element(2, 1), Element(3, -1), Element(4, 1)]
    permutation=Permutation(array1)
    testArray=[False, False, True, False]

    print("Testing mobility of elements")

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

    print("Testing test for failing values (all should be error unless same value)")
    for i in range(len(permutation2.array)):
        if(permutation2.isMobile(i)!=testArray[i]):
            print("isMobile error found in position: "+str(i))
        else:
            print("Element at "+ str(i)+": " +str(permutation.isMobile(i)))
    

def testAnyMobile():
    # first array: 1 (left) False 2 (right) False 3 (left) True 4(right) False
    array1=[Element(1, -1), Element(2, 1), Element(3, -1), Element(4, 1)]
    permutation=Permutation(array1)

    # second array: 4 (right) 3(left) 1 (right) 2 (left)
    array2=[Element(4, 1), Element(3, -1), Element(1, 1), Element(2, -1)]
    permutation2=Permutation(array2)

    array3=[Element(4, -1), Element(3, -1), Element(1, 1), Element(2, 1)]
    permutation3=Permutation(array3)

    print("Testing for any mobile element in permutation")
    # true
    print("Expected: true "+str(permutation.anyMobile()))
    print("Expected: true "+str(permutation2.anyMobile()))
    print("Expected: false "+str(permutation3.anyMobile()))
    # there is a mobile element
    

def testLargestMobile():

    # first array: 1 (left) False 2 (right) False 3 (left) True 4(right) False
    array1=[Element(1, -1), Element(2, 1), Element(3, -1), Element(4, 1)]
    permutation=Permutation(array1)
    position=permutation.largestMobile()
    
    print("Testing permutation 1: ")
    if(position!=2):
        print("Error in largest mobile, expected 2 but found: "+str(position))
    else:
        print("Largest mobile element is at position: "+str(position))
        print("Value of largest mobile element: "+str(permutation.array[permutation.largestMobile()].value))

    # second array: 4 (right) 3(left) 1 (right) 2 (left)
    array2=[Element(4, 1), Element(3, -1), Element(1, 1), Element(2, -1)]
    permutation2=Permutation(array2)

    position2=permutation2.largestMobile()
    
    print("Testing permutation 2: ")
    if(position2!=0):
        print("Error in largest mobile, expected 0 but found: "+str(position2))
    else:
        print("Largest mobile element is at position: "+str(position2))
        print("Value of largest mobile element: "+str(permutation2.array[permutation2.largestMobile()].value))

def testNextPermutation():
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
    nextPermArray=[]


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
                
        print("Next Permutation of "+str(permutationArray2)+ " is: " + str(testArray2))
    
   


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

    # makes array of numbers
    for i in range (1, n+1):
        permuteArray.append(i)

    # makes array of elements
    for element in permuteArray:
        el=Element(element,-1)
        permutationArray.append(el)
        
    permutation=Permutation(permutationArray)

    # while there are still permutations to be found
    #nextPerm=permutation.nextPermutation()
    
    #firstArray=[permutation]
    firstArray=[]
    for i in range(len(permutation.array)):
            firstArray.append(permutation.array[i].value)
    print(firstArray)
            
    while permutation.anyMobile():
        returnArray=[]
        permutation=permutation.nextPermutation()
        for i in range(len(permutation.array)):
            returnArray.append(permutation.array[i].value)
        print(returnArray)
        #nextPerm=nextPerm.nextPermutation()
        

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
    


