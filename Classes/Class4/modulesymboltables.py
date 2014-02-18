a = 0
def myName():
    print "When called by a function in my namespace, my name is", __name__
def whatisa():
    print a
def whatisglobala():
    global a
    print a
print "Right now, my name is:", __name__
