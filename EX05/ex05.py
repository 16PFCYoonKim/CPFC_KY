# -*- coding:cp949
name = 'Yoon Kim'
age = 21 # not a lie
height_cm = 180
cm_to_inch = 1.0 / 2.54
height_inch = height_cm * cm_to_inch
weight_kg = 77
eyes = "Black"
teeth = "White"
hair = "Black"
# place holder
print "Let's talk about %s." % name
print "He's %g centimiters tall. " % height_cm    # %g�� �Ҽ����� ��Ÿ����
print "He's %g inches tall." % height_inch
print "He's %d kilograms heavy." % weight_kg   # %d�� ���ڿ��� ��Ÿ����
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)   # %s�� ���ڿ��� ��Ÿ����
print "His teeth are usually %s depending on the coffee." % teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)



