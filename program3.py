'''
    program3.py
    Jali Purcell
    10/03/21
    For program 3 of Algorithms

    bruteForceStringMatch:
        input: two strings: a text Text, and pattern Pattern
        output: the location of the pattern in the string
        or a -1 if location is not found

        MODIFICATION: implemented the algorithm
        on page 105 into code, added clarifying comments

        added index in range 0 to (textLength-patternLength)+1,
        so that the last element that could find the pattern in
        the text is looked at

        I put the if positionInPattern==patternLength
        statement inside the while loop, so
        if an empty pattern was searched, the if statement
        would not compute for positionInPattern==patternLength
        (0==0) and return 0 when -1 is the right answer

        changed single letter variables to descriptive variables

        put if statement back inline with while loop so that
        the empty set is found (first place found=0) (Fixed in
        office hours)

    testCaseA:
        input: integer testNumber, longText string (text)
        searchString string (pattern) and expectedResult integer
        output: print statement of either pass or fail using
        result from bruteForceStrengthMatch

        MODIFICATION: fixed formatting errors by adding
        paranthesis

    testA:
        output: result of testCaseA for each test
        purpose: determine if the bruteForceStringMatch
        function works corrrectly, by calling testCaseA

        MODIFICATION: added two additional tests

        added more tests extending from what I put on the Word
        document to fine tune my code

    bruteForceStringMatch2:
        input: two strings: a text, and pattern
        output: the last instance of the pattern's
        location in the text, or a -1 if no location
        exists

        MODIFICATION: by using bruteForceStringMatch,
        I changed what happens if positionInPattern==patternLength.
        Instead of returningnautomatically, the location is saved,
        and printed at the end. That way, the location can update
        anytime positionInPattern==patternLength for index in
        range (0, (textLength-patternLength).

        I used the boolean variable found to return location
        if one is found, or -1 if not found.
        Found is initialized as False.

        added index in range 0 to (textLength-patternLength)+1,
        so that the last element that could find the pattern
        in the text is looked at

        I put the if positionInPattern==patternLength
        statement inside the while loop, so
        if an empty pattern was searched, the if statement
        would not compute for positionInPattern==patternLength
        (0==0) and return 0 when -1 is the right answer

        changed single letter variables to descriptive variables

        put if statement back inline with while loop so that
        the empty set is found (Last place found=18) (Fixed in
        office hours)

    testCaseB:
        input: integer testNumber, longText string (text)
        searchString string (pattern) and expectedResult integer
        output: print statement of either pass or fail using
        result from bruteForceStrengthMatch2

        MODIFICATION: fixed formatting errors by adding
        paranthesis

    testB:
        output: result of testCaseB for each test
        purpose: determine if the bruteForceStringMatch2
        function works corrrectly, by calling testCaseB

        MODIFICATION: added two additional tests, one where
        the pattern is located twice in the text

        added more tests extending from what I put on the Word
        document to fine tune my code
                
'''

def bruteForceStringMatch(Text, Pattern):

    # initialize variables for length of Text and Pattern 
    textLength=len(Text)
    patternLength=len(Pattern)

    # look through all elements until what's left is too short
    for index in range (0, (textLength-patternLength)+1):
        
        # positionInPattern is 0 when first letter is not found
        positionInPattern=0
        
        # while there is still letters to find
        # and pattern letter=text letter
        while (positionInPattern < patternLength
            and Pattern[positionInPattern]==Text[index+positionInPattern]):
            
            # iterate positionInPattern
            positionInPattern=positionInPattern+1
            
            # if all letters in text are found
        if positionInPattern==patternLength:
            
                # return index of text where pattern is
            return index
            #return patternLength
        
    # return -1 if not found   
    return -1
    

def testCaseA(testNumber,longText,searchString,expectedResult):
    actualResult = bruteForceStringMatch(longText,searchString)
    if actualResult == expectedResult:
        print ("Test",testNumber,"passed.")
    else:
        print ("Test",testNumber,"failed.  Expected",expectedResult, "but found",actualResult)


def testA():
    testCaseA(1,"Oh I wish I were an aardvark.","were",12) 
    testCaseA(2,"Oh I wish I were an aardvark.","join",-1) 
    testCaseA(3,"She sells sea shells by the seashore.","seashore",28)
    testCaseA(4, "instinct is something you polish", "some", 12)
    testCaseA(5, "I made it to nationals", "true", -1)

    # more test cases
    testCaseA(6, "one two three four", "one", 0)
    testCaseA(7, "one two three four", "four", 14)
    testCaseA(8, "one two three four", "", 0)
    testCaseA(9, "one two three four", "o", 0)
    testCaseA(10, "one two three four", "twa", -1)


def bruteForceStringMatch2(Text, Pattern):

    #initialize variables for length of Text and Pattern  
    textLength=len(Text)
    patternLength=len(Pattern)

    # position of text is initially 0, found is False (not found)
    position=0
    found=False;

    # look through all elements until what's left is too short
    for index in range (0, (textLength-patternLength)+1):

        # positionInText is initially 0 when text is not found
        positionInPattern = 0

        # while there is still letters to find
        # and pattern letter=text letter
        while (positionInPattern < patternLength
            and Pattern[positionInPattern]==Text[index + positionInPattern]):

            # iterate positionInText
            positionInPattern = positionInPattern + 1

            # if whole pattern is found
        if positionInPattern == patternLength:

                # mark position as index, found=True
                # this can be updated for new instances
            position=index
            found=True

    # after looking through text, if found
    if found==True:

        # return last updated position
        return position

    # if not found
    if found==False:

        # return -1
        return -1
    
def testCaseB(testNumber,longText,searchString,expectedResult):
    actualResult = bruteForceStringMatch2(longText,searchString)
    if actualResult == expectedResult:
        print("Test",testNumber,"passed.")
    else:
        print("Test",testNumber,"failed.  Expected",expectedResult, "but found",actualResult)

def testB():
    testCaseB(1,"Oh I wish I were an aardvark.","I w",10)
    testCaseB(2,"Oh I wish I were an aardvark.","anteater",-1)
    testCaseB(3,"She sells sea shells by the seashore.","sea",28)
    testCaseB(4, "instinct is something you polish", "in", 18)
    testCaseB(5, "cauliflower", "r ", -1)

    # more test cases
    testCaseB(6, "one two three four", "one", 0)
    testCaseB(7, "one two three four", "four", 14)
    testCaseB(8, "one two three four", "", 18)
    testCaseB(9, "one two three four", "o", 15)

