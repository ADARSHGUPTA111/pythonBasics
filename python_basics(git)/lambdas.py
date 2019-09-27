#lambdas are known as the anonymous functioin 
#they dont need the name or identifier as they are just used once

nums=[1,2,3,4,5,6]

def squared(n):
	return n**2

print(list(map(squared,nums)))

#using lambda

# lambda n:n*n for squaring
#we define the whole function in just a single line

print(list(map(lambda n:n*n,nums)))
#this thing does the exactly same thing


# print(list(map(lambda n,x:n*n,nums)))
# just to demonstrate how you can use two variables for a function