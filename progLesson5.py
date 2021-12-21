class MyData():
    def __init__(self,name,number):
        self.name=name
        self.number=number

def test():
    new =MyData("David",68)
    print(new.name,new.number)
    
def readData():
    dataFile=open('Lesson5CSV.csv','r')
    objectList=[]
    for line in dataFile:
        thisline=line.split(',')
        name=thisline[0]
        number=int(thisline[1])
        objectList.append(MyData(name,number))
    dataFile.close()
    return objectList

def testReadData():
    storedList=readData()
        
    for obj in storedList:
        print(obj.name+" "+str(obj.number))
        
def sortByName():
    myList = readData()
    
    for index in range(1,len(myList)):
        temp = myList[index]
        secondIndex = index - 1
        while secondIndex>=0 and myList[secondIndex].name > temp.name:
            myList[secondIndex+1]=myList[secondIndex]
            secondIndex = secondIndex-1
        myList[secondIndex+1] = temp    
    # Print the data in name order
    for item in myList:
        print(item.name,item.number)
        
def sortByNumber():
    myList = readData()
    
    for index in range(1,len(myList)):
        temp = myList[index]
        secondIndex = index - 1
        while secondIndex>=0 and myList[secondIndex].number > temp.number:
            myList[secondIndex+1]=myList[secondIndex]
            secondIndex = secondIndex-1
        myList[secondIndex+1] = temp    
    # Print the data in number order
    for item in myList:
        print(item.name,item.number)

def writeToTextfile():
    results = open('Lesson5results.text','w')
    myList=readData()
    for index in range(5):
        results.write(myList[index].name+'\n')
    results.close()
