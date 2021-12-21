class Element():
    def __init__(self,value,direction):
        self.value=value
        self.direction=direction

class Permutation():
    def __init__(self,array):
        self.array=array
        
# where to put this....        
    def isMobile(self, position):
        left=True
        right=True
        element=self.array[position]

        if position>0:
            elementLeft=self.array[position-1]
        else:
            left=False

        if position>=len(self.array)-1:
            right=False
        else:
            elementRight=self.array[position+1]
        
        
        if right and (element.direction==1 and element.value>elementRight.value):
            return True
        elif left and (element.direction==-1 and element.value>elementLeft.value):
            return True
        else:
            return False
        
    def anyMobile(self):
        
        for i in range(len(self.array)):
            if(self.isMobile(i)==True):
                return True
        return False
    
    def largestMobile(self):

        mobile=0
        isMobile=self.isMobile(0)
        for i in range(len(self.array)):
            if self.isMobile(i) and self.array[i].value>self.array[mobile].value:
                mobile=i
                isMobile=True
            
        if isMobile==True:        
            return mobile
        else:
            return "no mobile found"

    def nextPermutation(self):

        mobile=0
        for i in range(len(self.array)):
            if self.isMobile(i) and self.array[i].value>self.array[mobile].value:
                mobile=i
            
                
        if self.isMobile(mobile)==False:
            return False
        else: 
            returnArray=[]
            element=self.array[mobile]
            
            if (element.direction==1 and self.isMobile(mobile)==True):

                temp=element
                self.array[mobile]=self.array[mobile+1]
                self.array[mobile+1]=temp
                
            elif (element.direction==-1 and self.isMobile(mobile)==True):

                temp=element
                self.array[mobile]=self.array[mobile-1]
                self.array[mobile-1]=temp
                

            
                
            for i in range(len(self.array)):
                returnArray.append(self.array[i].value)

            return returnArray
            
        
        
            
def changeDirection(element):
    element.direction=element.direction*(-1)

def testChangeDirection():
    element=Element(1, -1)
    changeDirection(element)
    print("Given a direction of -1, switch direction.")
    print("Direction is now: ")
    print(element.direction)
    element2=Element(2,1)
    changeDirection(element2)
    print("Given a direction of 1, switch direction.")
    print("Direction is now: ")
    print(element2.direction)

def testPermInitializer():

    # first array: 1 (left) False 2 (right) False 3 (left) True 4(right) False
    array1=[Element(1, -1), Element(2, 1), Element(3, -1), Element(4, 1)]
    permutation=Permutation(array1)
    
    print(permutation.array[0].value)
    print(permutation.array[0].direction)
    print(permutation.array[1].value)
    print(permutation.array[1].direction)
    print(permutation.array[2].value)
    print(permutation.array[2].direction)
    print(permutation.array[3].value)
    print(permutation.array[3].direction)
    
    print(permutation.isMobile(0))
    print(permutation.isMobile(1))
    print(permutation.isMobile(2))
    print(permutation.isMobile(3))

    print(permutation.anyMobile())

    print(permutation.largestMobile())

    print(permutation.nextPermutation())

    # second array: 4 (right) 3(left) 1 (right) 2 (left)
    array2=[Element(4, 1), Element(3, -1), Element(1, 1), Element(2, -1)]
    permutation2=Permutation(array2)
    print("START PERM 2")
    print(permutation2.array[0].value)
    print(permutation2.array[0].direction)
    print(permutation2.array[1].value)
    print(permutation2.array[1].direction)
    print(permutation2.array[2].value)
    print(permutation2.array[2].direction)
    print(permutation2.array[3].value)
    print(permutation2.array[3].direction)
    
    # element 0 is mobile
    print(permutation2.isMobile(0))

    # element 1 is not mobile
    print(permutation2.isMobile(1))

    # element 2 is not mobile
    print(permutation2.isMobile(2))

    # element 2 is mobile
    print(permutation2.isMobile(3))

    # there is a mobile element
    print(permutation2.anyMobile())

    # largest mobile=3
    print(permutation2.largestMobile())

    # next permutation: 4, 3, 1, 2
    print(permutation2.nextPermutation())


    array3=[Element(4, 1), Element(5, -1), Element(1, 1), Element(2, -1)]
    permutation3=Permutation(array3)
    print(permutation3.nextPermutation())

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
    returnArray=[permutation]

    # while there are still permutations to be found
    while permutation.nextPermutation()!=False:
        returnArray.append(permutation.nextPermutation())
        
    return returnArray


def test():
    permute(3)
    permute(4)
    
    

    
    

