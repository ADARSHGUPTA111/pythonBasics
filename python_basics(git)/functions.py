def greet():
	print('Hello , everyone')

greet()

def greet(name,time):
	print(f' Good {time} {name}, hope you are doing great ')

name=input("Enter the name")
time=input('enter the time of the day')

greet(name,time)

def greet1(name="shilpa",time="noon"):
	print(f' Good {time} {name}')
greet1()
#there are default arguments in here
greet1(name="adasrh")
# the default parameter could be changed 

radius=int(input("Enter the radius"))
length=int(input("Enter the length"))

def area(radius):
	return 3.142*radius*radius

def vol(area,length):
	print(area*length)

area_calc=area(radius)
vol(area_calc,length)

vol(area(radius),length=)




