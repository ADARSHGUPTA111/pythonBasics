demo_file=open('files/demo.txt')

for line in demo_file:
	print(line)

for line in demo_file:
	print(line.rstrip())

#the gaps are stripped out  

lines=demo_file.readlines()
print(lines)
#returns the empty list as we had already read the file in the above code

demo_file.seek(0)
#we are basically telling the computer to seek the very first (0th) character in the file 

lines2=demo_file.readlines()
print(lines2)
#now each line is stored as a different elements of the list here 

demo_file.seek(50)
file_text=demo_file.read(100)
#rhis starts from the 50 char and read more 100 chars ffrom that point
print(file_text)

demo_file.close()




'''
#using without the file.close()

def sequence_filter(line):
	return '>' not in line

with open("files/summer2k19.docx") as summer2k19_file:
	lines=summer2k19_file.readlines()
	print(list(filter(sequence_filter,lines)))
	'''

