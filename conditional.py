#i = 8
#if(i % 2):
#    print "Odd Number"
#else:
#    print "Even Number"



num = [1,2,3,4,5,6,7,8,9,10]
ans = 0  
for i in num:
	if not(i % 2):
		ans += i
 
print ans
