ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while 10 != (len(stuff)):
    next_one = more_stuff.pop()
    print ("Adding: %s" % next_one)
    stuff.append(next_one)
    print ("There are %d items now." % len(stuff))

print ("There we go: %s" % str(stuff))
print ("Let's do some things with stuff")

print ("stuff[1] = %s" % stuff[1])
print ("stuff[-1] = %s" % stuff[-1])
print ("stuff.pop() = %s" % stuff.pop())
print (' ' .join(stuff))
print ('#' .join(stuff[3:5]))