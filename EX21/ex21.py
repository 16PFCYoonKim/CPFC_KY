#-*-coding:cp949
def add (a, b):
    print "ADDING %d + %d" % (a, b)
    return  a + b

def subtract (a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return  a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add (30, 5)
height = subtract (78, 4)
weight = multiply (82, 3)
IQ = divide (120, 4)

print "Age: %d, Height: %d, Weight: %d, IQ: %d " % (age, height, weight, IQ)

# A puzzle for the extra credit,type it in anyway.
print "Here is a puzzle."

what = add (age, subtract(height, multiply(weight, divide(IQ, 2)))) #devide가 먼저실핼

print "That's becomes: ", what, "Can you do it by hand?"
