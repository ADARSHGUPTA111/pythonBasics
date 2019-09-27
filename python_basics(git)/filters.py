grades =['A','B','F',"F",'C','A']

def remove_fails(grade):
	return grade!='F'

# filter(testing_function,data)

print(filter(remove_fails,grades))
# this gives <filter object at 0x04FC0710> therefore we shall typecast it into a list

print(list(filter(remove_fails,grades)))

filtered_grades=[]
for grade in grades:
	if grade!='F':
		filtered_grades.append(grade)

print(filtered_grades)

#comprehension

print([grade for grade in grades if grade!='F'])

