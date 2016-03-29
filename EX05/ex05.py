# -*- coding:cp949
my_name = 'Yoon Kim'
my_age = 21 # not a lie
my_height_cm = 180
cm_to_inch = 1.0 / 2.54
my_height_inch = my_height_cm * cm_to_inch
my_weight_kg = 77
my_eyes = "Black"
my_teeth = "White"
my_hair = "Black"
# place holder
print "Let's talk about %s." % my_name
print "He's %g centimiters tall. " % my_height_cm    # %g는 소수점을 나타낸다
print "He's %g inches tall."  % my_height_inch
print "He's %d kilograms heavy." % my_weight_kg   # %d는 숫자열을 나타낸다
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)   # %s는 문자열을 나타낸다
print "His teeth are usually %s depending on the coffee." % my_teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height_cm, my_weight_kg, my_age + my_height_cm + my_weight_kg)



