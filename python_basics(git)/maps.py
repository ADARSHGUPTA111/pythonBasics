#new_list=map(function,data)
from random import shuffle

def jumble (word):
	anagram=list(word)
	#it does seperate every character in the word and then lists them
	#eg:adarsh [s,r,a,d,h,a]
	shuffle(anagram)
	return ''.join(anagram)
	#concatenates every letter without space

words= ['beetroot','potatoes','carrots']

anagrams=[]

for word in words:
	anagrams.append(jumble(word))

print(anagrams)

#same thing using maps
#it maps the function for everything in the existing list 
print(list(map(jumble,words)))

#same thing using list comprehension
print([jumble(word) for word in words])