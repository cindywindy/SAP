from flask import Flask
app = Flask(__name__) #constructor

@app.route("/")
def welcome():
    return "Welcome!"

#time & space complexity- linear. O(n)
@app.route("/<int:countey>") 
def countey(countey):
    retVal = ""
    for x in range(1,countey+1):
        retVal += str(x)+" "
    return retVal

#time & space complexity- linear. O(2n) -> O(n)
@app.route("/<int:countey>/odd") 
def countey1(countey):
    retVal1 = ""
    if countey < 1:
        return "No odd numbers."
    for x in range(1,countey+1):
        if x % 2 != 0:
            retVal1 += str(x)+" "
    return retVal1

#time & space complexity- linear. O(n)
@app.route("/<int:countey>/even")
def countey2(countey):
    retVal2 = ""
    for x in range(0,countey+1):
        if x % 2 == 0:
            retVal2 += str(x)+" "
    return retVal2

#time complexity- quadratic. O(n^2)
#space complexity- linear. O(n)
@app.route("/<int:countey>/prime")
def prime(countey):
    retVal3 = ""
    if countey < 2:
        return "No prime numbers."
    for potentialPrime in range(2,countey+1):
        prime = True
        for i in range(2,potentialPrime):
            if (potentialPrime % i == 0):
                prime = False
        if prime:
            retVal3 += str(potentialPrime) + " "
    return retVal3