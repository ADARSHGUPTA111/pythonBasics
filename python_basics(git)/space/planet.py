class Planet:
	  
	shape="round"
	def __init__(self,name,radius,gravity,system):
		
		self.name=name
		self.radius=radius
		self.gravity=gravity
		self.system=system

	def orbit (self):#this is an instance method since self
		return f'{self.name} is orbiting in the {self.system}'

	@classmethod
	def commons(cls):#cls is the class acessible to both
		return f'All the planets are {cls.shape} because of gravity'


	@staticmethod 
	
	def spin(speed="2000 miles per hour"):#default speed
		return f'The planet spins and spins at {speed}'

