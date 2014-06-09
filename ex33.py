numbers = []
def add_numbers(elems, increm):
	i = 0
	print elems
	#while i < elems * increm:
	for i in range(0, elems):
		print "At the top, i is %d" % i
		numbers.append(i)
	
		#i += increm
		print "Numbers now: ", numbers
	
		print "At the bottom, i is %d" % i
	return

nums = int(raw_input("How many elements do you want in the list? "))
increment = int(raw_input("How much do you want to increment each time? "))
add_numbers(nums, increment)
print "The numbers: "
for num in numbers:
	print num