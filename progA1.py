# Answers for programming assignment 1 for Algorithms

# Jali Purcell

# 08/25/2021


def capitalizeFirst(string):
    if type(string)!=str:
        print("Please try again with a string parameter")
    else:
        remaining=" "
        stringList=string.split()
        for word in stringList:
            remaining=remaining+ " "+ word.capitalize()
        print(remaining)

capitalizeFirst("My STRING example")
capitalizeFirst("here is another example")
capitalizeFirst("OnE MORE for Good MEasure")
capitalizeFirst(8)

