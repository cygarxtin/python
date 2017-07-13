def calculate (num1, num2, a):
	print "add, substract, multiply or divide"
	result = raw_input("Type your choice: ")
	if a == "add":
		return num1 + num2
	elif a == "substract":
		return num1 - num2
	elif a == "multiply":
		return num1 * num2
	else: 
		a == "divide"
	return num1 / num2
	
	
	
#result = calculate(4,6, "add")
#print result	
		
def get_num1():
	num1 = int(raw_input("Enter your First number: "))
	return num1
	
def get_num2():
	num2 = int(raw_input("Enter your Second number: "))
	return num2
	
num1 = get_num1()
num2 = get_num2()	
calculate = calculate

	
	
print calculate()
