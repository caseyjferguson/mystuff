from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want this, press ctrl-c."
print "Otherwise, press enter."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line_1 = raw_input("Line 1: ")
line_2 = raw_input("Line 2: ")
line_3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line_1, line_2, line_3))


print "Finally, we close the file."

target.close()