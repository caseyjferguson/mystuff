name = 'Casey J. Ferguson'
age = 23
height = 68
weight = 222
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_cm = height * 2.54
weight_kilo = weight * .453592

print "Let's talk about %s." % name
print "He's %d inches tall and %f centimeters tall." % (height, height_cm)
print "He's %d pounds heavy and %f kilograms heavy." % (weight, weight_kilo)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (height, weight, age, height + weight + age)