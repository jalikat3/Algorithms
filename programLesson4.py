
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def snafu():
    snafu()



def recursiveFunc(k):
    if k==0:
        return 5
    else:
        return recursiveFunc(k-1)+7

def recursiveFib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return recursiveFib(n-1)+recursiveFib(n-2)
