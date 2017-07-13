#initialised i
i = 8
if(i % 2):
    print "Odd Number"#print out 'Odd Number'
else:
    print "Even Number"#print out 'Even Number'



num = [1,2,3,4,5,6,7,8,9,10]#calling num
ans = 0  
#for loop statement
for i in num:
	if not(i % 2):
		ans += i
 #print out the result = 30
print ans
