list = [5,6,77,45,22,12,24]
print ("Original list:")
print (list)
for i  in list:
	if(i%2 == 0):
	    list.remove(i)
print ("list after removing EVEN numbers:")
print (list)
