#decorator satrts with a @ and sits at the top of thee function
# it is a function itself! and can be used multiple times above any function!

def cough_dec(func):
	def func_wrapper():
		#code before function
		print('*cough*')
		func()
		#code after function
		print('*cough*')
	return func_wrapper


@cough_dec
def question():
	print("Can you give me a discount on that?")

question()

@cough_dec
def answer():
	print("It's only 50p you cheapskate")

answer()
