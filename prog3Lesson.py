class Element:
    def __init__(self,value):
        self.value = value
        self.indicator = (-1)**value
def main():
    initialArray=[Element(x) for x in range(1,11)]
    print(initialArray[4].value,initialArray[4].indicator)
    print(initialArray[0].value,initialArray[0].indicator)
    print(initialArray[4].value,initialArray[0].indicator)
    print(initialArray[2].value,initialArray[2].indicator)
    print(initialArray[6].value,initialArray[6].indicator)
    print(initialArray[8].value,initialArray[8].indicator)

    indicatorArray=[Element(x) for x in range(1, 11)]
    print([indicatorArray[index].value for index in range(0, 10)
          if indicatorArray[index].indicator==-1])
    


def myfun(mylist):
    indexList=[index for index in range (0, len(mylist)-1)
               if mylist[index] < mylist[index+1]]
    if len(indexList)==0:
        return "no value is less than the next value"
    else:
        return indexList[0]
