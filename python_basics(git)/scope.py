my_name="kajol"

print("Remember outside the function it's now",my_name)

def print_name():
	my_name="shilpa"
	print("The name inside the function is",my_name)

print_name()

def print_name():
	global my_name
	my_name="anjali"
	print("The name inside the function is",my_name)


print_name()
print("Now outside the function is (after using global) ",my_name)