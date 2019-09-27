#dictionaries act as a key value pair
ninja_belts={"crystal":"red","ryu":"black"}
print(ninja_belts)

print(ninja_belts['crystal'])
#this returns the value associated with this key

#how to check whether there exists a key in the given dictionary or not
#use key in dict

print('yoshi' in ninja_belts)#returns false

print(ninja_belts.keys())
print(list(ninja_belts.keys()))
#now see we can type cast into the list as per our wish

print(ninja_belts.values())
print(list(ninja_belts.values()))

#useful in cp as you can then convert the keys into a list and then work on it!
vals=list(ninja_belts.values())
print(vals)

print(vals.count('black'))
#this prints the number of occurences in the vals list

ninja_belts['yoshi']="red"
print(ninja_belts)
# adding a new key into our existing dict is so fucking easy!

#alternate way to make a dictionary

person=dict(name="adarsh",age=27,height="6ft")
print(person)

def ninja_intro(dictionary):
	for key,val in dictionary.items():
		print(f' I am {key} is {val} colour belt')

ninja_belts={}

while True:
	ninja_name=input("Enter the ninja name")
	ninja_belt=input("Enter the belt colour")
	ninja_belts[ninja_name]=ninja_belt

	another=input("add another?(y/n)")

	if another=='y':
		continue
	else:
		break

ninja_intro(ninja_belts)