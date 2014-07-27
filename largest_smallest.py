smallest_so_far = None
largest_so_far = None
       
while True:
    num = raw_input('Enter a number: ');

    if num == "done":
        break
    try:
        num = int(num)
        
	if smallest_so_far is None:
		smallest_so_far = num
	elif num < smallest_so_far:
		smallest_so_far = num
	
	if largest_so_far is None:
		largest_so_far = num
	elif num > largest_so_far:
		largest_so_far = num
        
    except:
        print "Invalid input"
        continue
print "Maximum is", largest_so_far
print "Minimum is", smallest_so_far