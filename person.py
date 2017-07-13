#defines age and print out 'What your age?'
def get_age():
	age = raw_input("Whats your age?")
	return age #returns age

#defines name and print out 'whats your name?'
def get_name():
	return raw_input("whats your name?")

age = get_age()#calling age
name = get_name()#calling age

print "Hey, " + name + ", you are " + age + "years old, dude!"
