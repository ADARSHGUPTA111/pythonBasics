name="shaun"
age=20
print(type(name))

nums=[1,2,3,4]
print(type(nums))

class Planet:
	#here comes different variables and methods of a class
	#we apply class level attribute if it is common to all instances(here above init)

	shape="round"
	def __init__(self,name,radius,gravity,system):
		#like a constructor (self has to be passed)
		#wherever self is seen its instance attribute(under init) and instance method
		self.name=name
		self.radius=radius
		self.gravity=gravity
		self.system=system

	def orbit (self):#this is an instance method since self
		return f'{self.name} is orbiting in the {self.system}'

	@classmethod#this is the class method(common to all planets) 

	def commons(cls):#cls is the class acessible to both
		return f'All the planets are {cls.shape} because of gravity'


	@staticmethod 
	#it doesn't have access to the self and to the class
	#can be used for overriding the default values

	def spin(speed="2000 miles per hour"):#default speed
		return f'The planet spins and spins at {speed}'

naboo=Planet("Naboo",3000000,8,'Naboo System')
hoth=Planet('Hoth',200000,5.5,"hoth system")
#the object of planet is created

print(Planet.spin())
print(naboo.spin())

print(hoth.spin("at a very high  speed"))#we overridden the value

print(f'Name is : {hoth.name}')
print(f' radius sis {hoth.radius}')
print(f'The gravity is {hoth.gravity}')

print(hoth.orbit())


print(f'{naboo.name} is its name')
print(f'{naboo.radius} is it')
print(f'{naboo.gravity} is its power ')

print(naboo.orbit())

print(Planet.shape)
print(naboo.shape)
#you can access the shape by the name of the class itself
#even by the innstance name we can achieve the shape
# print(Planet.name) this would give an error 

print(Planet.commons())
print(naboo.commons())
#both the class and the instance of the class can access the commons class

# instance attributes->instance only
# class-level attributes->instance and class 
# class methods ->instance and class 
# staticmethod->instance and class