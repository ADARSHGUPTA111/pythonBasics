with open('files/write.txt','w') as write_file:
	write_file.write("Hey there ninjas , python is awesome")
	write_file.write("\n i am a ninja and i love it so much , python is awesome")

# with open('files/write.txt','w') as write_file:
	# write_file.write("\n I love many people , but i dont show them!")

#when we open it again (with intent to 'w' ) it overrides whathever was written earlier 
#that is whatever written earlier is erased!

with open('files/write.txt','a') as write_file:
	write_file.write("\n I love many people , but i dont show them!")

#but if 'a' is passed then the writing material gets appended to it!

quotes=[
'\n I can resist everything eexcept temptation',
'\n We are all in gutter , but some of us are looking at the stars',
'\n Always forgive your enemies , nothing annoys them so much'
]

with open('files/write.txt','a') as write_file:
	write_file.writelines(quotes)


