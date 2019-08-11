a=input("enter a string")
all_freq = {} 
  
for i in a: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
  
 
print ("Count of all characters in a is :\n "
                                        +  str(all_freq)) 

