str="hello there dude"

print(str.split(' '))
#it gets split into a list at the places where it sees the spaces

fib1=[1,1,2,3,5,8,13]
print(fib1)

print(fib1[2])
print(fib1[-3])
#slicing
print(fib1[0:4])

fib2=[21,34,55]

print(fib1+fib2)

fib1[0]=9
print(fib1)

fib=fib1+fib2
print(fib)

fib.append(89)
print(fib)

fib.pop()
print(fib)

fib.append(89)
print(fib)
fib.append(89)

fib.remove(89)
#remember the remove function removes the first instance of the number passeed into the parenthesis
print(fib)
fib.append(89)

del(fib[2])
print("\n")
print(fib)

chars=["mario","luigi","browser"]
chars.append(5)
print(chars)
#you can see we can append whatever be the type of the variabl eeto the list 

#list within the list 
print("\n")
nums=[chars,fib1,[1,2,3,4,5]]
print(nums)
print(nums[1])
#print the fib

print("\n")
#no what if we have to access the the index within the list of thre list
print(nums[2][1])
#first locate the lisst and then locate the desired element 











