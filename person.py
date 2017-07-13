def get_age():
	age = raw_input("Whats your age?")
	return age

def get_name():
	return raw_input("whats your name?")

age = get_age()
name = get_name()
print "Hey, " + name + ", you are " + age + "years old, dude!"
