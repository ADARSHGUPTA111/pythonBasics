prizes=[5,10,50,100,1000]

dbl_prizes=[]

for prize in prizes:
	dbl_prizes.append(prize*2)

print(dbl_prizes)

#comprehension meethod :
dbl_prizes=[prize*2 for prize in prizes]
#in [what and in what]
print(dbl_prizes)

#squaring numbers
nums=[1,2,3,4,5,6,7,8,9,10]

squared_even_numbers=[]
for num in nums:
	if (num**2)%2==0:
		squared_even_numbers.append(num**2)

print(squared_even_numbers)

#comprehension method
squared_even_numbers=[num**2 for num in nums if (num**2)%2==0]
#in [what in what with condition if any]
print(squared_even_numbers)