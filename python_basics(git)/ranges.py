
for n in range(5):
	#0-4
	print(n,end=' ')

print("\n")

for n in range(3,10):
	print(n,end=' ')

print("\n")

for x in range(0,20,4):
	print(x,end=' ')

#the third parameter is set as 1 by default ;
# you can change it as per your wish
print('\n')
burgers=['beef','chicken','veg','supreme','double']

for n in range(len(burgers)):
	print(n,burgers[n])
#if you seperate in print by a comma then space comes automatically
print("\n")
for  n in range(len(burgers)-1,-1,-1):
	print(n,burgers[n])
#this is how you print the list in reverse order 
#use range(-1,-1,-1)
#-1-> takes you to the end -1->takes you to the beginning(as 0 will be included)
#then the -1-> takes you backward one step at a time
